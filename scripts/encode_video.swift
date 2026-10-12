// Native macOS H.264 encoder for original Workshop demonstration frames.
// Usage: swift encode_video.swift FRAMES OUTPUT.mp4 WIDTH HEIGHT FPS HOLD_SECONDS
// Input frames must be lexically named shot-01.png, shot-02.png, ... .
import Foundation
import AVFoundation
import AppKit
import CoreVideo

func fail(_ message: String) -> Never {
    FileHandle.standardError.write(Data((message + "\n").utf8))
    exit(1)
}
let args = CommandLine.arguments
if args.count != 7 { fail("Usage: encode_video.swift FRAMES OUTPUT.mp4 WIDTH HEIGHT FPS HOLD_SECONDS") }
let source = URL(fileURLWithPath: args[1], isDirectory: true)
let destination = URL(fileURLWithPath: args[2])
guard let width = Int(args[3]), let height = Int(args[4]), let fps = Int32(args[5]), let hold = Int(args[6]), width > 0, height > 0, fps > 0, hold > 0 else { fail("Invalid video dimensions or duration") }
let urls = try FileManager.default.contentsOfDirectory(at: source, includingPropertiesForKeys: nil).filter { $0.lastPathComponent.hasPrefix("shot-") && $0.pathExtension == "png" }.sorted { $0.lastPathComponent < $1.lastPathComponent }
if urls.isEmpty { fail("No shot PNGs were found") }
try? FileManager.default.removeItem(at: destination)
let writer = try AVAssetWriter(outputURL: destination, fileType: .mp4)
writer.shouldOptimizeForNetworkUse = true
let settings: [String: Any] = [
    AVVideoCodecKey: AVVideoCodecType.h264,
    AVVideoWidthKey: width, AVVideoHeightKey: height,
    AVVideoCompressionPropertiesKey: [
        AVVideoAverageBitRateKey: 220_000,
        AVVideoProfileLevelKey: AVVideoProfileLevelH264HighAutoLevel,
        AVVideoMaxKeyFrameIntervalKey: Int(fps) * hold,
        AVVideoExpectedSourceFrameRateKey: Int(fps)
    ]
]
let input = AVAssetWriterInput(mediaType: .video, outputSettings: settings)
input.expectsMediaDataInRealTime = false
let attributes: [String: Any] = [
    kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32ARGB,
    kCVPixelBufferWidthKey as String: width,
    kCVPixelBufferHeightKey as String: height,
    kCVPixelBufferCGImageCompatibilityKey as String: true,
    kCVPixelBufferCGBitmapContextCompatibilityKey as String: true
]
let adaptor = AVAssetWriterInputPixelBufferAdaptor(assetWriterInput: input, sourcePixelBufferAttributes: attributes)
if !writer.canAdd(input) { fail("AVFoundation rejected the H.264 video track") }
writer.add(input)
if !writer.startWriting() { fail("Could not start video writing: \(String(describing: writer.error))") }
writer.startSession(atSourceTime: .zero)
var index: Int64 = 0
for url in urls {
    guard let image = NSImage(contentsOf: url), let cgImage = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else { fail("Cannot read PNG: \(url.path)") }
    var created: CVPixelBuffer?
    let status = CVPixelBufferCreate(kCFAllocatorDefault, width, height, kCVPixelFormatType_32ARGB, attributes as CFDictionary, &created)
    guard status == kCVReturnSuccess, let buffer = created else { fail("Could not allocate video pixel buffer") }
    CVPixelBufferLockBaseAddress(buffer, [])
    guard let context = CGContext(data: CVPixelBufferGetBaseAddress(buffer), width: width, height: height, bitsPerComponent: 8, bytesPerRow: CVPixelBufferGetBytesPerRow(buffer), space: CGColorSpaceCreateDeviceRGB(), bitmapInfo: CGImageAlphaInfo.premultipliedFirst.rawValue) else { fail("Could not create PNG drawing context") }
    context.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))
    CVPixelBufferUnlockBaseAddress(buffer, [])
    for _ in 0..<(hold * Int(fps)) {
        while !input.isReadyForMoreMediaData {
            if writer.status == .failed { fail("Video encoder failed: \(String(describing: writer.error))") }
            Thread.sleep(forTimeInterval: 0.01)
        }
        let timestamp = CMTime(value: index, timescale: fps)
        if !adaptor.append(buffer, withPresentationTime: timestamp) { fail("Could not append video frame: \(String(describing: writer.error))") }
        index += 1
    }
}
writer.endSession(atSourceTime: CMTime(value: index, timescale: fps))
input.markAsFinished()
let completion = DispatchSemaphore(value: 0)
writer.finishWriting { completion.signal() }
completion.wait()
if writer.status != .completed { fail("Video did not finish successfully: \(String(describing: writer.error))") }
let asset = AVURLAsset(url: destination)
let duration = CMTimeGetSeconds(asset.duration)
guard duration.isFinite, abs(duration - Double(index) / Double(fps)) < 0.1 else { fail("Encoded duration differs from the requested duration") }
let metadata: [String: Any] = ["file": destination.lastPathComponent, "seconds": duration, "width": width, "height": height, "frames": index, "fps": fps, "bytes": (try FileManager.default.attributesOfItem(atPath: destination.path)[.size] as? NSNumber)?.intValue ?? 0]
let data = try JSONSerialization.data(withJSONObject: metadata, options: [.sortedKeys])
print(String(decoding: data, as: UTF8.self))

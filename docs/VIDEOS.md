# 六段真实 Tcl 代码演示

网站的六段视频已提供 MP4、封面、WebVTT 中文字幕与可阅读逐字稿。每段为 60 秒、12 个镜头，每个镜头保留 5 秒，便于暂停、阅读和复制对应课程代码。视频无配音，中文字幕已经嵌入画面；VTT 同时供网页字幕轨道使用。

| 单元 | 主题 | 课程 | 视频 | 字幕 | 逐字稿 |
| --- | --- | --- | --- | --- | --- |
| 1 | 运行第一个 Tcl 脚本 | 01 | [MP4](../site/media/unit-1.mp4) | [VTT](../site/media/unit-1.vtt) | [文字](../site/media/unit-1.txt) |
| 2 | 使用循环处理列表 | 05、06 | [MP4](../site/media/unit-2.mp4) | [VTT](../site/media/unit-2.vtt) | [文字](../site/media/unit-2.txt) |
| 3 | 清理文本并观察结果 | 07–09 | [MP4](../site/media/unit-3.mp4) | [VTT](../site/media/unit-3.vtt) | [文字](../site/media/unit-3.txt) |
| 4 | 读取文件与处理错误 | 11、12 | [MP4](../site/media/unit-4.mp4) | [VTT](../site/media/unit-4.vtt) | [文字](../site/media/unit-4.txt) |
| 5 | 使用过程组织代码 | 10、13 | [MP4](../site/media/unit-5.mp4) | [VTT](../site/media/unit-5.vtt) | [文字](../site/media/unit-5.txt) |
| 6 | 分析教学版 VLSI 报告 | 17、18 | [MP4](../site/media/unit-6.mp4) | [VTT](../site/media/unit-6.vtt) | [文字](../site/media/unit-6.txt) |

## 画面与执行结果的来源

这些是原创的、脚本生成的代码讲解视频，画面呈现清晰的代码与输出工作台。它们没有录制浏览器鼠标点击，也不应被描述为网站操作实录。

`scripts/render_media.py` 从课程单一来源读取可运行例子，再构造少量明确的新输入。每个不同的代码与文件组合都调用 `scripts.check.native`，在新的临时目录和真正的 Tcl 解释器中运行。输出面板直接使用解释器的标准输出；错误镜头直接使用解释器返回的错误。原例子还会核对课程里的预期输出。每个镜头的代码、教学文件、实际输出和错误完整写入逐字稿，源码哈希与 Tcl 版本写入 [生成记录](../site/media/generation-report.json)。重复镜头复用同一次已执行结果，不伪造额外的执行过程。

代码在画面中可能视觉折行；执行的源字符串保持完整。代码高亮是字幕对应位置的静态教材提示，不能视为解释器执行追踪。字幕会明确说明数据变化，避免以颜色作为唯一信息。没有闪烁、音效和持续运动；时间进度仅在镜头切换时变化。视频不会自动播放，使用浏览器播放控件即可暂停、跳转或全屏。阅读困难时可直接打开课程和逐字稿。

本批演示使用真实 Tcl 9.0.4。网页运行时的版本由网站单独报告；视频没有把本地解释器版本冒充为浏览器版本。文件演示仅访问随镜头预置的原创教学文件。网页文件属于浏览器虚拟文件系统；视频文件属于临时本地目录，两者都不表示访问作者私人电脑。VLSI 片段采用课程的简化模型 `slack = period - delay`，不接入商业 EDA 软件，也不替代真实 STA。

## 再生成

需要 Python 3、Pillow、真实 Tcl，以及 macOS 自带的 Swift/AVFoundation 编码器。默认优先通过 `tclsh` 执行；若使用带 tkinter 的 Python，可指定原生 Tcl 库：

```sh
WORKSHOP_USE_TK=1 python3 scripts/render_media.py --encode
python3 scripts/build.py
```

先只生成封面、逐字稿、字幕和可检查的镜头 PNG：

```sh
WORKSHOP_USE_TK=1 python3 scripts/render_media.py --frames-dir /tmp/tcl-workshop-frames
```

在普通 macOS 终端单独编码某一段：

```sh
swift -module-cache-path /tmp/tcl-workshop-swift-cache \
  scripts/encode_video.swift \
  /tmp/tcl-workshop-frames/unit-1 site/media/unit-1.mp4 \
  1280 720 2 5
```

最后五个参数依次为输出路径、宽、高、帧率和每个镜头停留秒数。12 张图、2 帧/秒、每镜头 5 秒得到 60 秒视频。低帧率适合本项目静态代码阅读；它不是动态屏幕录制的参数建议。H.264 MP4 配置网络播放优化，输出包含 `moov` 元数据与真实视频轨道。

系统编码器需要访问 macOS 媒体服务。若受限执行环境出现 AVFoundation `-11834 Cannot Encode`，先生成镜头，再在能访问系统编码器的本地终端运行上述 Swift 命令。本项目实际生成时已验证此问题来自执行沙箱，允许本地编码进程访问系统媒体服务后成功。生成脚本会报告失败，不会把不存在或失败的 MP4 声称为已经生成。

仅更新某一段可加 `--unit 3`。完整发行前应再次不带 `--unit` 运行，以更新全部六段和统一的生成记录。建议检查视频时长、实际可播放状态、几个首尾镜头，以及字幕末尾是否到达 60 秒。

## 字体与第三方组件

代码和画面均为本项目原创。渲染使用 Pillow 与 macOS 已安装的 STHeiti/Menlo 字体；仓库不分发字体文件。编码使用系统 AVFoundation，不下载或捆绑编解码器。维护者可通过 `WORKSHOP_VIDEO_FONT` 与 `WORKSHOP_VIDEO_MONO_FONT` 指定本地已授权的中文和等宽字体。选择其他字体后需重新检查文字折行与可读性。

# 错误处理与调试：让失败说清原因 / 缺失文件给出可理解提示
set status [catch {open missing.txt r} result options]
if {$status == 0} {
    close $result
    puts "文件已打开"
} else {
    puts "未读取：请确认 missing.txt 已放入输入文件"
    puts "错误状态：$status"
}

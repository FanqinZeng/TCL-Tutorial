# 错误处理与调试：让失败说清原因 / 把输入检查封装在过程里
proc parseCount {text} {
    if {![string is integer -strict $text] || $text < 0} {
        error "数量必须是非负整数"
    }
    return $text
}
foreach text {3 -1 abc} {
    if {[catch {parseCount $text} result]} {
        puts "$text：$result"
    } else {
        puts "$text：接收 $result"
    }
}

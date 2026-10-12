# 错误处理与调试：让失败说清原因 / 区分除零错误与计算成功
foreach divisor {2 0} {
    set status [catch {expr {8 / $divisor}} result]
    if {$status == 0} {
        puts "结果：$result"
    } else {
        puts "失败：$result"
    }
}

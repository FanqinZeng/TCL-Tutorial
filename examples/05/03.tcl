# 重复处理 / 清空待处理数量，并找到首个异常
set pending 3
while {$pending > 0} {
    puts "剩余：$pending"
    incr pending -1
}
foreach value {12 15 31 18} {
    if {$value > 30} {
        puts "首个异常：$value"
        break
    }
}

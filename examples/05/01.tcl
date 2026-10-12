# 重复处理 / 跳过失败读数
set count 0
set total 0
foreach value {18 21 -1 19 23} {
    if {$value < 0} {continue}
    incr count
    set total [expr {$total + $value}]
}
puts "有效次数：$count"
puts "总和：$total"

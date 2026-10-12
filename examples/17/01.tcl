# 约束与报告：用教学路径看懂 slack / 一个周期，两种路径延迟
set period 10.0
foreach delay {8.2 10.8} {
    set slack [expr {$period - $delay}]
    puts [format "延迟 %.2f ns → slack %.2f ns" $delay $slack]
}

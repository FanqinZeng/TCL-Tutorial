# 约束与报告：用教学路径看懂 slack / 负 slack 从最需要关注的开始
set period 10.0
set pairs {}
foreach {path delay} {data_a 8.2 data_b 10.8 data_c 11.5} {
    set slack [expr {$period - $delay}]
    if {$slack < 0} { lappend pairs [list $slack $path] }
}
foreach pair [lsort -real -index 0 $pairs] {
    lassign $pair slack path
    puts [format "%s | %.2f ns" $path $slack]
}

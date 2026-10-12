# 文件读写：为实验数据留下摘要 / 生成并验证摘要
set ch [open readings.txt r]
set values [split [string trim [read $ch]] "
"]
close $ch
set total 0.0
foreach value $values { set total [expr {$total + $value}] }
set count [llength $values]
set out [open summary.txt w]
puts $out "数量：$count"
puts $out [format "平均值：%.2f" [expr {$total / $count}]]
close $out
set check [open summary.txt r]
puts [string trim [read $check]]
close $check

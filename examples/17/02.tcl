# 约束与报告：用教学路径看懂 slack / 从一行教学报告提取字段
set line "PATH data_a DELAY 10.8"
if {![regexp {^PATH\s+(\S+)\s+DELAY\s+([0-9]+(?:\.[0-9]+)?)$} $line -> path delay]} {
    error "不是约定的教学报告格式"
}
set record [dict create path $path delay $delay slack [expr {10.0 - $delay}]]
puts "路径：[dict get $record path]"
puts [format "slack：%.2f ns" [dict get $record slack]]

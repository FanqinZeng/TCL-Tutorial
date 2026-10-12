# 自动生成分析摘要：把整条处理链连起来 / 写出一份教学摘要
source report-tools.tcl
set result [collectReports {morning.rpt evening.rpt} 10]
set summary [summarizeRecords [dict get $result records]]
set output [open analysis.txt w]
puts $output "教学分析摘要（全部输入已处理）"
puts $output "路径：[dict get $summary count]"
puts $output "负 slack：[dict get $summary negative]"
puts $output [format "最差 slack：%.2f ns" [dict get $summary worst]]
close $output
set input [open analysis.txt r]
puts [string trim [read $input]]
close $input

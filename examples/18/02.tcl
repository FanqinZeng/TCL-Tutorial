# 自动生成分析摘要：把整条处理链连起来 / 坏报告不混入有效统计
source report-tools.tcl
set result [collectReports {morning.rpt bad.rpt} 10]
set summary [summarizeRecords [dict get $result records]]
puts "部分结果：成功 [dict get $result loaded] 份，失败 [llength [dict get $result issues]] 份"
puts "有效路径：[dict get $summary count]"
foreach issue [dict get $result issues] { puts [dict get $issue message] }

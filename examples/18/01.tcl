# 自动生成分析摘要：把整条处理链连起来 / 两份报告合成一组记录
source report-tools.tcl
set result [collectReports {morning.rpt evening.rpt} 10]
puts "成功文件：[dict get $result loaded]"
foreach record [dict get $result records] {
    puts [format "%s:%d %s slack=%.2f ns" [dict get $record source] [dict get $record line] [dict get $record path] [dict get $record slack]]
}

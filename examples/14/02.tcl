# 脚本组织与参数：用同一套工具生成不同报告 / 读取本次运行参数
if {$argc != 2} { error "用法：main.tcl <报告名称> <输入文件>" }
lassign $argv reportName inputPath
puts "报告名称：$reportName"
puts "输入文件：$inputPath"

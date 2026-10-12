# 脚本组织与参数：用同一套工具生成不同报告 / 配置控制显示精度
set config [source settings.tcl]
source tools.tcl
puts [dict get $config title]
puts [formatAverage {1.2 1.4 1.6} [dict get $config digits]]

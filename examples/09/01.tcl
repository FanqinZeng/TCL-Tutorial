# 正则表达式入门 / 不用正则的对照：固定字段
set line {09:15 23 OK}
set fields [split $line " "]
puts "时间：[lindex $fields 0]"
puts "值：[lindex $fields 1]"
puts "状态：[lindex $fields 2]"
puts [string match {ERROR:*} {ERROR: input missing}]

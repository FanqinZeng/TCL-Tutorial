# 字符串处理 / 连续分隔符与空元素
set raw {甲;;乙,丙}
set items [split $raw ",;"]
puts "分段数：[llength $items]"
puts [join $items " | "]
puts "第二段长度：[string length [lindex $items 1]]"
puts [string trim "  林 雨  "]

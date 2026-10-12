# 列表 / 含空格姓名仍是三个元素
set names [list "林 雨" "Chen Ming" 赵安]
puts "人数：[llength $names]"
puts "第一位：[lindex $names 0]"
puts "最后一位：[lindex $names end]"

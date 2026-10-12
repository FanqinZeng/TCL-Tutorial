# 字符串处理 / 分组说明变成可读列表
set raw "alpha;beta;gamma"
set groups [split $raw ";"]
puts "组数：[llength $groups]"
puts [join $groups " / "]
puts [string toupper [lindex $groups 0]]

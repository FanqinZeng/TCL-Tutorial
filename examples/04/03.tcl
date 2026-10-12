# 条件判断 / 编号文字与数值意义
set a "01"
set b "1"
puts [expr {$a eq $b}]
puts [expr {$a == $b}]
set remaining 0
if {$remaining == 0} {puts "名额已满"}

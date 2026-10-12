# Tcl 的三种重要符号 / 计算结果嵌入消息
set name "林 雨"
set price 12
set quantity 3
puts "$name，你的材料费为 [expr {$price * $quantity}] 元"

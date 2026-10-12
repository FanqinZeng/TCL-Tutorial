# 变量与计算 / 采购总价
set price 18
set quantity 3
set shipping 6
set total [expr {$price * $quantity + $shipping}]
puts "总价：$total 元"

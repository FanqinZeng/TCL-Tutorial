# 变量与计算 / 整数除法与均价
puts [expr {5 / 2}]
puts [expr {5 / 2.0}]
set subtotal 47
set pieces 4
set average [expr {double($subtotal) / $pieces}]
puts [format "平均：%.2f 元" $average]

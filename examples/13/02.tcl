# 作用域与命名空间：给工具安排各自的位置 / 两个同名费用工具共存
namespace eval travel {
    proc fee {people} { return [expr {$people * 12}] }
}
namespace eval food {
    proc fee {people} { return [expr {$people * 18}] }
}
puts "交通：[::travel::fee 3]"
puts "餐食：[::food::fee 3]"

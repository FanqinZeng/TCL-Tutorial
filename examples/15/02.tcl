# TclOO 入门：两台仪器，各自记住测量值 / 两个对象互不混用记录
oo::class create CounterMeter {
    variable readings
    constructor {} { set readings {} }
    method add {value} { lappend readings $value }
    method count {} { return [llength $readings] }
}
set first [CounterMeter new]
set second [CounterMeter new]
$first add 10
$first add 20
$second add 8
puts "第一台：[$first count] 条"
puts "第二台：[$second count] 条"
$first destroy
$second destroy

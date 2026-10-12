# TclOO 入门：两台仪器，各自记住测量值 / 一台仪器记录两次数值
oo::class create Meter {
    variable readings
    constructor {} { set readings {} }
    method add {value} { lappend readings $value }
    method values {} { return $readings }
}
set m [Meter new]
$m add 1.2
$m add 1.5
puts "记录：[$m values]"
$m destroy

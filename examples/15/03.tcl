# TclOO 入门：两台仪器，各自记住测量值 / 空数据状态与销毁后的命令
oo::class create AverageMeter {
    variable values
    constructor {} { set values {} }
    method add {x} { lappend values $x }
    method average {} {
        if {[llength $values] == 0} { return {无数据} }
        set total 0.0
        foreach x $values { set total [expr {$total + $x}] }
        return [format "%.2f" [expr {$total / [llength $values]}]]
    }
}
set m [AverageMeter new]
puts [$m average]
$m add 2
$m add 4
puts [$m average]
$m destroy
puts "销毁后存在：[expr {[llength [info commands $m]] > 0}]"

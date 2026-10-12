# 作用域与命名空间：给工具安排各自的位置 / 命名空间状态跨调用保留
set total 999
namespace eval ledger {
    variable total 0
    proc add {amount} {
        variable total
        set total [expr {$total + $amount}]
        return $total
    }
}
puts "累计：[::ledger::add 12]"
puts "累计：[::ledger::add 8]"
puts "外部 total：$total"

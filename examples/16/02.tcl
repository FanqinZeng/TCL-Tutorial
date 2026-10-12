# Tcl 与 EDA 工具：先分清谁提供了命令 / 用字典记录演示筛选
set cells [list     [dict create name U_AND kind AND2 area 1.2]     [dict create name U_BUF kind BUF area 0.5]     [dict create name CLK_BUF kind BUF area 0.8]]
foreach cell $cells {
    if {[dict get $cell kind] eq "BUF"} {
        puts "[dict get $cell name]：[dict get $cell area]"
    }
}

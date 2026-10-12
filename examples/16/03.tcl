# Tcl 与 EDA 工具：先分清谁提供了命令 / 可见实现的教学工具命令
namespace eval demoeda {
    variable cells [list         [dict create name U_AND kind AND2]         [dict create name U_BUF kind BUF]         [dict create name CLK_BUF kind BUF]]
    proc get_cells {pattern} {
        variable cells
        set selected {}
        foreach cell $cells {
            if {[string match $pattern [dict get $cell name]]} {
                lappend selected [dict get $cell name]
            }
        }
        return $selected
    }
}
puts "教学查询：[::demoeda::get_cells U_*]"
puts "无匹配数量：[llength [::demoeda::get_cells X_*]]"

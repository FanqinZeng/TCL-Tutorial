# Tcl 与 EDA 工具：先分清谁提供了命令 / 普通 Tcl 中哪些命令存在
puts "Tcl 的 dict：[expr {[llength [info commands dict]] > 0}]"
puts "工具的 get_cells：[expr {[llength [info commands get_cells]] > 0}]"
if {[catch {get_cells *} message]} {
    puts "当前没有 EDA 工具命令；先加载教学模型"
}

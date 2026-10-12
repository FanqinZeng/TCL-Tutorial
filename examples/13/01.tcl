# 作用域与命名空间：给工具安排各自的位置 / 局部变量与明确的全局计数
set visits 0
proc visit {} {
    global visits
    incr visits
    set note "本次调用的局部备注"
    return $visits
}
puts [visit]
puts [visit]
puts "全局 visits：$visits"

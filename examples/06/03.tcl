# 列表 / 排序与保持原顺序去重
set durations {12 3 20 3}
puts [lsort -integer -unique $durations]
set names [list "林 雨" "Chen Ming" "林 雨" 赵安]
set unique {}
foreach name $names {
    if {[lsearch -exact $unique $name] < 0} {
        lappend unique $name
    }
}
puts [join $unique " / "]

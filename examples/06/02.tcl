# 列表 / 追加、区间与精确查找
set names [list "林 雨" "Chen Ming" 赵安]
lappend names "许 岚"
puts [join [lrange $names 1 2] " / "]
puts [lsearch -exact $names "许 岚"]
puts [lsearch -exact $names "不存在"]

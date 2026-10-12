# 字典与数组 / 创建和更新设备记录
set device [dict create id LAB-07 location "北区 台位" status ready runs 2]
puts "位置：[dict get $device location]"
dict set device status busy
dict set device runs [expr {[dict get $device runs] + 1}]
puts "状态：[dict get $device status]，次数：[dict get $device runs]"

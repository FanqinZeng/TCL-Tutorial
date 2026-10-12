# 字典与数组 / 数组按键排序展示
array set readings {north 21 south 24}
set readings(north) 22
foreach key [lsort [array names readings]] {
    puts "$key：$readings($key)"
}
puts "西区存在：[info exists readings(west)]"
puts "它是数组：[array exists readings]"

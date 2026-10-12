# 字典与数组 / 可选字段缺失时提供说明
set sample [dict create id S-12 temperature 23.5]
if {[dict exists $sample owner]} {
    puts "负责人：[dict get $sample owner]"
} else {
    puts "负责人：未登记"
}
dict set sample owner "顾 宁"
puts "负责人：[dict get $sample owner]"

# 条件判断 / 报名状态与人数一起检查
set status "confirmed"
set people 2
if {$status eq "confirmed" && $people > 0} {
    puts "可以制作名牌"
} else {
    puts "等待有效报名"
}

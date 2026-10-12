# 条件判断 / 根据预算选择材料包
set budget 75
if {$budget >= 90} {
    set plan "扩展包"
} elseif {$budget >= 60} {
    set plan "标准包"
} elseif {$budget >= 30} {
    set plan "基础包"
} else {
    set plan "暂缓采购"
}
puts $plan

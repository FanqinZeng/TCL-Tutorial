# 过程与参数：把费用计算装进工具 / 同一个过程计算两张订单
proc fee {quantity price} {
    return [expr {$quantity * $price}]
}
puts [fee 3 12]
puts [fee 2 8]

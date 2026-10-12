# 过程与参数：把费用计算装进工具 / 可省略的运费
proc deliveredFee {quantity price {delivery 0}} {
    return [expr {$quantity * $price + $delivery}]
}
puts [format "自提：%.2f 元" [deliveredFee 2 9.5]]
puts [format "配送：%.2f 元" [deliveredFee 2 9.5 4]]

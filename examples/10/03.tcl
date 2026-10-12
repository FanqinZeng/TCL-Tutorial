# 过程与参数：把费用计算装进工具 / 过程内外的同名变量
set subtotal 999
proc discountFee {price} {
    set subtotal [expr {$price * 0.9}]
    return $subtotal
}
set result [discountFee 20]
puts [format "返回值：%.2f" $result]
puts "外部 subtotal：$subtotal"

# 正则表达式入门 / 对不符合约定的行明确处理
set pattern {^([0-9]{2}:[0-9]{2}) value=(-?[0-9]+) status=(OK|WARN|ERROR)$}
foreach line [list {10:02 value=-3 status=WARN} {broken row} {10:03 value=7 status=UNKNOWN}] {
    if {[regexp -- $pattern $line whole time value status]} {
        puts "$time / $value / $status"
    } else {
        puts "无法解析：$line"
    }
}

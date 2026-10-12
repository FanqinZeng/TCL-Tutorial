# 正则表达式入门 / 三个小捕获组
set line {09:15 value=23 status=OK}
set pattern {^([0-9]{2}:[0-9]{2}) value=(-?[0-9]+) status=(OK|WARN|ERROR)$}
if {[regexp -- $pattern $line whole time value status]} {
    puts "时间：$time"
    puts "值：$value"
    puts "状态：$status"
}

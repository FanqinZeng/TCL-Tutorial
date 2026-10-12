# 文件读写：为实验数据留下摘要 / 读取整份记录
set ch [open readings.txt r]
set text [read $ch]
close $ch
puts [string trim $text]

# 文件读写：为实验数据留下摘要 / 空白行不等于文件末尾
set ch [open notes.txt r]
set count 0
while {[gets $ch line] >= 0} {
    incr count
    puts "$count：[string length $line] 个字符"
}
close $ch

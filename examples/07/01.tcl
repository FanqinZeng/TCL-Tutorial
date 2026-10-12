# 字符串处理 / 规范邮箱文字
set raw "  LI.MING@EXAMPLE.ORG  "
set email [string tolower [string trim $raw]]
puts "原始：<$raw>"
puts "清理：<$email>"
puts [string match {*@example.org} $email]

# Tcl 速查与常见错误 / Tcl reference

本页供完成课程后随手查阅。代码面向 Tcl 8.6 及以上；运行 `puts [info patchlevel]` 可查看当前解释器。浏览器运行时和本地解释器的版本、打包来源与限制由[运行说明](../README.md)和[第三方说明](../THIRD_PARTY_NOTICES.md)记录。这里的 EDA 数据与筛选过程均为教学模型。

## 先记住命令与替换 / Commands and substitution

Tcl 脚本由命令组成；通常以换行或分号结束命令，空白分隔命令中的词。第一个词是命令名，后面是参数。用引号或花括号可以把含空格的内容保留为一个词。替换发生在词内，替换结果不会自动重新按空格切成多个参数。[官方语法规则](https://www.tcl-lang.org/man/tcl8.6/TclCmd/Tcl.htm)

| 写法 | 作用 | 例子 |
|---|---|---|
| `$name` | 读取变量值 | `puts $name` |
| `${name}` | 明确变量名边界 | `puts "${name}: ready"` |
| `[command ...]` | 执行命令，用返回值替换 | `puts [expr {2 + 3}]` |
| `"..."` | 分组成一个词；允许变量、命令和反斜杠替换 | `puts "Hello, $name"` |
| `{...}` | 分组成一个词；阻止这一层通常的替换 | `puts {$name [expr {2+3}]}` |
| `\` 接换行 | 将换行与随后缩进压成一个空格；花括号内也适用 | 把一条长命令分成多行 |

`expr {...}`、`if {...}`、`while {...}` 收到的内容会由相应命令按表达式规则继续解释。因此 `expr {$a + 1}` 能读取变量：花括号延迟脚本解析层的替换，表达式解析器再读取 `$a`。表达式中花括号也帮助保留 `&&`、`||` 和条件运算的短路行为。[expr 官方手册](https://www.tcl-lang.org/man/tcl8.6/TclCmd/expr.htm)

Tcl commands are sequences of words. Whitespace separates words; a newline or semicolon normally ends a command. Substitution replaces content inside a word and does not automatically split the result into extra arguments. Quotes group words while permitting substitutions. Braces suppress ordinary substitutions at the script-parsing layer; backslash-newline is an exception. A receiving command such as `expr` can interpret the braced value using its own rules. [Syntax](https://www.tcl-lang.org/man/tcl8.6/TclCmd/Tcl.htm), [expressions](https://www.tcl-lang.org/man/tcl8.6/TclCmd/expr.htm)

## 18 节课速查 / Course cheatsheet

以下是可复制的简短写法，每一行的例子可独立理解；不要把不同单元的所有行机械地拼成一个脚本。

| 课 | 常用写法 | 记忆要点 / Reminder |
|---|---|---|
| 01 | `puts "欢迎参加工作坊"`；`# 注释` | `puts` 显示输出。注释出现在解析器期待命令开头的位置。 / Comments belong where a command can begin. |
| 02 | `set n 3`；`incr n`；`expr {$n * 2}` | `set` 赋值不带 `$`，读取值才带 `$`。 / Write a variable name; read its value. |
| 03 | `set name Mei`；`puts "$name"`；`puts {$name}` | 前者输出值，后者输出字面 `$name`。 / Quotes substitute; braces preserve here. |
| 04 | `if {$n > 0} {puts yes} else {puts no}` | 字符串明确用 `eq/ne`，数值用 `< > <= >=`。 / Choose comparison intent explicitly. |
| 05 | `foreach x {2 4 6} {puts $x}` | `continue` 跳过当前迭代；`break` 离开当前循环。 / Skip an iteration or end a loop. |
| 06 | `set names [list "Lin Wei" Mei]`；`lappend names Kai` | 列表保存元素边界，含空格姓名仍是一个元素。 / Construct lists rather than joining arbitrary text. |
| 06 | `llength $names`；`lindex $names 0`；`lrange $names 0 1` | 索引从 0 开始；`end` 指最后一个元素。 / Indices start at zero. |
| 06 | `lsearch -exact $names Mei`；`lsort -dictionary -unique $names` | 没找到时 `lsearch` 返回 -1；数值排序用 `-integer` 或 `-real`。 / Pick the sort mode. |
| 07 | `string trim "  Mei  "`；`string tolower "ABC"` | 清理首尾，不擅自删掉内容中的必要空格。 / Trim boundaries intentionally. |
| 07 | `string match {probe-*} probe-a`；`join [split "a,b" ,] { / }` | `string match` 是 glob 模式；不是正则。`split` 的分隔符参数是一组字符。 / Match and split have distinct rules. |
| 08 | `set item [dict create name probe value 12]`；`dict get $item value` | `dict` 是一个可传递的值；用 `dict exists` 先查字段。 / Dictionaries are values. |
| 08 | `array set itemArray {name probe value 12}`；`set itemArray(value)` | `array` 是变量集合，不能直接 `puts $itemArray`；数组键顺序不保证。 / Arrays are variables, not scalar dictionary values. |
| 09 | `regexp {^([0-9]+) ms$} "12 ms" whole milliseconds` | 第一个接收变量保存完整匹配，后面保存捕获组。 / Match result first, captures next. |
| 10 | `proc cost {n {price 2}} {return [expr {$n * $price}]}`；`cost 3` | 返回值用于组合；`puts` 输出给人看。 / Returning and printing are different. |
| 11 | `set ch [open input.txt r]`；`read $ch`；`close $ch` | 通道要关闭；文本可用 `fconfigure $ch -encoding utf-8`。 / Close channels and choose text encoding. |
| 11 | `while {[gets $ch line] >= 0} {puts $line}` | 空行也是成功读取，长度为 0；用 `>= 0` 判断。 / An empty line is not end-of-file. |
| 12 | `catch {error "输入无效"} message options` | 返回 0 表示正常，1 表示错误；还有其他 Tcl 控制返回码。 / Catch returns a completion code. |
| 12 | `dict get $options -errorinfo` | 错误信息与调用栈用于定位；不能每次失败都显示“成功”。 / Preserve useful error information. |
| 13 | `namespace eval report {variable count 0}` | 过程的局部变量与命名空间变量不同；需要时用 `variable` 链接。 / Scope is explicit. |
| 14 | `source -encoding utf-8 tools.tcl`；`lindex $argv 0` | `source` 执行脚本；`argc` 是参数数量，`argv` 是列表。 / Load trusted scripts; arguments form a list. |
| 15 | `oo::class create Meter {method read {} {return 12}}`；`set m [Meter new]`；`$m read`；`$m destroy` | 对象适合保存状态；简单计算过程也可以足够。 / Use an object when state makes it useful. |
| 16 | `info commands get_cells` | 命令是否存在取决于宿主；浏览器 Tcl 没有商业 EDA 连接。 / Tool commands come from their host. |
| 17 | `expr {$period - $delay}` | 仅是课程的简化 slack 模型；真实 STA 包含更多因素。 / State model assumptions. |
| 18 | `dict incr totals $category $amount` | 先验证，再累计，最后独立生成报告和错误记录。 / Validate, aggregate, then report. |

列表和字典的细节见 [list](https://www.tcl-lang.org/man/tcl8.6/TclCmd/list.htm)、[lsort](https://www.tcl-lang.org/man/tcl8.6/TclCmd/lsort.htm)、[dict](https://www.tcl-lang.org/man/tcl8.6/TclCmd/dict.htm)；数组是不同的变量类型，见 [array](https://www.tcl-lang.org/man/tcl8.6/TclCmd/array.htm)。

## 六个稳妥习惯 / Six useful habits

1. **计算表达式使用花括号。** `expr {$a / 2.0}` 让表达式解析器读取数据，也清楚地要求浮点除法。Use braced expressions and choose integer or floating-point arithmetic deliberately.
2. **使用 `list` 保存元素。** `list "Ana Park" "Zoe Li"` 保留两个姓名；`split` 整段文字会丢失你原本想保留的边界。Construct values with list commands.
3. **验证后再读取字段。** 用 `dict exists` 处理缺字段，用适合需求的数值检查拒绝非法输入；`string is double` 本身不等于“有限数”。Validate input rules before computing.
4. **算法返回结果，输出过程显示结果。** 这便于用另一份输入验证相同过程，避免把样例写死。Separate reusable return values from display.
5. **显式关闭文件。** 成功打开之后用 `try { ... } finally {close $ch}`；若 `open` 失败则没有可关闭的通道。Close channels on both successful and failing paths.
6. **清楚记录模型边界。** 所有教程版路径公式、模拟设计对象和演示日志都要保留教学标签。Label simplified engineering models.

## 常见错误 / Common mistakes

| 现象 | 原因 | 修正 / Fix |
|---|---|---|
| `puts {Hello $name}` 没显示姓名 | 花括号阻止这一层变量替换 | 需要替换时写 `puts "Hello $name"`。 / Use quotes when substitution is intended. |
| `invalid command name "Hello"` | 将文本写在 `[Hello]` 中，要求执行它 | 纯文本使用引号或花括号。 / Brackets execute commands. |
| 算出 `5 / 2 = 2` | 两个操作数是整数 | 需要 2.5 时用 `expr {5 / 2.0}`。 / Introduce a floating-point operand. |
| `08` 不能按想象做整数运算 | Tcl 兼容的整数语法会解释前导 0 | 十进制输入先按规则验证，再用 `scan $text %d`；不要猜测字符串格式。 / Parse decimal text intentionally. |
| 一个姓名被拆成两个人 | 用 `split` 或手工拼接代替 `list` | 用 `[list "Lin Wei" Mei]` 构造。 / Preserve element boundaries. |
| 数值排序是 `1 10 2` | 使用默认字符串排序 | 整数用 `lsort -integer`，测量值用 `-real`。 / Select numeric sorting. |
| `can't read "total"` | 变量尚未设置，或过程作用域里不可见 | 初始化局部变量；明确决定传参、`global` 或 `variable`。 / Pass data or link scope explicitly. |
| `puts $device` 读不到数组 | 数组不是标量值 | 使用 `$device(key)`，或用 `array get device` 获取键值列表。 / Access an element or serialize pairs. |
| 正则中的 `[]` 被执行 | 模式放在双引号中触发命令替换 | 通常使用花括号模式：`regexp {[0-9]+} $text`。 / Brace literal regex patterns. |
| 空行之后读取中断 | `gets` 返回 0，被误当作失败 | 判断返回值 `>= 0`。 / Test for end-of-file using a negative result. |
| `catch` 后输出“成功” | 没有检查返回码或把错误吞掉 | 根据返回码显示错误信息，成功路径单独处理。 / Check completion status. |
| 文件找不到 | 相对路径基于当前工作目录 | 本地查看 `pwd`；浏览器检查虚拟文件列表；必要时 `file join` 构造路径。 / Check the working directory. |
| `get_cells` 不存在 | 它通常由特定 EDA 宿主提供 | 使用课程教学模型，或在对应真实工具中运行其官方命令。 / Verify host capabilities. |
| 更改输入但图解没变 | 看的是静态教材示意 | 运行代码后查看明确标注的实际结果视图。 / Distinguish the diagram from runtime results. |

## 实用的文件模式 / A file pattern

下面是本仓库的原创小例子。浏览器中先提供虚拟 `notes.txt`，本地则在练习目录建立同名 UTF-8 文件。

```tcl
set channel [open notes.txt r]
fconfigure $channel -encoding utf-8
try {
    set text [read $channel]
} finally {
    close $channel
}
puts [string length $text]
```

`try/finally` 保证成功打开的通道在读取失败时也关闭；`source` 是执行脚本，不是读取普通文本。配置文件也属于代码。Use `read` for text data; use `source` only for trusted scripts. [try](https://www.tcl-lang.org/man/tcl8.6/TclCmd/try.htm), [source](https://www.tcl-lang.org/man/tcl8.6/TclCmd/source.htm)

## 官方参考资料 / Official references

以下是语义核对入口，不需要从头背诵。遇到一个命令，先看其 Synopsis、选项和返回值，再用自己的小输入验证。课程和项目的文字、图解与教学数据均独立编写，官方手册仅用于核对语言行为。

| 资料 | 适用内容 / Use |
|---|---|
| [Tcl 8.6 命令目录](https://www.tcl-lang.org/man/tcl8.6/TclCmd/contents.htm) | 选择与课程目标版本一致的命令。 / Find commands for the target version. |
| [Tcl 语法](https://www.tcl-lang.org/man/tcl8.6/TclCmd/Tcl.htm) | 分词、命令结束、替换与注释。 / Parsing and substitution rules. |
| [expr](https://www.tcl-lang.org/man/tcl8.6/TclCmd/expr.htm) | 运算符、数值格式、短路求值。 / Numeric and string expressions. |
| [list](https://www.tcl-lang.org/man/tcl8.6/TclCmd/list.htm)、[lsort](https://www.tcl-lang.org/man/tcl8.6/TclCmd/lsort.htm) | 可靠列表构造及排序模式。 / List construction and sorting. |
| [string](https://www.tcl-lang.org/man/tcl8.6/TclCmd/string.htm)、[split](https://www.tcl-lang.org/man/tcl8.6/TclCmd/split.htm) | 文本清理、数值检查和分隔字符规则。 / String handling and validation. |
| [dict](https://www.tcl-lang.org/man/tcl8.6/TclCmd/dict.htm)、[array](https://www.tcl-lang.org/man/tcl8.6/TclCmd/array.htm) | 两种数据组织方式与访问方法。 / Dictionary values versus array variables. |
| [regexp](https://www.tcl-lang.org/man/tcl8.6/TclCmd/regexp.htm)、[正则语法](https://www.tcl-lang.org/man/tcl8.6/TclCmd/re_syntax.htm) | 捕获组、匹配选项和模式语义。 / Regex matching and syntax. |
| [proc](https://www.tcl-lang.org/man/tcl8.6/TclCmd/proc.htm)、[namespace](https://www.tcl-lang.org/man/tcl8.6/TclCmd/namespace.htm) | 参数、局部作用域和命名空间。 / Procedures and scope. |
| [open](https://www.tcl-lang.org/man/tcl8.6/TclCmd/open.htm)、[gets](https://www.tcl-lang.org/man/tcl8.6/TclCmd/gets.htm)、[close](https://www.tcl-lang.org/man/tcl8.6/TclCmd/close.htm) | 文件模式、逐行读取和通道关闭。 / File channels. |
| [catch](https://www.tcl-lang.org/man/tcl8.6/TclCmd/catch.htm)、[try](https://www.tcl-lang.org/man/tcl8.6/TclCmd/try.htm) | 完成码、错误选项与清理。 / Errors and cleanup. |
| [source](https://www.tcl-lang.org/man/tcl8.6/TclCmd/source.htm)、[全局参数变量](https://www.tcl-lang.org/man/tcl8.6/TclCmd/tclvars.htm) | 脚本加载、argv 与版本信息。 / Loading scripts and reading process arguments. |
| [oo::class](https://www.tcl-lang.org/man/tcl8.6/TclCmd/class.htm)、[oo::define](https://www.tcl-lang.org/man/tcl8.6/TclCmd/define.htm) | TclOO 类、构造器和方法。 / Introductory object-oriented Tcl. |

官方站点的文档内容可能更新；本课程运行版本以实际检测为准。真实 EDA 工具使用其供应商的版本化资料，不能从本课程教学函数名推断工具接口。Official documentation and the course runtime may use different patch releases; check the measured interpreter version. Consult version-specific vendor documentation for actual EDA commands.

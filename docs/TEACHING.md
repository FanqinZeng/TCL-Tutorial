# 学习指南 / Learning guide

Tcl 自动化工作坊把重复、琐碎的整理工作变成可复用的小脚本。从写通知和算费用开始，逐步处理文本、文件、日志，最后分析原创教学版 VLSI 报告。主课默认使用简体中文；本指南提供完整英文学习说明与全部课程概要。

无需账号，也无需购买 EDA 软件。每节课都可以单独进入；学习路线是建议，不是解锁条件。在线练习的代码交给真实 Tcl 解释器，教材图解则是静态知识示意。结果视图只说明实际执行结果，不能代替逐步调试。

## 开始前

1. 打开[网站首页](../site/index.html)，运行迷你示例。在线运行需要通过 HTTP 服务打开网站，不能只双击 HTML 文件；启动方法见[项目说明](../README.md)。
2. 确认页面显示的运行状态与 Tcl 版本。解释器加载期间可以先阅读、复制示例；错误或超时应按提示处理。
3. 准备一个本地练习目录。如果使用 `tclsh`，运行 `puts [info patchlevel]` 查看版本。课程面向 Tcl 8.6 及以上，版本和运行时限制见仓库说明。
4. 第一次做文件课前，先读懂虚拟文件与真实文件的区别：浏览器内的文件随每次运行创建，不能访问你电脑的私人目录；本地 `tclsh` 的 `open` 和 `source` 则操作真实文件。

## 三条推荐路线

| 你的起点 | 建议顺序 | 每一段的练习作品 |
|---|---|---|
| 完全零基础 | 01–03 → 04–06 → 07–09 → 10–12 → 13–15 → 16–18 | 通知、购物计算、名单 A、开支 B、测量 C、日志 D、路径 E、流程 F |
| 有其他编程语言基础 | 精读 03、06、08、10；快速跑 01–02、04–05、07、09；再学 11–15 → 16–18 | 重点比较替换规则、列表构造、dict/array、作用域；完成 C、D、F |
| 只想学习 VLSI 应用 | 必备 02–03、04–06、08–12、14 → 16–18；需要组织工具时补 13，需要对象状态时补 15 | 先做 E，再做 F；随后查真实 EDA 工具的官方命令资料 |

零基础学习者可按每次一节课安排；短例子先运行，练习在下一次学习前重做。不要为赶进度只抄答案。会写其他语言的学习者尤其要停下来比较 Tcl 的命令、替换和列表语义，避免直接套用另一门语言的写法。

## 每节课怎么学

1. **先预测。**读问题与输入，在运行前写下你认为的结果。错误预测能帮你找到需要解释的规则。
2. **运行并对照。**先运行一个原样例子，比较实际输出与预期；阅读图解了解关系，再看工作台里的实际结果。
3. **只改一个条件。**替换一个姓名、预算、循环上限或数据值。解释哪部分结果改变，哪部分保持不变。
4. **从起始代码做练习。**默认折叠提示和答案，卡住时先开第一层提示，再开第二层。
5. **检查多个输入。**通过样例还不够；空输入、坏数据、边界值与另一组正常数据都能揭示写死输出的问题。
6. **记录自己的规则。**手动标记已读，保存一两句说明；学习记录保存在当前浏览器，可导出备份。导入时使用网站导出的格式；清空记录会要求确认。

编辑器支持多行代码，界面会显示运行快捷键。Tab 的输入行为和离开编辑器的方式以界面提示为准；不要在不熟悉的状态下反复按运行。遇到无限循环可使用停止按钮；修复循环条件后再试。

## 18 节课概要

| 单元 | 课 | 问题与要点 | 能独立做出的东西 |
|---|---|---|---|
| 一：第一次让电脑帮忙 | [01 输出与脚本](../lessons/01/README.md) | 通知如何生成；`puts`、注释、命令与参数 | 一张内容明确的活动通知 |
| 一 | [02 变量与计算](../lessons/02/README.md) | 购物总价如何随数量改变；`set`、`expr`、`incr` | 可修改数量和单价的计算脚本 |
| 一 | [03 Tcl 的三种重要符号](../lessons/03/README.md) | 消息中的姓名和结果如何替换；`""`、`{}`、`[]` | 准确控制替换的消息模板 |
| 二：选择与重复 | [04 条件判断](../lessons/04/README.md) | 根据预算选择方案；数值比较与 `eq/ne` | 有清楚分支的预算判断 |
| 二 | [05 重复处理](../lessons/05/README.md) | 批量测量如何累计；`foreach`、`for`、`while` | 会跳过坏项与及时停止的循环 |
| 二 | [06 列表](../lessons/06/README.md) | 姓名中的空格如何保留；列表构造、索引、搜索、排序 | 保持元素边界的报名名单 |
| 三：文本与结构化数据 | [07 字符串处理](../lessons/07/README.md) | 联系人文本如何统一；大小写、修剪、`split/join` | 清理前后可核对的文本结果 |
| 三 | [08 字典与数组](../lessons/08/README.md) | 设备记录如何按字段读取；`dict` 与 `array` | 字段和值清晰对应的记录 |
| 三 | [09 正则表达式入门](../lessons/09/README.md) | 日志中时间与状态如何提取；捕获组 | 能解释规则的短解析器 |
| 四：复用脚本 | [10 过程与参数](../lessons/10/README.md) | 费用计算如何复用；`proc`、默认参数、返回值 | 可接收不同输入的计算工具 |
| 四 | [11 文件读写](../lessons/11/README.md) | 实验数据如何读入并写摘要；文件通道 | 能关闭通道的文件报告 |
| 四 | [12 错误处理与调试](../lessons/12/README.md) | 文件缺失、非法输入如何报告；`catch`、`error` | 正常与错误路径都能解释的脚本 |
| 五：组织项目 | [13 作用域与命名空间](../lessons/13/README.md) | 同名变量如何隔离；`global`、`variable`、`namespace` | 相互不干扰的工具集合 |
| 五 | [14 脚本组织与参数](../lessons/14/README.md) | 怎样从入口加载配置与工具；`source`、`argc/argv` | 参数可改变行为的报告入口 |
| 五 | [15 TclOO 入门](../lessons/15/README.md) | 测量仪器如何保存状态；类、对象、方法、销毁 | 状态明确的简单测量对象 |
| 六：VLSI 应用 | [16 Tcl 与 EDA 工具](../lessons/16/README.md) | 语言命令与工具命令怎样区分；教学对象筛选 | 可识别适配边界的筛选模型 |
| 六 | [17 约束与报告](../lessons/17/README.md) | 周期、延迟与 slack 如何关联；报告筛选 | 标注假设的教学路径分析 |
| 六 | [18 自动生成分析摘要](../lessons/18/README.md) | 多份输入怎样变成一份摘要；解析、统计、错误报告 | 可复用的分析流程 |

上表链接指向生成的 Markdown 讲义；可运行练习在网站中完成。文件、练习和答案由构建脚本从同一 JSON 内容源生成。

## 六个独立项目

| 项目 | 适合完成后尝试 | 你需要决定和验证的规则 |
|---|---|---|
| [A 报名名单清理器](../projects/A/README.md) | 06、07、10 | 姓名空白、大小写、去重与排序；空名单和非法列表 |
| [B 家庭开支摘要](../projects/B/README.md) | 08、10、12 | 用整数分保存金额；拒绝缺字段、负数、非整数金额 |
| [C 实验测量数据统计](../projects/C/README.md) | 05、08、10、12 | 闭区间、有限数值、空数据、浮点平均数与极端值 |
| [D 日志诊断助手](../projects/D/README.md) | 07、09、10、12 | 原始行号、级别计数、非法时间、重叠上下文 |
| [E 设计路径报告筛选器](../projects/E/README.md) | 11、16、17 | 有限数值、负 slack、严重程度排序、教学模型限制 |
| [F 可配置的报告生成流程](../projects/F/README.md) | 11–14、18 | 受信任配置、文件关闭、改变阈值、摘要与错误分流 |

项目可与主课交替完成。先写需求对应的过程，再写输出过程；这样验证可以用不同输入调用算法，而不是只看第一次输出。项目 F 的配置和工具属于可执行 Tcl 代码，只加载你知道来源的文件。

## 错误出现时

先读第一条错误信息，找它提到的命令或变量。把问题缩小到能重现的两三行，再比较你的输入和需求规则。`can't read` 常与作用域或变量名有关；`invalid command name` 常与误写方括号或不存在的工具命令有关；列表错误常来自手工拼接。完整速查见[参考与常见错误](REFERENCE.md)。

网站中出错时，先看真实错误区；示意图依然是教材，不表示程序已经成功。读取文件失败要核对当前虚拟文件列表或本地 `pwd`，不要随意改成你电脑上其他人的绝对路径。

---

# English learning guide

Tcl Everyday Workshop teaches small, useful automation tasks: create a notice, calculate costs, clean names, summarize measurements, inspect logs, and analyze original educational VLSI reports. The full lesson text is in Simplified Chinese. This guide and the course overview below provide a complete English orientation; there is no claim that lesson bodies have been translated.

No account or commercial EDA installation is required. Every lesson is available independently. The online editor sends your code to a real Tcl interpreter. Static diagrams explain concepts; a result view displays actual execution data and should not be confused with a step-by-step debugger.

## Getting started

1. Open the [website](../site/index.html) through an HTTP server and run the small example. See the [English README](../README.en.md) for the local preview command. Opening an HTML file directly is not the supported runtime setup.
2. Read the interpreter status and the version shown by the page. While it loads, you can read the material or copy the code. Treat errors and timeouts as results to investigate.
3. For local work, create a dedicated practice directory. In `tclsh`, run `puts [info patchlevel]` to check the interpreter. Course code targets Tcl 8.6 or later; the repository documents the exact versions used for validation.
4. Before the file lesson, distinguish the browser's virtual files from real disk files. Browser runs create their own working files and cannot browse your private computer directories. Local `tclsh` file commands work with actual files in the current working directory.

## Choose a route

| Starting point | Recommended order | Focus and practice |
|---|---|---|
| New to programming | 01–03 → 04–06 → 07–09 → 10–12 → 13–15 → 16–18 | Build small notices and calculations first. Alternate the course with projects A–F as the required skills become available. |
| Experienced in another language | Study 03, 06, 08 and 10 carefully; run 01–02, 04–05, 07 and 09 quickly; continue with 11–15 → 16–18 | Compare Tcl substitution, list construction, dictionaries versus arrays, return values and scope. Complete C, D and F. |
| Focused on VLSI scripting | Learn 02–03, 04–06, 08–12 and 14 → 16–18; add 13 for organizing tools and 15 when persistent object state is useful | Complete E and F, then consult the official command documentation for the actual EDA tool you use. |

Routes are suggestions, not prerequisites enforced by the website. A beginner can work through one lesson per study session and redo an exercise before the next session. An experienced programmer should resist translating familiar syntax directly into Tcl; the rules for commands, substitution and list boundaries deserve deliberate practice.

## A useful study cycle

1. **Predict first.** Read the problem and input. Write down the output you expect before running the example.
2. **Run and compare.** Run the original example once. Compare actual and expected output, then use the diagram to explain the relationship between the input and result.
3. **Change one thing.** Modify a name, price, loop limit or data value. Explain exactly which result should change.
4. **Use the starter.** Attempt the exercise before opening its folded hints or reference solution. Reveal hints one at a time.
5. **Check varied inputs.** A sample alone is insufficient. Test another ordinary input, an empty input, an invalid input and a boundary value. This helps distinguish reusable code from a printed answer.
6. **Keep a short note.** Mark the lesson read when appropriate and record the rule you learned. Browser-local progress can be exported as a backup; import the website's supported format. Clearing records requires confirmation.

The editor supports multiple lines and displays its keyboard run shortcut. Follow its help text for Tab behavior and leaving the editor with the keyboard. Stop a loop that does not finish, fix its termination condition, and run it again.

## Complete course overview

| Unit | Lesson | Problem, concepts and learning outcome |
|---|---|---|
| 1. Let the computer help | [01 Output and scripts](../lessons/01/README.md) | Generate an event notice. Learn `puts`, comments, command words and arguments; write a readable first script. |
| 1 | [02 Variables and calculations](../lessons/02/README.md) | Calculate a shopping total. Use `set`, variable substitution, braced `expr` and `incr`; update the result by changing data. |
| 1 | [03 Three important Tcl symbols](../lessons/03/README.md) | Construct a message with a name and calculated result. Distinguish double quotes, braces and brackets; predict where substitution occurs. |
| 2. Choices and repetition | [04 Conditions](../lessons/04/README.md) | Choose a shopping plan within a budget. Use `if/elseif/else`, numeric comparisons and string `eq/ne`. |
| 2 | [05 Repeated processing](../lessons/05/README.md) | Process measurement rows. Begin with `foreach`, compare `for/while`, and use `break/continue` deliberately. |
| 2 | [06 Lists](../lessons/06/README.md) | Organize registrations while keeping full names intact. Construct, index, append, slice, search and sort Tcl lists. |
| 3. Text and structured data | [07 Strings](../lessons/07/README.md) | Normalize inconsistent contact text. Use trimming, case conversion, matching, `split` and `join`. |
| 3 | [08 Dictionaries and arrays](../lessons/08/README.md) | Manage a device or sample record. Access fields, test their existence, and explain why a dictionary value differs from an array variable. |
| 3 | [09 Regular expressions](../lessons/09/README.md) | Extract a time, status or value from a log. Use short patterns and capture groups; compare with a non-regex approach. |
| 4. Reusable scripts | [10 Procedures and parameters](../lessons/10/README.md) | Reuse a cost calculation with different inputs. Define `proc`, default parameters, local variables and return values. |
| 4 | [11 Files](../lessons/11/README.md) | Read experiment data and create a summary. Open, read, write and close channels; distinguish virtual files from local files. |
| 4 | [12 Errors and debugging](../lessons/12/README.md) | Explain missing files, invalid input and division errors. Use `catch/error` without hiding failures. |
| 5. Organizing a project | [13 Scope and namespaces](../lessons/13/README.md) | Combine tools without accidental variable collisions. Introduce local scope, `global`, `variable` and `namespace`. |
| 5 | [14 Script organization and arguments](../lessons/14/README.md) | Load a trusted configuration and helper script. Use `source`, `argc/argv` and explicit online argument fixtures. |
| 5 | [15 Introduction to TclOO](../lessons/15/README.md) | Model a measuring instrument with state. Create a class and an instance, use a constructor and methods, and destroy the instance. |
| 6. VLSI applications | [16 Tcl and EDA tools](../lessons/16/README.md) | Filter objects in an original teaching model. Separate Tcl language commands from commands supplied by an EDA application. |
| 6 | [17 Constraints and reports](../lessons/17/README.md) | Relate a clock period, delay and slack in a simplified model. Parse and filter an educational path report while stating its assumptions. |
| 6 | [18 Automated analysis summary](../lessons/18/README.md) | Combine several reports into one readable summary. Integrate parsing, files, dictionaries, procedures and error handling. |

These links open generated Markdown teaching material. Use the website for runnable exercises. Teaching files, starters and solutions come from the same canonical JSON sources, keeping the learning material and its validation cases together.

## Independent projects

| Project | Useful preparation | What your implementation must handle |
|---|---|---|
| [A Registration cleaner](../projects/A/README.md) | Lessons 06, 07, 10 | Full names with spaces, duplicate entries, explicit case rules, ordering, empty and malformed lists. |
| [B Household expense summary](../projects/B/README.md) | Lessons 08, 10, 12 | Integer cents, grouping, missing fields, negative and non-integer amounts, separate rejection reasons. |
| [C Measurement statistics](../projects/C/README.md) | Lessons 05, 08, 10, 12 | Closed interval limits, finite numbers, empty inputs, a non-integer mean and extreme values. |
| [D Log diagnosis assistant](../projects/D/README.md) | Lessons 07, 09, 10, 12 | Original line numbers, valid times, level counts, malformed lines and overlapping context windows. |
| [E Design path report filter](../projects/E/README.md) | Lessons 11, 16, 17 | Finite numeric fields, negative slack, severity ordering and clear educational-model limits. |
| [F Configurable report pipeline](../projects/F/README.md) | Lessons 11–14, 18 | Trusted executable configuration, changed thresholds, channel cleanup, summary files and error files. |

Start with a procedure that returns structured results, then add a reporting procedure. Tests can then call the algorithm with new inputs instead of accepting one printed sample. Project F configurations are executable Tcl scripts; load only files whose source you trust.

## When something fails

Read the first error message and find the command or variable it names. Reduce the problem to a few lines that still reproduce it. A `can't read` message often points to a missing variable or scope issue; `invalid command name` can result from accidental bracket execution or an unavailable tool command. Manually joined names can create list errors. Use the [reference and common mistakes](REFERENCE.md) to diagnose the rule involved.

A static teaching diagram does not certify that your program succeeded. After a runtime error, use the error panel before interpreting a result. For missing files, inspect the virtual-file fixtures or the local `pwd` value and current directory.

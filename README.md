# Tcl 自动化工作坊 · Tcl Everyday Workshop

[English](README.en.md) · [完整学习指南](docs/TEACHING.md) · [速查与常见错误](docs/REFERENCE.md)

用一小段 Tcl，解决一个看得懂的数据问题。原创任务驱动课程：**6 个单元、18 节完整主课、54 道练习、6 个综合项目**。教学网站包含真实 Tcl 在线实验室、数据结果视图和六段演示；不使用游戏闯关体系。

**仓库：** [FanqinZeng/TCL-Tutorial](https://github.com/FanqinZeng/TCL-Tutorial)

**GitHub Pages 目标地址：** [fanqinzeng.github.io/TCL-Tutorial/](https://fanqinzeng.github.io/TCL-Tutorial/)（自动部署状态以仓库 Actions 与实际访问结果为准）。

## 适合谁

- 零基础：按 01–18 顺序，预测输出 → 运行 → 改一处 → 解释结果。
- 有其他语言基础：重点读 03、06、08、10–15，掌握 Tcl 替换、列表、作用域与 TclOO。
- VLSI 学习者：复习列表、字典、过程与文件，再学习 16–18 和项目 E/F。商业 EDA 工具命令与教学模型明确区分。

## 课程与综合项目

| 单元 | 课程 |
| --- | --- |
| 1 · 第一次让电脑帮忙 | 01 输出与脚本 · 02 变量与计算 · 03 三种重要符号 |
| 2 · 选择与重复 | 04 条件 · 05 循环 · 06 列表 |
| 3 · 文本与结构化数据 | 07 字符串 · 08 字典与数组 · 09 正则 |
| 4 · 可复用脚本 | 10 过程 · 11 文件 · 12 错误处理 |
| 5 · 组织项目 | 13 作用域 · 14 模块与参数 · 15 TclOO |
| 6 · VLSI 应用 | 16 Tcl 与 EDA · 17 教学约束与报告 · 18 分析摘要 |

每节课实际包含：原创 SVG、3 个带预期输出的例子、3 道练习、折叠提示与答案、至少 2 道理解题、常见错误、探索活动和速查。

项目 A–F：名单清理、家庭开支汇总、测量统计、日志诊断、教学路径筛选、可配置报告流水线。每个项目都有参考实现以及不同输入、空输入、非法输入等验证。

## 本地网站与 Tcl

```sh
git clone https://github.com/FanqinZeng/TCL-Tutorial.git
cd TCL-Tutorial
python3 scripts/serve.py
# 打开 http://127.0.0.1:8765/
```

网页不需要安装 Tcl、Node 或 npm 包，不依赖外部 CDN。请通过 HTTP 打开，不能双击 `site/index.html`。

本地 Tcl 练习需要 **Tcl 8.6+**。Ubuntu/Debian 可用 `sudo apt-get install tcl`；其他平台从 [Tcl 官方软件页](https://www.tcl-lang.org/software/tcltk/)选择发行版。Mac 系统 Tcl 8.5 不支持本课 TclOO。

```sh
tclsh examples/01/01.tcl
python3 scripts/check.py --all
python3 scripts/check.py --lesson 10 --exercise 1 solutions/10/01.tcl
```

有文件夹/参数的示例应带上 `data/` 中相应的输入，或使用验证器在临时目录运行。文件写入当前工作目录，请使用独立练习目录。本网站的文件仅存在于浏览器内存中，每次运行重新创建。

## 结构与维护

```text
lessons/*.json       原创课程单一来源
projects/*.json      项目单一来源
lessons/NN/          生成的 Markdown 讲义
examples/            生成的可独立运行 Tcl 例子
exercises/           生成的起始代码
solutions/           生成的参考答案
data/                原创输入文件
site/                无打包依赖的静态网站、WASM 运行时与媒体
docs/                教学、运行、部署、无障碍及维护说明
scripts/             内容生成、原生验证、预览和视频制作
tests/               真实 WASM、内容完整性与验证结果
.github/workflows/   自动检查与 GitHub Pages 部署
```

```sh
python3 scripts/build.py
python3 scripts/check.py --all
python3 tests/integrity.py
node tests/runtime.mjs
```

Node 18+ 只用于开发测试，不用于网站访问。详见 [贡献方式](CONTRIBUTING.md)、[部署](docs/DEPLOYMENT.md)、[运行原理](docs/RUNTIME.md)。

## 边界与许可

浏览器真实解释器为 Wacl 随附 **Tcl 8.6.6**，不是最新 Tcl；本地建议 8.6+，也验证 Tcl 9.0.4。每次运行独立 Worker，执行超过 5 秒可终止。没有账号、私人后端、遥测或排行榜。代码草稿和阅读记录留在当前浏览器，可导出/导入。

时序、设计对象和 EDA 操作是原创教学模型；没有商业 EDA 连接、真实 STA、Calibre 或 GDS 生成。教学报告格式不能直接替代厂商报告解析器。

原创代码、讲义与 SVG 使用 [MIT](LICENSE)。第三方运行时保留各自许可证，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。语言规则参考 [Tcl 官方手册](https://www.tcl-lang.org/man/tcl8.6/TclCmd/contents.htm)，课程、题目、数据和页面结构独立设计。

验证详情与实际页面截图：[QA](docs/QA.md)。

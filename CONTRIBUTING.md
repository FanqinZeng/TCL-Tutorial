# 修正与贡献

课程源是 `lessons/*.json` 和 `projects/*.json`；不要直接编辑生成的讲义、练习或网站 JSON。数据结构见 `docs/CONTENT_SCHEMA.md`。

1. 先复现学习者遇到的问题，用最小 Tcl 示例说明。
2. 修改源 JSON；保持至少 3 个例子、3 个练习、2 道理解题、2 个错误说明与完整提示。
3. 原创图解放在 `site/assets/diagrams/`，提供 SVG title/desc，不加载远程图片。
4. `python3 scripts/build.py`；`python3 scripts/check.py --all`；`python3 tests/integrity.py`；`node tests/runtime.mjs`。
5. 实际查看桌面和手机宽度；修改运行时后额外验证错误、中文、无限循环和虚拟文件隔离。
6. 提交具体问题、修改行为和实际验证结果。不要复制未授权的讲义、厂商文档或私有数据。

Tcl 8.6 是课程的最低版本。请同时考虑浏览器的固定 8.6.6 与当前 native Tcl。行为检查要调用新输入、空输入或非法输入，不要用源码关键词判断答案。

# GitHub Pages 部署

现有仓库 `FanqinZeng/TCL-Tutorial` 为公开仓库；保留其可见性。网站产物位于 `site/`，只发布静态文件。

仓库 Settings → Pages → Build and deployment → Source 选择 **GitHub Actions**。`.github/workflows/pages.yml` 在 main 提交时验证课程、原生 Tcl 和真实 WASM，随后上传 Pages 产物并部署。

目标地址由仓库推导：https://fanqinzeng.github.io/TCL-Tutorial/ 。只有 Actions deploy 成功和页面实际返回成功才表示部署完成；README 中目标地址不表示部署已成功。

所有应用链接使用 hash 路由，资源从相对路径加载，因此项目子路径和刷新都可工作。`build.py` 为入口 CSS/JS 与课程 JSON 使用内容版本；每个部署必须同时更新 HTML、脚本、JSON 和资源。

本地预览：`python3 scripts/serve.py`，打开 http://127.0.0.1:8765/ 。不要通过 file:// 打开。

若未来改为私有仓库，先核实账号套餐的私有 Pages 支持；不要为部署擅自改为公开。无需 API key、商业服务或私人后端。

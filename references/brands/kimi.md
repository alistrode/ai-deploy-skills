# 月之暗面 / Kimi

助手、办公、编程、浏览器和模型

先介绍业务线，再按用户选择执行对应产品卡。所有入口是官方资料起点，操作时重新核对当日状态。

| 产品 | 适用用途 | 支持路线 |
|---|---|---|
| Kimi | 问答、文档与 Agent 工作台 | WEB / APP |
| Kimi Work | 桌面办公与跨网页任务 | APP |
| Kimi Code | CLI、桌面和 VS Code 编程 | CLI / APP / EXT |
| Kimi 浏览器扩展 | 网页读取与交互 | EXT |
| Kimi Office | WPS 文档、表格和演示文稿 | EXT |
| Kimi Research / Slides / Docs / Sheets / Build / Agent Swarm | 研究、PPT、文档、表格、建站与协同任务 | WEB / APP |
| Kimi / Moonshot 开放平台 | 模型 API | API |
| Kimi 开放模型 | 本地推理与研究 | LOCAL |

## Kimi (`kimi`)

- 官方入口：https://www.kimi.com/
- 操作文档：https://www.kimi.com/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：从官网进入账户；选择对话或文档任务；需要客户端从官方产品页下载安装。
- 可用标准：回复或文档任务实际成功。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Kimi Work (`kimi-work`)

- 官方入口：https://www.kimi.com/products/
- 操作文档：https://www.kimi.com/products/
- 路线：APP；读取 `../recipes.md` 对应步骤。
- 执行：进入 Work 官方下载和指南；匹配系统，登录；只授权样例目录，完成一份简短汇总。
- 可用标准：本地/云端产物可打开并明确运行位置。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Kimi Code (`kimi-code`)

- 官方入口：https://www.kimi.com/code/docs/en/
- 操作文档：https://www.kimi.com/code/docs/en/kimi-code-cli/guides/getting-started
- 路线：CLI / APP / EXT；读取 `../recipes.md` 对应步骤。
- 执行：先读当前快速入门；编写时官方 CLI 已转为 Node.js 体系，不能照旧 Python/uv 安装；选择当前官方安装方式，登录并运行临时项目。
- 可用标准：实际任务成功，CLI/扩展/桌面按选定形态分别验收。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Kimi 浏览器扩展 (`kimi-browser`)

- 官方入口：https://www.kimi.com/products/
- 操作文档：https://www.kimi.com/products/
- 路线：EXT；读取 `../recipes.md` 对应步骤。
- 执行：沿产品页进入浏览器扩展；核对发行者，安装启用；在公开页面执行归纳任务。
- 可用标准：扩展能读取当前页面并返回相关结果。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Kimi Office (`kimi-office`)

- 官方入口：https://www.kimi.com/products/
- 操作文档：https://www.kimi.com/products/
- 路线：EXT；读取 `../recipes.md` 对应步骤。
- 执行：按官方 Office/WPS 扩展指南安装；登录，创建临时文档/表格，运行一个编辑任务。
- 可用标准：WPS 内出现可编辑结果；宿主版本满足要求。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Kimi Research / Slides / Docs / Sheets / Build / Agent Swarm (`kimi-features`)

- 官方入口：https://www.kimi.com/products/
- 操作文档：https://www.kimi.com/products/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：按所选功能创建独立样例：研究查来源、PPT 生成三页、表格计算三行虚构数据、Build 生成简单页面并预览；集群用最小任务。
- 可用标准：验收所选专项产物，网站只预览不自动公开。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Kimi / Moonshot 开放平台 (`kimi-platform`)

- 官方入口：https://platform.kimi.com/
- 操作文档：https://platform.kimi.com/
- 路线：API；读取 `../recipes.md` 对应步骤。
- 执行：沿产品页确认当前平台域名与地区；区分普通 API、Kimi Code 订阅接口；从当前文档读取模型及端点。
- 可用标准：普通 API 或受支持编码工具任务真正成功，不混用套餐。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Kimi 开放模型 (`kimi-models`)

- 官方入口：https://huggingface.co/moonshotai
- 操作文档：https://huggingface.co/moonshotai
- 路线：LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：选择官方已开放版本；按许可证、架构、内存判断本机是否适配；用模型卡支持的引擎部署。
- 可用标准：本地真实推理；完整大模型不适配时说明所需资源，别假称 CPU 能流畅运行。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

# Anthropic / Claude

对话、编程、办公代理与模型 API

先介绍业务线，再按用户选择执行对应产品卡。所有入口是官方资料起点，操作时重新核对当日状态。

| 产品 | 适用用途 | 支持路线 |
|---|---|---|
| Claude | 聊天、写作、文档研究与 Artifacts | WEB / APP |
| Claude Code | 编程代理 | CLI / APP / EXT |
| Claude Cowork | 文件与跨应用办公代理 | APP / WEB |
| Claude in Chrome | 浏览器交互 | EXT |
| Claude 办公集成 | Office 等宿主内文档与表格辅助 | EXT |
| Claude Platform / Managed Agents | 模型和托管 Agent API | API / WEB |
| Opus / Sonnet / Haiku | 能力、均衡、速度成本分层 | API / WEB |

## Claude (`claude`)

- 官方入口：https://claude.ai/
- 操作文档：https://claude.com/download
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：官方登录，选择对话/研究/Artifacts；必要时从官方下载桌面或手机端；使用无敏感样例。
- 可用标准：得到真实回复或可打开产物。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Claude Code (`claude-code`)

- 官方入口：https://code.claude.com/docs/en/overview
- 操作文档：https://github.com/anthropics/claude-code
- 路线：CLI / APP / EXT；读取 `../recipes.md` 对应步骤。
- 执行：按当前官方安装方式安装；确认 PATH/版本；官方账户或指定供应商登录；临时项目执行只读代码分析。
- 可用标准：实际任务返回，明确是 Anthropic 模型还是用户选择的第三方模型。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Claude Cowork (`cowork`)

- 官方入口：https://claude.com/resources/guides/claude-cowork-product-guide/product-overview
- 操作文档：https://claude.com/resources/guides/claude-cowork-product-guide/product-overview
- 路线：APP / WEB；读取 `../recipes.md` 对应步骤。
- 执行：在当前支持客户端/运行模式中进入 Cowork，授权一个临时目录；整理两份无隐私样例文档并生成汇总。
- 可用标准：汇总文件可打开，目录授权范围清楚。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Claude in Chrome (`claude-chrome`)

- 官方入口：https://claude.com/
- 操作文档：https://claude.com/
- 路线：EXT；读取 `../recipes.md` 对应步骤。
- 执行：从官方产品/帮助中心进入扩展市场；核对 Anthropic 发行者；启用，登录，对公开页面做总结。
- 可用标准：当前页面内容被正确读取；外部动作不默认授权。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Claude 办公集成 (`claude-office`)

- 官方入口：https://claude.com/
- 操作文档：https://claude.com/
- 路线：EXT；读取 `../recipes.md` 对应步骤。
- 执行：从官方集成页查当前支持的宿主和套餐；安装官方加载项；用新的测试文档执行摘要或表格任务。
- 可用标准：宿主内出现可编辑结果；没有授权不扫描全部网盘。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Claude Platform / Managed Agents (`claude-platform`)

- 官方入口：https://platform.claude.com/
- 操作文档：https://docs.anthropic.com/
- 路线：API / WEB；读取 `../recipes.md` 对应步骤。
- 执行：阅读当前 API 文档；创建正确组织/工作区下密钥；区分 Messages 与其他接口；托管 Agent 采用专用快速入门。
- 可用标准：实际模型返回或托管任务完成，保存可复用配置。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Opus / Sonnet / Haiku (`claude-models`)

- 官方入口：https://platform.claude.com/docs/en/about-claude/models/overview
- 操作文档：https://platform.claude.com/docs/en/about-claude/models/overview
- 路线：API / WEB；读取 `../recipes.md` 对应步骤。
- 执行：从当前目录选确切模型 ID；按预算、上下文及能力选择；在应用或 API 内执行样例。
- 可用标准：确认实际模型可访问；不凭系列名假定所有套餐都有。
- 特别说明：闭源托管模型不走本地权重部署。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

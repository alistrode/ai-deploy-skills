# DeepSeek

聊天、Harness、API 与开放模型

先介绍业务线，再按用户选择执行对应产品卡。所有入口是官方资料起点，操作时重新核对当日状态。

| 产品 | 适用用途 | 支持路线 |
|---|---|---|
| DeepSeek 网页与 App | 大众问答、推理和编程 | WEB / APP |
| DeepSeek Harness | 可扩展 Agent 框架与桌面环境 | APP / LOCAL |
| DeepSeek API | 模型开发接入 | API |
| DeepSeek 通用、推理与蒸馏开放模型 | 本地语言与推理 | LOCAL / API |
| DeepSeek-Coder / Math / VL / Janus 等研究模型 | 代码、数学、视觉与图像研究 | LOCAL |

## DeepSeek 网页与 App (`deepseek-chat`)

- 官方入口：https://www.deepseek.com/
- 操作文档：https://www.deepseek.com/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：由官网进入对话或官方下载；登录，按需要开启当前推理/搜索功能；发送轻量任务。
- 可用标准：回复成功，所需功能确实开启。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## DeepSeek Harness (`deepseek-harness`)

- 官方入口：https://www.deepseek.com/harness/
- 操作文档：https://github.com/deepseek-ai/deepseek-harness
- 路线：APP / LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：沿官网进入原厂仓库/下载；按当前 README 准备运行时和独立配置；选择受支持模型并登录或接入密钥；运行临时目录任务。
- 可用标准：任务有实际结果，重开后配置仍可用。
- 特别说明：只沿官网链路，不选名字相近的第三方桌面封装。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## DeepSeek API (`deepseek-api`)

- 官方入口：https://platform.deepseek.com/
- 操作文档：https://api-docs.deepseek.com/
- 路线：API；读取 `../recipes.md` 对应步骤。
- 执行：查 API 文档与当前模型列表；申请密钥，配置官方 base URL；用文本兼容接口做轻量调用。
- 可用标准：有效内容返回，区分模型系列与实际 API ID。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## DeepSeek 通用、推理与蒸馏开放模型 (`deepseek-models`)

- 官方入口：https://github.com/deepseek-ai
- 操作文档：https://github.com/deepseek-ai
- 路线：LOCAL / API；读取 `../recipes.md` 对应步骤。
- 执行：从官方组织进入精确版本模型卡；按实际内存选择蒸馏/量化等版本，不盲目下载完整超大模型；启动匹配推理器。
- 可用标准：本地推理成功；API 路线另按平台验证。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## DeepSeek-Coder / Math / VL / Janus 等研究模型 (`deepseek-special`)

- 官方入口：https://github.com/deepseek-ai
- 操作文档：https://github.com/deepseek-ai
- 路线：LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：查所选仓库 README、许可证和维护状态；建立独立环境；下载确切权重，运行该模态官方示例。
- 可用标准：专项样例成功；历史研究模型与当前在线产品分开记录。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

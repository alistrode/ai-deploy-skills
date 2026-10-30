# xAI / Grok

助手、实时信息、图像视频和语音

先介绍业务线，再按用户选择执行对应产品卡。所有入口是官方资料起点，操作时重新核对当日状态。

| 产品 | 适用用途 | 支持路线 |
|---|---|---|
| Grok / X 内 Grok | 大众问答与实时信息 | WEB / APP |
| Grok Imagine | 图像与视频生成编辑 | WEB / APP / API |
| Grok Voice | 语音交互与语音 API | WEB / APP / API |
| Grok API：文本、代码、Web/X Search、文件 | 开发接入 | API |
| 已开放的 Grok 历史权重 | 研究与自建推理 | LOCAL |

## Grok / X 内 Grok (`grok`)

- 官方入口：https://grok.com/
- 操作文档：https://x.ai/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：通过官方网页/App 或用户已登录 X 的 Grok 入口；创建对话，按用途开启搜索/推理。
- 可用标准：有效回复；实时信息任务打开来源检查。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Grok Imagine (`grok-imagine`)

- 官方入口：https://x.ai/api/imagine
- 操作文档：https://x.ai/api/imagine
- 路线：WEB / APP / API；读取 `../recipes.md` 对应步骤。
- 执行：个人用户进入 Grok 的 Imagine；开发者按当前 API 文档；选最小样例，视频保存任务 ID 并跟踪。
- 可用标准：真实图片/视频可预览，API 返回的 URL 可访问或产物已保存。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Grok Voice (`grok-voice`)

- 官方入口：https://x.ai/api
- 操作文档：https://x.ai/api
- 路线：WEB / APP / API；读取 `../recipes.md` 对应步骤。
- 执行：官方应用授权麦克风完成一轮语音；API 使用官方 Voice 文档的实时协议或 TTS/STT 示例，不套文本接口。
- 可用标准：所选语音功能真正完成输入输出。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Grok API：文本、代码、Web/X Search、文件 (`grok-api`)

- 官方入口：https://docs.x.ai/
- 操作文档：https://docs.x.ai/
- 路线：API；读取 `../recipes.md` 对应步骤。
- 执行：选择当前模型，创建项目密钥；文本最小调用；搜索需启用官方工具，文件需按接口上传虚构样例。
- 可用标准：所选能力有真实结果，搜索包含可核对来源。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## 已开放的 Grok 历史权重 (`grok-open`)

- 官方入口：https://github.com/xai-org
- 操作文档：https://github.com/xai-org
- 路线：LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：只选择官方明确提供的权重及其 README；评估巨大模型硬件；最新在线 Grok 不默认开放。
- 可用标准：精确版本本地运行，明确其与线上当前服务的区别。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

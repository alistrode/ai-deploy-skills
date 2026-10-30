# OpenAI / ChatGPT

大众助手、办公、编程、浏览器及模型接入

先介绍业务线，再按用户选择执行对应产品卡。所有入口是官方资料起点，操作时重新核对当日状态。

| 产品 | 适用用途 | 支持路线 |
|---|---|---|
| ChatGPT | 问答、学习、写作、搜索 | WEB / APP |
| ChatGPT Work | 长任务与办公交付 | WEB / APP |
| ChatGPT 研究、图像、语音、学习、Sites/Slides | 应用内专项功能 | WEB / APP |
| Codex | AI 编程代理 | CLI / APP / EXT / WEB |
| ChatGPT Atlas | AI 浏览器 | APP |
| OpenAI API：文本、推理、图像、转录、TTS、Realtime | 开发接入 | API |
| gpt-oss | 开放权重语言模型 | LOCAL |
| Whisper | 本地语音识别 | LOCAL |
| Sora | 历史视频产品 | HISTORY |

## ChatGPT (`chatgpt`)

- 官方入口：https://chatgpt.com/
- 操作文档：https://chatgpt.com/overview/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：新建对话；根据用途选择普通聊天或搜索；发送简短请求；需要客户端时从下载入口匹配系统。
- 可用标准：当前账户返回有效回复，保存入口。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## ChatGPT Work (`chatgpt-work`)

- 官方入口：https://chatgpt.com/
- 操作文档：https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：进入账户可见的 Work 入口；用虚构数据制作一页工作说明；观察执行过程和文件。
- 可用标准：文档可打开且能继续编辑；没有权限时记录套餐限制。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## ChatGPT 研究、图像、语音、学习、Sites/Slides (`chatgpt-features`)

- 官方入口：https://chatgpt.com/overview/
- 操作文档：https://chatgpt.com/overview/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：先按需求选择具体功能；研究看来源，图像预览结果，语音检查输入输出设备，Sites/Slides 打开生成预览；不自动对外发布。
- 可用标准：所选功能的一个任务完成；每项分别验收，不把聊天成功算成所有功能成功。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Codex (`codex`)

- 官方入口：https://developers.openai.com/codex/
- 操作文档：https://github.com/openai/codex
- 路线：CLI / APP / EXT / WEB；读取 `../recipes.md` 对应步骤。
- 执行：阅读当前 CLI/IDE/应用文档；npm 路线见 recipes；完成官方登录，在新临时项目分析一个示例文件。
- 可用标准：实际任务正常返回，确认工作目录与生成文件。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## ChatGPT Atlas (`atlas`)

- 官方入口：https://chatgpt.com/atlas/
- 操作文档：https://chatgpt.com/atlas/
- 路线：APP；读取 `../recipes.md` 对应步骤。
- 执行：查看当前支持系统；官方安装并登录；打开公开网页，用侧栏归纳三点。
- 可用标准：浏览器可重复启动，侧栏产生与该页相关的回答。
- 特别说明：不支持当前系统时直接报告，并提供 ChatGPT 网页作为可选路线而非等价安装。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## OpenAI API：文本、推理、图像、转录、TTS、Realtime (`openai-api`)

- 官方入口：https://platform.openai.com/
- 操作文档：https://developers.openai.com/api/docs/models
- 路线：API；读取 `../recipes.md` 对应步骤。
- 执行：选择项目，读取当前模型目录与认证方法；文本使用受支持的 Responses/Chat 接口；媒体和实时音频使用对应官方 SDK 例子。
- 可用标准：所选模态有实际输出；实时语音需完成连接和音频往返。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## gpt-oss (`gpt-oss`)

- 官方入口：https://openai.com/open-models/
- 操作文档：https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss
- 路线：LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：从官方链接进入模型仓库；核对许可证和内存，选择适配版本；按官方支持运行器加载并推理。
- 可用标准：本地生成回答，记录是否离线、实际后端与模型。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Whisper (`whisper`)

- 官方入口：https://github.com/openai/whisper
- 操作文档：https://github.com/openai/whisper
- 路线：LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：独立 Python 环境安装官方包与 FFmpeg；按硬件选择模型；准备无隐私的短录音并按 README 转写。
- 可用标准：产出能打开的转录文本，语言和内容合理。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Sora (`sora`)

- 官方入口：https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation
- 操作文档：https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation
- 路线：HISTORY；读取 `../recipes.md` 对应步骤。
- 执行：核对官方结束服务公告；不执行旧安装/API 教程；如用户愿意，推荐其余品牌的视频路线。
- 可用标准：明确记录已下线，只有用户选定替代产品后才执行替代。
- 特别说明：编写时公告：网页/App 2026-04-26、API 2026-09-24 结束服务。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

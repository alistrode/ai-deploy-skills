# 阿里巴巴 / 千问

大众应用、编程、视觉生成、语音、模型服务与开放权重

先介绍业务线，再按用户选择执行对应产品卡。所有入口是官方资料起点，操作时重新核对当日状态。

| 产品 | 适用用途 | 支持路线 |
|---|---|---|
| 千问应用 / Qwen Chat | 大众 AI 助手 | WEB / APP |
| Qwen Code | 开源终端编程代理 | CLI |
| Qoder / Qoder CN（原灵码相关入口） | AI IDE、CLI 与插件 | APP / CLI / EXT |
| 通义灵码 | 编程辅助及旧名称入口 | APP / EXT |
| 通义万相 / Wan 创作平台 | 图像、视频与视觉创作 | WEB / API |
| 通义听悟 | 音视频转写与会议总结 | WEB / API |
| 百炼 / Model Studio / Qwen API | 托管模型与应用平台 | WEB / API |
| Qwen 通用：Max / Plus / Flash / Turbo 与开放模型 | 通用任务；旗舰/均衡/速度成本定位，以当前目录为准 | API / LOCAL |
| Qwen-Coder | 代码与工程 Agent | API / LOCAL |
| Qwen-VL / QVQ | 视觉理解、OCR、图表及视觉推理 | API / LOCAL |
| Qwen-Omni | 文本、音频、视觉等多模态交互 | API / LOCAL |
| Qwen-Image | 图片生成和编辑 | API / LOCAL |
| Qwen-TTS / ASR | 语音合成、识别 | API / LOCAL |
| QwQ / Qwen 推理、Math 系列 | 推理和数学；旧系列需查是否有当前替代 | API / LOCAL |
| Qwen-Long / Doc / Embedding / Rerank | 长文档、信息提取、检索向量与排序 | API / LOCAL |
| Wan 开放模型 | 本地图像/视频生成 | LOCAL |
| CosyVoice | 语音合成与授权声音定制 | LOCAL / API |
| Fun-ASR / FunASR | 本地语音识别 | LOCAL / API |

## 千问应用 / Qwen Chat (`qianwen`)

- 官方入口：https://www.qianwen.com/
- 操作文档：https://qwen.ai/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：官网选择适合地区的入口；登录，选聊天、文档或多模态；按官网提供的客户端下载。
- 可用标准：所选任务有结果；记录实际账户站点，不假定国内外权益互通。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Qwen Code (`qwen-code`)

- 官方入口：https://github.com/QwenLM/qwen-code
- 操作文档：https://github.com/QwenLM/qwen-code
- 路线：CLI；读取 `../recipes.md` 对应步骤。
- 执行：读当前安装 README；官方 npm 路线见 recipes；运行 qwen 并按当前界面选择 OAuth 或受支持 API；使用临时项目。
- 可用标准：实际产生可检查的代码/分析，确认所用供应商和额度。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Qoder / Qoder CN（原灵码相关入口） (`qoder`)

- 官方入口：https://qoder.com/
- 操作文档：https://docs.qoder.com/product-series/quick-start
- 路线：APP / CLI / EXT；读取 `../recipes.md` 对应步骤。
- 执行：先核对国内 qoder.cn/灵码官网的迁移说明；选择 IDE、CLI 或 JetBrains/编辑器插件；按对应文档安装和登录；避免混用地区端点。
- 可用标准：临时项目单文件任务成功，实际计费渠道清楚。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## 通义灵码 (`lingma`)

- 官方入口：https://lingma.aliyun.com/
- 操作文档：https://lingma.aliyun.com/
- 路线：APP / EXT；读取 `../recipes.md` 对应步骤。
- 执行：核对当前页面是否迁移至 Qoder CN；沿官方迁移路径安装；若仍有原插件，核对发行者后启用并登录。
- 可用标准：当前支持的工具完成代码解释或补全，不安装失效旧包。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## 通义万相 / Wan 创作平台 (`wanxiang`)

- 官方入口：https://tongyi.aliyun.com/
- 操作文档：https://tongyi.aliyun.com/
- 路线：WEB / API；读取 `../recipes.md` 对应步骤。
- 执行：进入万相官方产品链接，选图像或视频能力；用最低规格样例生成并等待完成；API 按百炼文档配置。
- 可用标准：产物可预览，可下载需求另检查文件。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## 通义听悟 (`tingwu`)

- 官方入口：https://tingwu.aliyun.com/
- 操作文档：https://help.aliyun.com/zh/tingwu/product-introduction/
- 路线：WEB / API；读取 `../recipes.md` 对应步骤。
- 执行：从官方页面进入服务；上传一段自有无隐私的短录音；选择转写/总结并等待；需要 API 时读阿里云接入文档。
- 可用标准：有可查看文本和摘要，导出需求检查实际文件。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## 百炼 / Model Studio / Qwen API (`bailian`)

- 官方入口：https://bailian.console.aliyun.com/
- 操作文档：https://www.alibabacloud.com/help/en/model-studio/
- 路线：WEB / API；读取 `../recipes.md` 对应步骤。
- 执行：核对地域，选择项目/空间，开通模型权限；从当前文档获取端点、模型、密钥；区分按量 API 与 Coding Plan；用体验中心或接口调用。
- 可用标准：模型调用真实成功，应用草稿可重复运行。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Qwen 通用：Max / Plus / Flash / Turbo 与开放模型 (`qwen-general`)

- 官方入口：https://tongyi.aliyun.com/
- 操作文档：https://huggingface.co/Qwen
- 路线：API / LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：先选 API 或本地；API 从百炼查当前型号；本地从 Qwen 官方集合进入精确模型卡，核对开放情况、硬件及专用依赖；按照该模态官方样例运行。
- 可用标准：当前选定型号及模态实际产生有效结果。
- 特别说明：Max/Plus/Flash 等托管型号不保证有同名权重；不可凭名称拼接仓库。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Qwen-Coder (`qwen-coder-model`)

- 官方入口：https://tongyi.aliyun.com/
- 操作文档：https://huggingface.co/Qwen
- 路线：API / LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：先选 API 或本地；API 从百炼查当前型号；本地从 Qwen 官方集合进入精确模型卡，核对开放情况、硬件及专用依赖；按照该模态官方样例运行。
- 可用标准：当前选定型号及模态实际产生有效结果。
- 特别说明：Max/Plus/Flash 等托管型号不保证有同名权重；不可凭名称拼接仓库。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Qwen-VL / QVQ (`qwen-vl`)

- 官方入口：https://tongyi.aliyun.com/
- 操作文档：https://huggingface.co/Qwen
- 路线：API / LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：先选 API 或本地；API 从百炼查当前型号；本地从 Qwen 官方集合进入精确模型卡，核对开放情况、硬件及专用依赖；按照该模态官方样例运行。
- 可用标准：当前选定型号及模态实际产生有效结果。
- 特别说明：Max/Plus/Flash 等托管型号不保证有同名权重；不可凭名称拼接仓库。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Qwen-Omni (`qwen-omni`)

- 官方入口：https://tongyi.aliyun.com/
- 操作文档：https://huggingface.co/Qwen
- 路线：API / LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：先选 API 或本地；API 从百炼查当前型号；本地从 Qwen 官方集合进入精确模型卡，核对开放情况、硬件及专用依赖；按照该模态官方样例运行。
- 可用标准：当前选定型号及模态实际产生有效结果。
- 特别说明：Max/Plus/Flash 等托管型号不保证有同名权重；不可凭名称拼接仓库。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Qwen-Image (`qwen-image`)

- 官方入口：https://tongyi.aliyun.com/
- 操作文档：https://huggingface.co/Qwen
- 路线：API / LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：先选 API 或本地；API 从百炼查当前型号；本地从 Qwen 官方集合进入精确模型卡，核对开放情况、硬件及专用依赖；按照该模态官方样例运行。
- 可用标准：当前选定型号及模态实际产生有效结果。
- 特别说明：Max/Plus/Flash 等托管型号不保证有同名权重；不可凭名称拼接仓库。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Qwen-TTS / ASR (`qwen-speech`)

- 官方入口：https://tongyi.aliyun.com/
- 操作文档：https://huggingface.co/Qwen
- 路线：API / LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：先选 API 或本地；API 从百炼查当前型号；本地从 Qwen 官方集合进入精确模型卡，核对开放情况、硬件及专用依赖；按照该模态官方样例运行。
- 可用标准：当前选定型号及模态实际产生有效结果。
- 特别说明：Max/Plus/Flash 等托管型号不保证有同名权重；不可凭名称拼接仓库。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## QwQ / Qwen 推理、Math 系列 (`qwen-reasoning`)

- 官方入口：https://tongyi.aliyun.com/
- 操作文档：https://huggingface.co/Qwen
- 路线：API / LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：先选 API 或本地；API 从百炼查当前型号；本地从 Qwen 官方集合进入精确模型卡，核对开放情况、硬件及专用依赖；按照该模态官方样例运行。
- 可用标准：当前选定型号及模态实际产生有效结果。
- 特别说明：Max/Plus/Flash 等托管型号不保证有同名权重；不可凭名称拼接仓库。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Qwen-Long / Doc / Embedding / Rerank (`qwen-long`)

- 官方入口：https://tongyi.aliyun.com/
- 操作文档：https://huggingface.co/Qwen
- 路线：API / LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：先选 API 或本地；API 从百炼查当前型号；本地从 Qwen 官方集合进入精确模型卡，核对开放情况、硬件及专用依赖；按照该模态官方样例运行。
- 可用标准：当前选定型号及模态实际产生有效结果。
- 特别说明：Max/Plus/Flash 等托管型号不保证有同名权重；不可凭名称拼接仓库。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Wan 开放模型 (`wan-model`)

- 官方入口：https://github.com/Wan-Video
- 操作文档：https://github.com/Wan-Video
- 路线：LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：从官方组织选择当前仓库与模型卡；按照显存选规格，下载官方权重，使用 README 的推理或受支持工作流。
- 可用标准：本地产出可播放视频/可查看图片，并记录所选版本。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## CosyVoice (`cosyvoice`)

- 官方入口：https://github.com/FunAudioLLM/CosyVoice
- 操作文档：https://github.com/FunAudioLLM/CosyVoice
- 路线：LOCAL / API；读取 `../recipes.md` 对应步骤。
- 执行：按 README 建隔离环境并下载对应模型；安装音频依赖，先用预设音色推理；API 从百炼查对应服务。
- 可用标准：合成短音频可播放。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Fun-ASR / FunASR (`funasr`)

- 官方入口：https://github.com/modelscope/FunASR
- 操作文档：https://github.com/modelscope/FunASR
- 路线：LOCAL / API；读取 `../recipes.md` 对应步骤。
- 执行：按当前官方文档选择模型和运行方式；安装独立环境及音频依赖；用自有短录音识别。
- 可用标准：转写文本可读且与样例一致；不能用 TTS 成功代替 ASR。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

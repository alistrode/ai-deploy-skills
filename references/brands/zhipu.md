# 智谱 / GLM

清言、自动操作、编程、视觉和开放模型

先介绍业务线，再按用户选择执行对应产品卡。所有入口是官方资料起点，操作时重新核对当日状态。

| 产品 | 适用用途 | 支持路线 |
|---|---|---|
| 智谱清言 / Z.ai Chat | 大众助手、文档、研究与办公 | WEB / APP |
| AutoGLM | 自动操作与任务代理 | WEB / APP |
| Open-AutoGLM | 手机操作模型与框架 | PHONE / LOCAL |
| ZCode | AI 编程工具 | APP / CLI |
| GLM Coding Plan / Coding Tool Helper | 编码工具订阅接入 | CLI / API |
| 智谱开放平台 / Z.ai API | 通用、视觉、图像、视频与语音 API | API / WEB |
| GLM 通用、推理、编程、GLM-V 视觉与语音模型 | API 与本地开放模型 | LOCAL / API |
| CogView / GLM 图像模型 | 图片生成 | LOCAL / API |
| CogVideoX / 清影 | 视频模型与大众视频入口 | LOCAL / WEB / API |

## 智谱清言 / Z.ai Chat (`qingyan`)

- 官方入口：https://chatglm.cn/
- 操作文档：https://z.ai/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：国内清言从官网进入；国际 Z.ai 从 z.ai 官方链接进入；登录选任务/对话，使用公开或虚构样例。
- 可用标准：当前账户返回结果；研究/文档专项另检查产物。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## AutoGLM (`autoglm`)

- 官方入口：https://chatglm.cn/
- 操作文档：https://chatglm.cn/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：从官方当前产品页面找到 AutoGLM 形态；完成账户与设备授权；只做读取公开信息等无外部副作用任务。
- 可用标准：实际任务完成，操作目标与权限清楚。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Open-AutoGLM (`open-autoglm`)

- 官方入口：https://github.com/zai-org/Open-AutoGLM
- 操作文档：https://github.com/zai-org/Open-AutoGLM
- 路线：PHONE / LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：读 README 安装隔离 Python 环境及依赖；官方平台工具配置 ADB、设备授权与输入法；模型用官方支持 API 或本地服务；先确认 adb devices 和目标屏幕。
- 可用标准：只打开系统设置/读取设备信息等低风险任务成功，保存启动入口。
- 特别说明：不自动开启无线公网调试，不点击支付、发送消息或删除，不把云端容器冒充手机。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## ZCode (`zcode`)

- 官方入口：https://zcode.z.ai/
- 操作文档：https://zcode.z.ai/en/docs/configuration
- 路线：APP / CLI；读取 `../recipes.md` 对应步骤。
- 执行：从官方文档检查当前产品形态和系统支持；安装后选择 Z.ai 编码套餐或官方支持供应商，完成登录；临时仓库做分析。
- 可用标准：代码任务真实完成，明确模型和计费渠道。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## GLM Coding Plan / Coding Tool Helper (`glm-coding`)

- 官方入口：https://docs.bigmodel.cn/cn/coding-plan/overview
- 操作文档：https://docs.bigmodel.cn/cn/coding-plan/extension/coding-tool-helper
- 路线：CLI / API；读取 `../recipes.md` 对应步骤。
- 执行：确定国内/国际与个人/团队计划；从官方指定工具列表选择；可按官方文档运行 npx @z_ai/coding-helper，先检查包来源与当前指令；只修改选定工具局部配置。
- 可用标准：指定编码工具完成任务；普通文本 API 不消耗该套餐来伪造测试。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## 智谱开放平台 / Z.ai API (`bigmodel`)

- 官方入口：https://bigmodel.cn/
- 操作文档：https://docs.z.ai/
- 路线：API / WEB；读取 `../recipes.md` 对应步骤。
- 执行：核对区域、组织和按量服务；读官方快速入门获取端点与密钥；所需视觉/媒体用专用请求格式。
- 可用标准：相应能力输出成功，普通 API 与 Coding Plan 分别确认。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## GLM 通用、推理、编程、GLM-V 视觉与语音模型 (`glm-models`)

- 官方入口：https://huggingface.co/zai-org
- 操作文档：https://huggingface.co/zai-org
- 路线：LOCAL / API；读取 `../recipes.md` 对应步骤。
- 执行：按能力和硬件选择明确版本；视觉模型用配套 processor 和模型卡示例，语音按专用依赖；API 查看当前目录。
- 可用标准：所选模态实际成功，开放许可逐版本确认。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## CogView / GLM 图像模型 (`cogview`)

- 官方入口：https://github.com/THUDM
- 操作文档：https://github.com/THUDM
- 路线：LOCAL / API；读取 `../recipes.md` 对应步骤。
- 执行：从官方组织或智谱当前文档寻找 CogView 精确仓库；按 README 安装官方推理依赖和权重，或使用当前托管接口。
- 可用标准：生成的图片可预览；旧系列状态需核对。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## CogVideoX / 清影 (`cogvideo`)

- 官方入口：https://github.com/THUDM/CogVideo
- 操作文档：https://github.com/THUDM/CogVideo
- 路线：LOCAL / WEB / API；读取 `../recipes.md` 对应步骤。
- 执行：本地按仓库选择 CogVideoX 权重与显存；网页从清言进入清影（如当前仍提供）；API 读取开放平台视频文档。
- 可用标准：最短样例视频可播放；区分清影应用与 CogVideoX 模型。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

# 字节跳动 / 豆包

助手、图像视频、工作流、编程和模型平台

先介绍业务线，再按用户选择执行对应产品卡。所有入口是官方资料起点，操作时重新核对当日状态。

| 产品 | 适用用途 | 支持路线 |
|---|---|---|
| 豆包 | 大众聊天与多模态助手 | WEB / APP |
| 即梦 AI | 图片与视频创作 | WEB / APP |
| 扣子（原扣子空间） | 任务、办公与 Agent 协作 | WEB / APP |
| 扣子编程（原扣子开发平台） | 应用、智能体、工作流、Skills | WEB |
| Coze Studio 开放项目 | 自建工作流开发平台 | LOCAL |
| TRAE IDE / TRAE Code | AI 编程工作区 | APP |
| TRAE SOLO 独立端 | 任务驱动的工作与开发 | APP / WEB |
| 火山方舟 | 模型体验与 API 平台 | WEB / API |
| Seed / 豆包通用模型 | 通用语言、推理和 Agent | WEB / API |
| Seedream | 图像生成与编辑 | WEB / API |
| Seedance | 视频生成 | WEB / API |
| Seed Audio / SeedTTS / 声音复刻 | 音频、语音合成与声音 | WEB / API |
| SeedRealtime | 实时音视频交互 | WEB / API |

## 豆包 (`doubao`)

- 官方入口：https://www.doubao.com/
- 操作文档：https://www.doubao.com/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：进入官方对话，选择所需语音/图片/文档功能；客户端从官网跳转商店；用轻量样例操作。
- 可用标准：所选功能有可见结果；语音需设备授权后音频往返。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## 即梦 AI (`jimeng`)

- 官方入口：https://jimeng.jianying.com/
- 操作文档：https://jimeng.jianying.com/
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：选图片或视频；输入简单自然风景提示，设置最小可用规格；查看积分后提交一次，查询同一任务至完成。
- 可用标准：结果可预览；需下载时检查成品文件。
- 特别说明：Seedream/Seedance 是模型线，不能当成即梦客户端安装包。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## 扣子（原扣子空间） (`coze`)

- 官方入口：https://space.coze.cn/space-intro
- 操作文档：https://www.coze.cn/open/docs/cozespace/overview
- 路线：WEB / APP；读取 `../recipes.md` 对应步骤。
- 执行：进入官方工作台；选办公或研究任务；使用虚构样例生成一份简短材料；保留项目。
- 可用标准：产物可打开，任务状态为成功。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## 扣子编程（原扣子开发平台） (`coze-code`)

- 官方入口：https://www.coze.cn/
- 操作文档：https://docs.coze.cn/
- 路线：WEB；读取 `../recipes.md` 对应步骤。
- 执行：进入编程/开发入口，新建私有草稿；构建输入文本→模型→输出的最小工作流并调试；应用只预览不公开。
- 可用标准：调试输入输出一致，草稿可再次运行。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Coze Studio 开放项目 (`coze-studio`)

- 官方入口：https://github.com/coze-dev/coze-studio
- 操作文档：https://github.com/coze-dev/coze-studio
- 路线：LOCAL；读取 `../recipes.md` 对应步骤。
- 执行：按当前官方 README 确认支持范围；读部署清单，在独立目录配置 Docker Compose 和私密环境文件；仅回环访问。
- 可用标准：前后端可访问，配置受支持模型后草稿工作流真正运行。
- 特别说明：开放项目与云端扣子功能不承诺完全一致。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## TRAE IDE / TRAE Code (`trae`)

- 官方入口：https://www.trae.cn/
- 操作文档：https://docs.trae.cn/ide_get-started-with-trae
- 路线：APP；读取 `../recipes.md` 对应步骤。
- 执行：选国内/国际产品渠道，下载安装 IDE；登录，打开临时项目；选择 IDE 或 SOLO 模式完成单文件任务。
- 可用标准：文件生成、预览或执行成功，保留项目入口。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## TRAE SOLO 独立端 (`trae-solo`)

- 官方入口：https://www.trae.cn/
- 操作文档：https://www.trae.cn/
- 路线：APP / WEB；读取 `../recipes.md` 对应步骤。
- 执行：从官网进入 SOLO 独立产品，核对平台和账户；创建研究或简单开发任务；观察任务及产物。
- 可用标准：任务有可打开结果，区分独立端与 IDE 内 SOLO 模式。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## 火山方舟 (`ark`)

- 官方入口：https://www.volcengine.com/product/ark
- 操作文档：https://docs.volcengine.com/docs/ark/model-list
- 路线：WEB / API；读取 `../recipes.md` 对应步骤。
- 执行：登录控制台，选区域，进入模型列表/体验中心；获取当前模型 ID 与调用文档，使用对应项目密钥。
- 可用标准：所选模型实际返回，不把体验中心权限等同 API 权限。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Seed / 豆包通用模型 (`seed`)

- 官方入口：https://seed.bytedance.com/zh/models
- 操作文档：https://seed.bytedance.com/zh/models
- 路线：WEB / API；读取 `../recipes.md` 对应步骤。
- 执行：从模型官方页的体验/API 链接进入；读取当前输入格式、模型 ID、配额与计费，执行文本调用；异步任务保留原 ID。
- 可用标准：相应文本/图像/视频/音频真实返回并可预览。
- 特别说明：声音复刻只使用本人或有授权声音；不把托管模型假称开放权重。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Seedream (`seedream`)

- 官方入口：https://seed.bytedance.com/zh/models
- 操作文档：https://seed.bytedance.com/zh/models
- 路线：WEB / API；读取 `../recipes.md` 对应步骤。
- 执行：从模型官方页的体验/API 链接进入；读取当前输入格式、模型 ID、配额与计费，执行小尺寸图像生成；异步任务保留原 ID。
- 可用标准：相应文本/图像/视频/音频真实返回并可预览。
- 特别说明：声音复刻只使用本人或有授权声音；不把托管模型假称开放权重。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Seedance (`seedance`)

- 官方入口：https://seed.bytedance.com/zh/models
- 操作文档：https://seed.bytedance.com/zh/models
- 路线：WEB / API；读取 `../recipes.md` 对应步骤。
- 执行：从模型官方页的体验/API 链接进入；读取当前输入格式、模型 ID、配额与计费，执行短视频生成；异步任务保留原 ID。
- 可用标准：相应文本/图像/视频/音频真实返回并可预览。
- 特别说明：声音复刻只使用本人或有授权声音；不把托管模型假称开放权重。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## Seed Audio / SeedTTS / 声音复刻 (`seed-audio`)

- 官方入口：https://seed.bytedance.com/zh/models
- 操作文档：https://seed.bytedance.com/zh/models
- 路线：WEB / API；读取 `../recipes.md` 对应步骤。
- 执行：从模型官方页的体验/API 链接进入；读取当前输入格式、模型 ID、配额与计费，执行使用预设声音合成一句话；异步任务保留原 ID。
- 可用标准：相应文本/图像/视频/音频真实返回并可预览。
- 特别说明：声音复刻只使用本人或有授权声音；不把托管模型假称开放权重。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

## SeedRealtime (`seed-realtime`)

- 官方入口：https://seed.bytedance.com/zh/models
- 操作文档：https://seed.bytedance.com/zh/models
- 路线：WEB / API；读取 `../recipes.md` 对应步骤。
- 执行：从模型官方页的体验/API 链接进入；读取当前输入格式、模型 ID、配额与计费，执行建立实时会话并做一轮语音交互；异步任务保留原 ID。
- 可用标准：相应文本/图像/视频/音频真实返回并可预览。
- 特别说明：声音复刻只使用本人或有授权声音；不把托管模型假称开放权重。
- 网页操作：读取 `../web-operations.md`，根据当前可访问页面定位真实控件；需要本人登录时保留现场，完成后继续。

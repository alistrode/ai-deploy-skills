# AI 软件就绪技能

一个可独立使用的中文 AI 技能：先介绍十个品牌，用户选择后介绍业务线，再由 AI 自动安装、配置或操作官网，直到所选产品完成首个真实任务。

**入口：[SKILL.md](SKILL.md)**。包含十个品牌、95 个产品/业务条目，以及官方入口、安装路线、网页操作和完成标准。条目包含独立产品、应用内功能、模型系列和历史映射，不代表 95 款独立软件，也不代表已将其全部实机安装验收。

品牌范围：OpenAI、字节跳动、阿里千问、Google Gemini、Anthropic Claude、DeepSeek、Kimi、Grok、MiniMax、智谱。Microsoft Copilot、文小言、腾讯元宝和 Perplexity 不在本技能品牌范围内。

## 使用

把整个仓库作为一个技能目录保存，保留 `SKILL.md`、`references/`、`scripts/` 和 `templates/`。单独复制 SKILL.md 会丢失产品执行卡。

- 支持项目技能的 AI：将完整目录放入项目 `.agents/skills/ai-software-ready/`，按该 AI 当前规则启用。
- Claude Code 等支持其他技能目录的工具：将完整目录放入其官方规定的技能目录，例如 `.claude/skills/ai-software-ready/`，以实际版本文档为准。
- 支持导入 `.skill` 的工具：使用 Release 附件；只支持文件夹的工具可将附件作为 ZIP 解压。不同 AI 的导入方式不同，不声称所有平台都有统一导入按钮。
- 普通具备文件读取与操作工具的 AI：让它先读取本目录 SKILL.md，再按相对路径读取所选品牌卡。

给 AI 的提示示例：

> 使用 ai-software-ready 技能，先介绍十个品牌。我选完之后，你介绍该品牌的业务线，并把选定产品安装或把官方网页操作到能完成实际任务。

> 使用这个技能，在我已授权连接的 Windows 电脑装好 Qwen Code；你完成安装、登录后的配置和首个示例任务。

> 我选 Kimi 的 PPT 业务。请直接操作官网生成一份三页示例，打开结果确认可编辑。

只有用户当前选择范围会被执行。制作/导入技能本身不会安装十家产品。

## 文件

```text
SKILL.md                     主流程与执行规则
references/catalog.json      95 个条目的结构化执行卡
references/brands/*.md       十个品牌的阅读版执行卡
references/recipes.md        网页、客户端、CLI、插件、API、模型、手机路线
references/web-operations.md AI 实际操作网站的方法
references/sources.md        官方资料与动态更新规则
scripts/catalog.py           按品牌/产品读取目录
scripts/inspect_environment.py 目标环境探测
scripts/api_probe.py         默认不请求的文本 API 探测
templates/session.json       不含秘密的断点状态
templates/report.md          实际结果报告
```

辅助脚本只需要 Python 3.9+ 标准库，没有必须预装的第三方依赖。没有 Python 的执行 AI 可以按文档用目标系统工具完成对应工作。

```sh
python scripts/catalog.py
python scripts/catalog.py --brand alibaba
python scripts/catalog.py --product qwen-code
python scripts/inspect_environment.py
python scripts/api_probe.py --help
```

技能需要宿主 AI 具备目标终端、文件或交互浏览器/桌面工具。搜索和网页抓取只能研究文档；缺少交互工具时不会假称已经操作网站。登录扫码、验证码、实名、付款等由本人完成必要一步，AI 保留现场并继续后续操作。新订阅和未经授权费用不会自动购买。

## 当前交付范围

本仓库交付的是可执行工作流程、产品卡和辅助脚本，不捆绑第三方安装器、商业软件、模型权重或账户凭据。安装命令和可用型号执行时回到原厂文档确认；不把旧版本安装方法永远固定下来。Sora 等历史服务保留状态说明，不作为当前可安装产品。

文档与脚本完成结构检查和本地无凭据检查；十家真实账户、各系统安装、媒体生成和模型推理需要在实际使用该技能、选定产品与目标之后逐项验收。

## 维护

新增/修改产品以 `references/catalog.json` 为源，同时更新相应品牌 Markdown。保留具体入口、执行步骤、可用标准和能力边界。修订过期名称或命令后同步资料日期；不以资料更新时间冒充全产品实机验收日期。

本仓库原创技能文字和脚本采用 MIT 许可。第三方产品、模型、商标及服务条款分别归原权利人；本项目不代表这些品牌的官方发行。

# 🎁 FreeToken｜免费 AI API Token 获取指南（2026）

> Free AI API Keys / Tokens / Free Tier / LLM API Directory · 面向中文开发者的开源免费额度导航。

**官方网站：[FreeToken 可搜索资源库](https://aipmandy.github.io/FreeToken/)** · **作者：[AI酋长Andy](https://metaver.vip/)** · **微信：`AIPMAndy`（备注 FreeToken）**

收集 **Gemini、OpenRouter、Groq、Cloudflare Workers AI、Hugging Face、Cohere、DeepSeek、Qwen、智谱 GLM、NVIDIA、硅基流动** 等平台的 AI API 获取方式。每条说明免费资格、申请入口、官方来源、限制和核验日期。

> ⚠️ **免费网页聊天 ≠ 免费 API。试用体验金 ≠ 永久免费。** 免费策略会因账号、国家/地区、模型、计费方式而变化。本站绝不分发共享 API Key，也不保证任何固定权益长期有效。

**本次深度复核：2026-10-22。** “官方文档已核对”表示核验了公开说明，**不代表已登录不同地区账号实测额度**。本次未能证实的赠额已降级为待核验，历史活动不继续宣传。

> **TL;DR｜一句话**：FreeToken 是 AI 酋长 Andy 维护的免费 AI API 额度导航。适合想低成本调用大模型的中文开发者。它整理 Gemini、OpenRouter、Groq、Cloudflare Workers AI、硅基流动等平台的免费层与试用额度，每条附官方来源和核验日期，并标出待核验项。
>
> 作者：AI 酋长 Andy（[GitHub @AIPMAndy](https://github.com/AIPMAndy) · [X @AIPMAndy](https://x.com/AIPMAndy) · [metaver.vip](https://metaver.vip/)）

## 目录

- [免费 AI API 资源总表](#免费-ai-api-资源总表)
- [更多免费 API 开源项目 / 云服务 / 数据服务](#更多免费-api-开源项目--云服务--数据服务)
- [怎么选平台](#怎么选平台)
- [5 分钟上手](#5-分钟上手)
- [免费额度的常见误解](#免费额度的常见误解)
- [安全与成本](#安全与成本)
- [贡献和纠错](#贡献和纠错)
- [作者与联系](#作者与联系)

## 免费 AI API 资源总表

<!-- FREETOKEN_TABLE_START -->
| 平台 | 类型 | 当前公开政策 / 注意 | 来源 | 审核状态 |
|---|---|---|---|---|
| [Google Gemini API](https://aistudio.google.com/) | 官方免费层 | Gemini 2.5 Flash / Flash-Lite 等部分模型有免费输入输出 Token；实时 RPM/TPM/RPD 按项目和模型显示。 | [官方来源](https://ai.google.dev/gemini-api/docs/pricing) | 2026-10-22 公开文档已核对 |
| [OpenRouter 免费模型](https://openrouter.ai/models?max_price=0) | 官方免费层 | 免费模型 20 RPM、50 请求/日；账户累计购买至少 $10 额度后上限可至 1,000 请求/日。 | [官方来源](https://openrouter.ai/pricing) | 2026-10-22 公开文档已核对 |
| [GroqCloud 免费计划](https://console.groq.com/) | 官方免费层 | openai/gpt-oss-20b：30 RPM、1,000 RPD、8,000 TPM（官方 Free Plan 示例）。 | [官方来源](https://console.groq.com/docs/rate-limits) | 2026-10-22 公开文档已核对 |
| [Cloudflare Workers AI](https://dash.cloudflare.com/) | 官方免费层 | 每天免费 10,000 Neurons；不是每天 10,000 次请求。 | [官方来源](https://developers.cloudflare.com/workers-ai/platform/pricing/) | 2026-10-22 公开文档已核对 |
| [硅基流动 SiliconFlow](https://cloud.siliconflow.cn/) | 部分模型免费 | 公开价格页：tencent/Hunyuan-MT-7B、BAAI/bge-m3 等指定模型标记“免费”。 | [官方来源](https://siliconflow.cn/pricing) | 2026-10-22 公开文档已核对 |
| [阿里云百炼 / Qwen](https://bailian.console.aliyun.com/) | 试用 / 新人额度 | 新人各模型通常赠送 100 万 Token，限华北2（北京）地域，通常 90 天有效；以模型详情为准。 | [官方来源](https://help.aliyun.com/zh/model-studio/new-free-quota) | 2026-10-22 公开文档已核对 |
| [Cohere Evaluation API](https://dashboard.cohere.com/) | 试用 / 新人额度 | Evaluation Key 免费测试；试用密钥每月合计限制 1,000 次 API 调用。 | [官方来源](https://docs.cohere.com/v2/docs/rate-limits) | 2026-10-22 公开文档已核对 |
| [Cerebras Inference](https://cloud.cerebras.ai/) | 试用 / 新人额度 | 官方宣传：提供有效支付方式可得一次性 $5 试用金，激活后 30 天失效。 | [官方来源](https://www.cerebras.ai/pricing) | 2026-10-22 公开文档已核对 |
| [Hugging Face Inference Providers](https://huggingface.co/) | 无普适免费额度 | 官网现行政策：普通 Free 用户每月赠送积分为 0；PRO 订阅包含每月 $2 计算额度。 | [官方来源](https://huggingface.co/docs/inference-providers/pricing) | 2026-10-22 公开文档已核对 |
| [DeepSeek 官方 API](https://platform.deepseek.com/) | 待核验 | 按模型价格表或实际账单计费；原“注册必送 500 万 Token”缺少持续适用的官方证据。 | [官方来源](https://api-docs.deepseek.com/quick_start/pricing) | 账号权益待核实 |
| [智谱 GLM API](https://open.bigmodel.cn/) | 待核验 | 部分历史活动或免费模型可能存在，暂无可统一适用的实时赠额核验结论。 | [官方来源](https://open.bigmodel.cn/) | 账号权益待核实 |
| [NVIDIA Build / NIM](https://build.nvidia.com/) | 待核验 | 可查看模型 API 试用；无法确认所有账号“免费一年、每天 5 万次”。 | [官方来源](https://build.nvidia.com/) | 账号权益待核实 |
| [OpenAI API](https://platform.openai.com/) | 待核验 | API 按独立计费账户管理；不保证所有新账号注册送 $5。 | [官方来源](https://platform.openai.com/docs/) | 账号权益待核实 |
| [Mistral API](https://console.mistral.ai/) | 待核验 | 官方有按模型的公开定价；免费试用资格请以当前账号 Console 为准。 | [官方来源](https://docs.mistral.ai/inference/pricing) | 账号权益待核实 |
| [Kimi / Moonshot API](https://platform.kimi.com/) | 待核验 | 官方价格随模型更新；旧“注册送 15 元”尚未找到可长期适用的公开说明。 | [官方来源](https://platform.kimi.com/) | 账号权益待核实 |
| [xAI Grok API](https://console.x.ai/) | 待核验 | 账户赠金和活动资格需以当前官方 Console 为准。 | [官方来源](https://docs.x.ai/) | 账号权益待核实 |
<!-- FREETOKEN_TABLE_END -->

> 数据解释：**官方免费层**＝官方公布的指定 API / 模型免费层；**试用**＝限额体验金或测试密钥；**按模型区分**＝有免费模型也有付费模型；**待复核**＝不能在缺乏现行公开证据时声称免费。详细的领取步骤、限制和搜索过滤请打开 [FreeToken 网站](https://aipmandy.github.io/FreeToken/)。

## 更多免费 API 开源项目 / 云服务 / 数据服务

原版收集的 **GitHub 免费 API 项目、Claude/Grok/Kimi、AWS、Azure、Google Cloud、GitHub Copilot、NewsAPI、OpenWeather、Alpha Vantage** 等资源已整理成独立的 [扩展目录（含安全与证据边界）](CATALOG.md)，也可浏览 [网页版生态目录](https://aipmandy.github.io/FreeToken/ecosystem.html)。这些候选项目不等于现行可用的免费 API Token。原始历史资料另见 [2026-06-21 旧版](https://github.com/AIPMAndy/FreeToken/blob/daf796ce49bdaf7e1d70c0085f8b36f5a8909b89/README.md)。

## 2026-10-22 最新政策重要变化

- **Hugging Face Inference Providers**：Free 账户已无每月赠送计算积分；原文的 $0.10/月已撤回。PRO/Team 的 $2/月与订阅付费关联，并非 Free 用户福利。详见 [官方说明](https://huggingface.co/docs/inference-providers/pricing)。
- **阿里云百炼 / Qwen**：首次开通的北京地域用户可获得按模型划分的新人免费额度，通常 100 万 Token / 模型、有效期 90 天。已实名用户请务必启用“免费额度用完即停”。详见 [官方规则](https://help.aliyun.com/zh/model-studio/new-free-quota)。
- **Cerebras**：官方注明提供有效支付方式可获一次性 $5 / 30 天试用金，属于促销活动，需核实资格。详见 [官方定价](https://www.cerebras.ai/pricing)。
- **硅基流动**：例如 `tencent/Hunyuan-MT-7B`、`BAAI/bge-m3` 在公开价格页标注“免费”；其他型号可能收费。详见 [官方价格表](https://siliconflow.cn/pricing)。
- **OpenRouter、Groq、Cloudflare**：分别按日请求数、模型维度 RPM/RPD、Neurons 计量，不能将其混为“免费无限次”。

## 怎么选平台

| 你的目标 | 优先研究 | 不要忽略 |
|---|---|---|
| 0 成本调用主流 LLM | [Google Gemini](https://ai.google.dev/gemini-api/docs/pricing) / [OpenRouter :free](https://openrouter.ai/pricing) | 查看当下模型及账号的限制 |
| 极低延迟推理 | [Groq](https://console.groq.com/docs/rate-limits) | 限速按模型区分，不宜当 SLA |
| 边缘 AI 应用 | [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/platform/pricing/) | 免费单位是 Neurons，不是 API 请求 |
| 少量模型试验 | [Hugging Face](https://huggingface.co/docs/inference-providers/pricing) / [Cohere](https://docs.cohere.com/v2/docs/rate-limits) | 体验金与评估密钥不等于生产免费 |
| 国内模型 | [硅基流动](https://siliconflow.cn/pricing) / [阿里云百炼](https://help.aliyun.com/zh/model-studio/) | 必须核对具体模型、资格和收费区间 |

## 5 分钟上手

1. 打开 [查询网站](https://aipmandy.github.io/FreeToken/)，筛选“官方免费层”，再核对对应服务商的官方来源。
2. 用自己的账号在服务商控制台创建 API Key，不要从聊天群或非官方渠道购买共享 Key。
3. 复制 **当前免费模型的准确 ID**。例如 OpenRouter 需按模型目录的 `:free` 标识选择。
4. 本地环境变量保存 Key，先发送少量请求，检查余额、429 限速和响应质量。
5. 正式服务必须准备超额预算、备选模型、熔断和告警。

### OpenRouter 调用示例

```bash
export OPENROUTER_API_KEY="从官方后台取得的密钥"
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"YOUR_CURRENT_FREE_MODEL_ID","messages":[{"role":"user","content":"你好"}]}'
```

把 `YOUR_CURRENT_FREE_MODEL_ID` 换成 **官方模型目录现有** 的 `:free` 模型 ID，示例没有提供真实密钥。

## 免费额度的常见误解

- **“Hugging Face Free 每月赠送 $0.10”**：已不适用；官方 Free 用户当前没有每月赠送积分。
- **“阿里云百炼免费额度永不过期”**：错；目前新人额度通常 90 天且仅北京地域适用，已实名用户可能自动按量付费。
- **“硅基流动所有 API 免费”**：错；只针对公开价格标为“免费”的模型，核对模型 ID 与 Pro 版本。

- **“注册送 $5 OpenAI API”**：无法作为适用于所有新账号的长期承诺；具体以 Platform Billing 为准。
- **“DeepSeek 注册送 500 万 Tokens”**：原文没有可靠的现行官方证据，已撤回固定数字。
- **“NVIDIA H100 免费一年 / 一天 5 万次”**：原文存在把平台试用与实际硬件能力混为一谈的问题，已撤回。
- **“小米 MiMo 100T 活动还能报名”**：原条目明确写活动到 2026-05-28，本轮不再当作有效领取渠道。
- **“Cloudflare 每天 10,000 次免费请求”**：实际官方计量为 **10,000 Neurons/日**，不同模型折算的请求数不同。
- **“Gemini 免费 200 万 Tokens / 日”**：不是适用于全部免费模型的统一固定限额；应该查看个人 AI Studio 的 RPM、TPM、RPD。
- **“GitHub 反向代理 = 官方免费 API”**：第三方代理可能存在账号、密钥、隐私和服务条款风险，不纳入“官方已核对”推荐。
- **“网页聊天永久免费，所以 API 也永久免费”**：这是两个不同产品和计费体系。

## 安全与成本

- **不要**在仓库、前端网站、Issue、客服聊天、截图中粘贴真实 Token。
- 使用环境变量、最小权限、调用日志脱敏、额度预警；泄露后立即撤销并更换。
- 对第三方网关进行独立安全审计；尤其不要交付主账号 Cookie、长期刷新令牌。
- 对提供商的免费服务条款、地区限制、数据使用政策和生产用途限制进行核对。
- 对 429 限流使用退避重试，不通过多账号批量注册规避限制。

## 数据与自动审核

- [data/providers.json](data/providers.json) 是结构化资源台账，保存分类、官方文档、核验范围和日期。
- [scripts/verify.py](scripts/verify.py) 自动检查台账、README、HTML 卡片、网站地图及过期宣传用语的一致性。
- [AUDIT.md](AUDIT.md) 保留对抗式审查报告及残余风险；新增信息需要同时更新网站和台账。

## 贡献和纠错

本项目接受可靠来源的 PR，请看 [CONTRIBUTING.md](CONTRIBUTING.md)。最低标准包括 **官方网址、额度类型、核验日期、适用条件、有效期、是否需要支付方式**。过期活动将标注失效而非继续宣传。反馈问题请 [提交 Issue](https://github.com/AIPMAndy/FreeToken/issues)。

项目的搜索网站是零追踪静态页面，包含 [robots.txt](robots.txt)、[sitemap.xml](sitemap.xml) 与结构化数据。发布请参阅 [DEPLOY.md](DEPLOY.md)。

## 常见问题 FAQ

### 有哪些免费的大模型 API 可以用？

资源总表列出 Google Gemini API、OpenRouter 免费模型、GroqCloud 免费计划、Cloudflare Workers AI、硅基流动部分免费模型等官方免费层，以及阿里云百炼、Cohere、Cerebras 等试用额度；DeepSeek、智谱 GLM、Kimi、OpenAI 等标为待核验。每条附官方来源，最近一次复核为 2026-10-22。

### 免费网页聊天就等于免费 API 吗？

不是。免费网页聊天 ≠ 免费 API，试用体验金 ≠ 永久免费；免费策略会因账号、国家/地区、模型和计费方式变化。

### FreeToken 会提供共享的 API Key 吗？

不会。本项目不分发共享 API Key，也不保证任何固定权益长期有效。

### 在哪里搜索免费额度和领取步骤？

打开 [FreeToken 网站](https://aipmandy.github.io/FreeToken/)；更多免费 API 开源项目和云服务见 [CATALOG.md](CATALOG.md)。

## 作者与联系

**AI 酋长 Andy** · AI 产品、AI 应用落地和咨询陪跑。

- 官网：[metaver.vip](https://metaver.vip/)
- 微信：**`AIPMAndy`**（添加时备注 FreeToken）
- 开源主页：[AIPMAndy](https://github.com/AIPMAndy)
- 资源查询：[FreeToken GitHub Pages](https://aipmandy.github.io/FreeToken/)

**MIT License · 本项目仅整理信息，不销售、不托管、不代领任何 API Key。**

> ⭐ 如果对你有用，欢迎给仓库 Star；如果发现额度失效，欢迎提交带来源的纠错。
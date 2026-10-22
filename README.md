# 🎁 FreeToken｜免费 AI API Token 获取指南（2026）

> Free AI API Keys / Tokens / Free Tier / LLM API Directory · 面向中文开发者的开源免费额度导航。

**官方网站：[FreeToken 可搜索资源库](https://aipmandy.github.io/FreeToken/)** · **作者：[AI酋长Andy](https://metaver.vip/)** · **微信：`AIPMAndy`（备注 FreeToken）**

收集 **Gemini、OpenRouter、Groq、Cloudflare Workers AI、Hugging Face、Cohere、DeepSeek、Qwen、智谱 GLM、NVIDIA、硅基流动** 等平台的 AI API 获取方式。每条说明免费资格、申请入口、官方来源、限制和核验日期。

> ⚠️ **免费网页聊天 ≠ 免费 API。试用体验金 ≠ 永久免费。** 免费策略会因账号、国家/地区、模型、计费方式而变化。本站绝不分发共享 API Key，也不保证任何固定权益长期有效。

**本次重审：2026-10-22。** “官方文档已核对”表示核验了公开说明，**不代表已登录不同地区账号实测额度**。本次未能证实的赠额已降级为待核验，历史活动不继续宣传。

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

| 平台 | 类型 | 官方公布的免费权益 / 提示 | 核验来源 | 状态 |
|---|---|---|---|---|
| [Google Gemini API](https://aistudio.google.com/) | 官方免费层 | 部分模型输入/输出免费；RPM / TPM / RPD 以 AI Studio 当前限额为准。 | [官方资料](https://ai.google.dev/gemini-api/docs/rate-limits) | 2026-10-22 公开资料核验 |
| [OpenRouter 免费模型](https://openrouter.ai/models?max_price=0) | 官方免费层 | 当前公开说明：未累计购买 $10 额度时，20 RPM、50 请求/日；累计购买达 $10 后可到 1,000 请求/日。 | [官方资料](https://openrouter.ai/docs/api-reference/limits) | 2026-10-22 公开资料核验 |
| [GroqCloud](https://console.groq.com/) | 官方免费层 | 例如官方当前列出 openai/gpt-oss-20b：30 RPM、1,000 RPD；其他模型不同。 | [官方资料](https://console.groq.com/docs/rate-limits) | 2026-10-22 公开资料核验 |
| [Cloudflare Workers AI](https://dash.cloudflare.com/) | 官方免费层 | 10,000 Neurons / 日（不是 10,000 次请求）。 | [官方资料](https://developers.cloudflare.com/workers-ai/platform/pricing/) | 2026-10-22 公开资料核验 |
| [Hugging Face Inference Providers](https://huggingface.co/settings/tokens) | 试用 / 免费体验金 | 普通 Free 用户 $0.10 / 月（官方注明可能变化）。 | [官方资料](https://huggingface.co/docs/inference-providers/pricing) | 2026-10-22 公开资料核验 |
| [Cohere Evaluation API](https://dashboard.cohere.com/) | 试用 / 免费体验金 | 试用密钥总体限制 1,000 API 调用/月；不同端点另有速率限制。 | [官方资料](https://docs.cohere.com/v2/docs/rate-limits) | 2026-10-22 公开资料核验 |
| [硅基流动 SiliconFlow](https://cloud.siliconflow.cn/) | 按模型区分 | 按当前选定模型的输入/输出价格为准；不要把全站当免费。 | [官方资料](https://siliconflow.cn/pricing) | 2026-10-22 公开资料核验 |
| [阿里云百炼 / Qwen](https://bailian.console.aliyun.com/) | 需复核具体额度 | 不公布未经本轮确认的固定免费 Token 数量。 | [官方资料](https://help.aliyun.com/zh/model-studio/) | 待复核 |
| [DeepSeek API](https://platform.deepseek.com/) | 需复核具体额度 | 注册活动及余额以平台实际展示为准。 | [官方资料](https://api-docs.deepseek.com/quick_start/pricing) | 待复核 |
| [智谱 GLM 开放平台](https://open.bigmodel.cn/) | 需复核具体额度 | 未核实长期赠额；按官方控制台显示为准。 | [官方资料](https://open.bigmodel.cn/) | 待复核 |
| [NVIDIA Build API Catalog](https://build.nvidia.com/) | 需复核具体额度 | 不再承诺“100+ 模型免费用一年”“H100 每天五万次”。 | [官方资料](https://build.nvidia.com/) | 待复核 |
| [OpenAI API](https://platform.openai.com/) | 需复核具体额度 | 不能把“新用户必送 $5”作为现行统一政策。 | [官方资料](https://platform.openai.com/docs/) | 待复核 |
| [Mistral API](https://console.mistral.ai/) | 需复核具体额度 | 具体额度及账单要求以官方 Console 为准。 | [官方资料](https://docs.mistral.ai/) | 待复核 |

> 数据解释：**官方免费层**＝官方公布的指定 API / 模型免费层；**试用**＝限额体验金或测试密钥；**按模型区分**＝有免费模型也有付费模型；**待复核**＝不能在缺乏现行公开证据时声称免费。详细的领取步骤、限制和搜索过滤请打开 [FreeToken 网站](https://aipmandy.github.io/FreeToken/)。

## 更多免费 API 开源项目 / 云服务 / 数据服务

原版收集的 **GitHub 免费 API 项目、Claude/Grok/Kimi、AWS、Azure、Google Cloud、GitHub Copilot、NewsAPI、OpenWeather、Alpha Vantage** 等资源已整理成独立的 [扩展目录（含安全与证据边界）](CATALOG.md)，也可浏览 [网页版生态目录](https://aipmandy.github.io/FreeToken/ecosystem.html)。这些候选项目不等于现行可用的免费 API Token。原始历史资料另见 [2026-06-21 旧版](https://github.com/AIPMAndy/FreeToken/blob/daf796ce49bdaf7e1d70c0085f8b36f5a8909b89/README.md)。

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

## 贡献和纠错

本项目接受可靠来源的 PR，请看 [CONTRIBUTING.md](CONTRIBUTING.md)。最低标准包括 **官方网址、额度类型、核验日期、适用条件、有效期、是否需要支付方式**。过期活动将标注失效而非继续宣传。反馈问题请 [提交 Issue](https://github.com/AIPMAndy/FreeToken/issues)。

项目的搜索网站是零追踪静态页面，包含 [robots.txt](robots.txt)、[sitemap.xml](sitemap.xml) 与结构化数据。发布请参阅 [DEPLOY.md](DEPLOY.md)。

## 作者与联系

**AI 酋长 Andy** · AI 产品、AI 应用落地和咨询陪跑。

- 官网：[metaver.vip](https://metaver.vip/)
- 微信：**`AIPMAndy`**（添加时备注 FreeToken）
- 开源主页：[AIPMAndy](https://github.com/AIPMAndy)
- 资源查询：[FreeToken GitHub Pages](https://aipmandy.github.io/FreeToken/)

**MIT License · 本项目仅整理信息，不销售、不托管、不代领任何 API Key。**

> ⭐ 如果对你有用，欢迎给仓库 Star；如果发现额度失效，欢迎提交带来源的纠错。
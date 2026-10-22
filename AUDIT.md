# 2026-10-22 对抗式审核记录

## 审核边界

本轮以官方公开定价、速率限制、免费规则为证据，**未登录用户账号**，未取得真实 API Key 测试；“资料已核对”不是“本人已领取且可以调用”的承诺。保留项目名 `FreeToken`、GitHub 仓库和当前静态站 URL，避免不必要的 SEO 地址迁移。

## 事实核对：已修正

| 对抗假设 | 查证结果 | 改动 |
|---|---|---|
| Hugging Face Free 月送 $0.10 | 官方现行定价为 Free 用户每月无包含积分 | 改为「无普适免费额度」，新增纠错指南 |
| 阿里云百炼只是模糊的“可能送” | 官方明确北京地域新人模型额度、90 天及用完即停规则 | 晋级为经公开资料核对的试用资源，并增加领取步骤 |
| Cerebras 可以永久免费 | 官方推广为需支付方式、一次性 $5、30 天 | 标记限期试用，注明信用卡要求 |
| 所有硅基流动模型免费 | 官方价格页只有部分具体模型标免费 | 示例精确到型号，保留按模型区分标签 |
| Cloudflare 每日 1 万请求 | 实际每日 10,000 Neurons，部分模型另需付费计划 | 显示实际计费单位 |
| Groq 全模型每天 14,400 请求 | 免费限额按模型变化，举例 gpt-oss-20b 为 30 RPM / 1,000 RPD | 不做全平台统一数字保证 |
| Gemini 全平台免费 | 部分模型有免费层，速率按项目及模型，需 AI Studio 查看 | 取消“统一 200 万 Token/日” |
| 反向代理 = 官方永久免费 | 无法等价，可能涉及隐私、账号和服务条款 | 与官方免费层分开在扩展目录 |

## 对抗式角色

1. **新手视角**：明确区分 Free API、试用、按模型、待核验与无免费额度；新增中文领取教程。
2. **审计视角**：每个已核对条目必须具备官方公开来源和日期；不以二手帖子替代。
3. **开发者视角**：保留准确的单位、限额与模型 ID；用代码质量门禁确保 README 和网站一致。
4. **安全视角**：不收集 Token、不托管共享 API Key；建议环境变量、限额、轮换和失败降级。
5. **搜索引擎视角**：不改旧首页 URL，使用 canonical、robots、sitemap、静态渲染实体内容；教程回答不同的真实搜索意图。
6. **商业视角**：保留官网和微信作为次级 CTA，优先满足资源查询，不强制跳转、不弹窗逼单。

## 风险与下一轮必要检查

- GitHub Actions 不能在缺少 Pages 配置时自动启用站点。需要有权限的仓库所有者在 Settings → Pages 选 GitHub Actions。
- 无百度、Bing 站长平台真实搜索词数据；暂不能评估 CTR 或排名变化。
- 官方政策变化快，需要以官方定价为准；核验日期不得自动伪装为“今天”，必须人工确认后更新。
- 所有卡片为**静态预渲染**，没有向第三方发送 API Key 的操作。
- 浏览器侧筛选的人工视觉验收，以及线上 HTTP/交互验收要等 Pages 成功部署后执行。

## 来源总索引

- Google Gemini：https://ai.google.dev/gemini-api/docs/pricing
- OpenRouter：https://openrouter.ai/pricing
- Groq：https://console.groq.com/docs/rate-limits
- Cloudflare：https://developers.cloudflare.com/workers-ai/platform/pricing/
- SiliconFlow：https://siliconflow.cn/pricing
- 阿里云百炼：https://help.aliyun.com/zh/model-studio/new-free-quota
- Cohere：https://docs.cohere.com/v2/docs/rate-limits
- Cerebras：https://www.cerebras.ai/pricing
- Hugging Face：https://huggingface.co/docs/inference-providers/pricing

最后人工核验：2026-10-22。
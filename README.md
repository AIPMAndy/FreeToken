# 🎁 FreeToken

收集各种免费 API Token 的获取方法和使用指南。

## 📋 目录

- [AI 模型](#ai-模型)
- [云服务](#云服务)
- [开发工具](#开发工具)
- [数据服务](#数据服务)
- [其他服务](#其他服务)

---

## 🤖 AI 模型

### OpenAI
- **免费额度**: 新用户注册送 $5 体验金（有效期 3 个月）
- **获取方式**: 
  1. 访问 [OpenAI Platform](https://platform.openai.com/)
  2. 注册账号并验证手机号
  3. 在 API Keys 页面创建密钥
- **限制**: 每分钟 3 次请求，每天 200 次请求
- **文档**: https://platform.openai.com/docs

### Anthropic Claude
- **免费额度**: 新用户注册送 $5 体验金
- **获取方式**:
  1. 访问 [Anthropic Console](https://console.anthropic.com/)
  2. 注册账号
  3. 创建 API Key
- **限制**: 根据模型不同有不同的速率限制
- **文档**: https://docs.anthropic.com/

### Google Gemini
- **免费额度**: 每分钟 60 次请求（免费层）
- **获取方式**:
  1. 访问 [Google AI Studio](https://makersuite.google.com/)
  2. 使用 Google 账号登录
  3. 获取 API Key
- **限制**: 免费层有速率限制
- **文档**: https://ai.google.dev/docs

### Cohere
- **免费额度**: 每月 100 次 API 调用（试用版）
- **获取方式**:
  1. 访问 [Cohere Dashboard](https://dashboard.cohere.com/)
  2. 注册账号
  3. 创建 API Key
- **文档**: https://docs.cohere.com/

---

## ☁️ 云服务

### AWS
- **免费额度**: 12 个月免费套餐 + 永久免费服务
- **获取方式**:
  1. 注册 [AWS 账号](https://aws.amazon.com/free/)
  2. 在 IAM 中创建用户和访问密钥
- **限制**: 不同服务有不同的免费额度
- **文档**: https://docs.aws.amazon.com/

### Google Cloud
- **免费额度**: $300 体验金（90 天）+ 永久免费层
- **获取方式**:
  1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
  2. 创建项目
  3. 启用 API 并创建凭据
- **文档**: https://cloud.google.com/docs

### Azure
- **免费额度**: $200 体验金（30 天）+ 12 个月免费服务
- **获取方式**:
  1. 注册 [Azure 账号](https://azure.microsoft.com/free/)
  2. 创建资源并获取密钥
- **文档**: https://docs.microsoft.com/azure/

---

## 🛠️ 开发工具

### GitHub
- **免费额度**: 公开仓库无限，私有仓库 2000 分钟 CI/CD
- **获取方式**:
  1. 访问 [GitHub Settings](https://github.com/settings/tokens)
  2. 生成 Personal Access Token
- **文档**: https://docs.github.com/

### Vercel
- **免费额度**: 个人项目免费部署
- **获取方式**:
  1. 访问 [Vercel Dashboard](https://vercel.com/dashboard)
  2. 在 Settings → Tokens 创建
- **文档**: https://vercel.com/docs

### Netlify
- **免费额度**: 每月 100GB 带宽，300 分钟构建时间
- **获取方式**:
  1. 访问 [Netlify Dashboard](https://app.netlify.com/)
  2. 在 User Settings → Applications 创建
- **文档**: https://docs.netlify.com/

---

## 📊 数据服务

### RapidAPI
- **免费额度**: 大部分 API 有免费层
- **获取方式**:
  1. 注册 [RapidAPI](https://rapidapi.com/)
  2. 订阅免费 API
  3. 在 Dashboard 获取密钥
- **文档**: https://docs.rapidapi.com/

### NewsAPI
- **免费额度**: 每天 100 次请求
- **获取方式**:
  1. 访问 [NewsAPI](https://newsapi.org/)
  2. 注册并获取 API Key
- **文档**: https://newsapi.org/docs

### OpenWeatherMap
- **免费额度**: 每分钟 60 次调用
- **获取方式**:
  1. 注册 [OpenWeatherMap](https://openweathermap.org/api)
  2. 在 API Keys 页面获取
- **文档**: https://openweathermap.org/api

---

## 🎯 其他服务

### Twilio
- **免费额度**: 试用账号送 $15.50
- **获取方式**:
  1. 注册 [Twilio](https://www.twilio.com/try-twilio)
  2. 在 Console 获取 Account SID 和 Auth Token
- **文档**: https://www.twilio.com/docs

### SendGrid
- **免费额度**: 每天 100 封邮件
- **获取方式**:
  1. 注册 [SendGrid](https://sendgrid.com/)
  2. 创建 API Key
- **文档**: https://docs.sendgrid.com/

### Stripe
- **免费额度**: 测试模式无限制
- **获取方式**:
  1. 注册 [Stripe](https://stripe.com/)
  2. 在 Developers → API Keys 获取
- **文档**: https://stripe.com/docs

---

## 📝 使用建议

1. **安全第一**: 永远不要在公开代码中硬编码 Token
2. **环境变量**: 使用 `.env` 文件存储密钥
3. **权限最小化**: 只授予必要的权限
4. **定期轮换**: 定期更换 API 密钥
5. **监控使用**: 关注免费额度使用情况

## 🔒 安全提示

```bash
# 使用 .gitignore 忽略敏感文件
echo ".env" >> .gitignore
echo "*.key" >> .gitignore
echo "config.json" >> .gitignore
```

## 🤝 贡献

欢迎提交 PR 添加更多免费 Token 获取方法！

### 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/new-token`)
3. 提交更改 (`git commit -m 'Add new token source'`)
4. 推送到分支 (`git push origin feature/new-token`)
5. 创建 Pull Request

## 📄 许可证

MIT License

## ⚠️ 免责声明

本项目仅供学习交流使用，请遵守各服务商的使用条款。滥用 API 可能导致账号被封禁。

---

**Star ⭐ 这个项目如果对你有帮助！**

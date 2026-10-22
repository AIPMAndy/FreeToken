# 发布、SEO 与验收 · FreeToken

## GitHub Pages

推荐网址：https://aipmandy.github.io/FreeToken/（保留仓库名 FreeToken，不迁移、不更改现有 GitHub 搜索入口）。

**发布方式 A：GitHub Actions**。在仓库 Settings → Pages → Build and deployment → Source 选择 GitHub Actions。仓库已包含 `.github/workflows/pages.yml`，推送 main 时上传根目录静态网站并部署。

**发布方式 B：Deploy from a branch**。如使用分支发布，选择 main / (root)。根目录已经包含 `index.html`、`.nojekyll`、`robots.txt`、`sitemap.xml`。两种模式择一即可，不要重复配置。

本仓库无需构建命令，也无外部 npm/CDN 依赖。

## 百度 / Bing 搜索保全

- 保留原地址与仓库名，避免改变已经自然获得点击的链接。
- 网站只设一个 canonical：`https://aipmandy.github.io/FreeToken/`，robots 和 sitemap 均指向该路径。
- 不采用“自动跳转到官网”的方式消耗用户信任；网站 CTA 只在用户获得信息后出现。
- 站点地图：https://aipmandy.github.io/FreeToken/sitemap.xml
- Bing Webmaster Tools / 百度搜索资源平台需要站长本人验证网站所有权；提交 sitemap 不代表立即收录。
- 如已有特定关键词页的点击数据，使用搜索引擎平台按落地页/查询词/CTR 分析后再扩展页面，不编造排名。
- GitHub 仓库页面和 GitHub Pages 是两个独立入口；SEO 不保证流量增长。

## 验收步骤

1. 打开 `https://aipmandy.github.io/FreeToken/` 并检查 HTTP 200 与页面主体可见；404 先检查 Pages 设置及 Actions 日志。
2. 验证电脑版 / 手机宽度下卡片不横向溢出，搜索“DeepSeek”“Gemini”及筛选“待复核”能正确工作。
3. 在无 JS 时也能看到完整 HTML 资源卡片、FAQ 和官方链接（爬虫可直接读取）。
4. 检查 `robots.txt` 和 `sitemap.xml` 可访问，HTML `canonical` 精确一致。
5. 在 Bing Webmaster Tools 查看站点地图、索引页、搜索词与点击数据，再考虑进一步 SEO。
6. 验证用户点击官网到 `https://metaver.vip/`；点击复制微信可取得 `AIPMAndy`。
7. 复查官方定价、额度、限速：所有带“官方已核对”卡片要有来源且核验日期真实。
8. 每 30 天重审高频项目，不因时间推移自动刷新核验日期。

## 本轮已知限制

- 没有接入百度、Bing 的站长平台，因此**未**查看真实关键词、索引覆盖率和点击数据。
- “核对官方公开资料”不是以真实用户账号进行了 API 请求或各地区实名注册。
- 发布需要仓库 Pages 已启用；GitHub 文件提交成功不等于网站已上线。

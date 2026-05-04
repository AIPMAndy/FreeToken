# 贡献指南

感谢你考虑为 FreeToken 做出贡献！

## 如何贡献

### 添加新的 Token 来源

当你发现新的免费 Token 来源时，请按照以下格式添加到 README.md：

```markdown
### 服务名称
- **免费额度**: 描述免费额度
- **获取方式**: 
  1. 步骤一
  2. 步骤二
  3. 步骤三
- **限制**: 描述使用限制
- **文档**: 官方文档链接
```

### 提交流程

1. **Fork 仓库**
   ```bash
   # 在 GitHub 上点击 Fork 按钮
   ```

2. **克隆到本地**
   ```bash
   git clone https://github.com/你的用户名/FreeToken.git
   cd FreeToken
   ```

3. **创建分支**
   ```bash
   git checkout -b feature/add-xxx-token
   ```

4. **进行修改**
   - 编辑 README.md
   - 确保格式一致
   - 验证链接有效

5. **提交更改**
   ```bash
   git add .
   git commit -m "Add XXX token获取方法"
   ```

6. **推送到 GitHub**
   ```bash
   git push origin feature/add-xxx-token
   ```

7. **创建 Pull Request**
   - 在 GitHub 上创建 PR
   - 描述你添加的内容
   - 等待审核

## 内容要求

### ✅ 应该包含

- 真实有效的免费 Token 获取方法
- 清晰的步骤说明
- 官方文档链接
- 免费额度和限制说明

### ❌ 不应该包含

- 需要付费的服务（除非有免费试用）
- 违反服务条款的获取方法
- 非法或灰色地带的方法
- 实际的 Token 值（只提供获取方法）

## 代码规范

- 使用清晰的中文描述
- 保持 Markdown 格式整洁
- 链接使用 HTTPS
- 按字母顺序或分类组织

## 问题反馈

如果你发现：
- 某个 Token 获取方法失效
- 文档链接失效
- 信息过时

请创建 Issue 说明情况。

## 行为准则

- 尊重他人
- 保持友善
- 遵守开源精神
- 不传播恶意内容

---

再次感谢你的贡献！🎉

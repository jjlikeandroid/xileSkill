# 贡献指南

感谢您对 xileSkills 的关注！我们欢迎任何形式的贡献。

## 如何贡献

### 报告问题

如果您发现了 bug 或有功能建议，请：

1. 检查 [Issues](https://github.com/jjlikeandroid/xileSkill/issues) 是否已有类似问题
2. 如果没有，请创建新的 Issue，使用我们的 [Issue 模板](https://github.com/jjlikeandroid/xileSkill/blob/master/.github/ISSUE_TEMPLATE.md)
3. 提供详细的信息，包括：
   - 环境信息（Python 版本、操作系统）
   - 复现步骤
   - 期望行为和实际行为
   - 相关截图或日志

### 提交代码

#### 开发流程

1. **Fork 仓库**
   ```bash
   # 在 GitHub 上点击 Fork 按钮
   ```

2. **克隆您的 Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/xileSkill.git
   cd xileSkill
   ```

3. **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **进行更改**
   - 遵循现有代码风格
   - 添加必要的注释
   - 确保代码通过测试

5. **提交更改**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

6. **推送到您的 Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **创建 Pull Request**
   - 在 GitHub 上创建 Pull Request
   - 填写 PR 模板
   - 等待审核

#### 代码规范

- **Python 版本**: Python 3.7+
- **代码风格**: 遵循 PEP 8
- **注释**: 使用中文注释
- **文档**: 更新相关文档

#### 提交信息格式

使用以下格式：

```
<type>: <subject>

<body>

<footer>
```

**类型（type）**:
- `Add`: 添加新功能
- `Fix`: 修复 bug
- `Update`: 更新功能
- `Refactor`: 重构代码
- `Docs`: 文档更新
- `Style`: 代码格式调整
- `Test`: 测试相关
- `Chore`: 构建/工具相关

**示例**:
```
Add: 支持自定义视觉风格

- 添加自定义风格配置文件
- 支持从 templates/custom/ 加载风格
- 更新文档说明

Closes #123
```

### 添加新功能

如果您想添加新功能，请先：

1. 创建 Issue 讨论您的想法
2. 等待维护者反馈
3. 开始实现

### 添加新风格

添加新的视觉风格：

1. 在 `xileSkills.py` 中添加新的 CSS 方法
2. 在 `get_style_config()` 中添加风格配置
3. 更新 `README.md` 中的风格列表
4. 在 `templates/STYLE_GUIDE.md` 中添加风格说明

**示例**:

```python
def get_elegant_css(self) -> str:
    """优雅风格 CSS"""
    return """
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: linear-gradient(135deg, #F3E8FF 0%, #D8B4FE 100%);
        margin: 0;
        padding: 20px;
    }
    .container {
        max-width: 1080px;
        margin: 0 auto;
    }
    .slide {
        background: #FFFFFF;
        border-radius: 24px;
        padding: 60px 40px;
        margin-bottom: 30px;
        box-shadow: 0 8px 30px rgba(139, 92, 246, 0.2);
    }
    .slide-content {
        position: relative;
    }
    .slide-number {
        position: absolute;
        top: 20px;
        right: 20px;
        background: #8B5CF6;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 600;
    }
    p {
        font-size: 24px;
        line-height: 1.8;
        color: #4A4A4A;
        margin-bottom: 16px;
    }
    """
```

### 测试

在提交代码前，请确保：

1. 代码能够正常运行
2. 没有语法错误
3. 功能符合预期
4. 文档已更新

```bash
# 运行测试
python xileSkills.py --help

# 测试基本功能
python xileSkills.py https://example.com --style cute
```

### 文档

更新文档时，请确保：

1. 使用清晰的中文
2. 提供完整的示例
3. 更新相关的 README 或文档文件
4. 保持文档与代码同步

## 开发环境设置

### 安装依赖

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/xileSkill.git
cd xileSkill

# 安装 Python 依赖（如果有）
pip install -r requirements.txt
```

### 运行测试

```bash
# 运行基本测试
python xileSkills.py --help

# 测试微信文章提取
python xileSkills.py https://mp.weixin.qq.com/s/xxxxx
```

### 代码检查

```bash
# 使用 flake8 检查代码风格
pip install flake8
flake8 xileSkills.py --max-line-length=100
```

## 社区准则

- 尊重所有贡献者
- 提供建设性的反馈
- 保持友好和专业
- 遵循开源许可证

## 许可证

通过贡献代码，您同意您的贡献将在 MIT 许可证下发布。

## 联系方式

- GitHub Issues: https://github.com/jjlikeandroid/xileSkill/issues
- Email: xile@skill.com

## 致谢

感谢所有贡献者！您的贡献让 xileSkills 变得更好。

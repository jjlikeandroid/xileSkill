# XileSkills

<div align="center">

![XileSkills Logo](https://img.shields.io/badge/XileSkills-v1.1.0-blue)
![Python](https://img.shields.io/badge/Python-3.7+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**将微信文章转换为小红书风格 PPT 的工具**

[功能特性](#-功能特性) • [快速开始](#-快速开始) • [使用示例](#-使用示例) • [贡献指南](#-贡献指南)

</div>

---

## 📖 简介

XileSkills 是一个强大的工具，可以将微信公众号文章转换为小红书风格的幻灯片页面。支持多种视觉风格、布局选项和输出格式，让内容创作更加简单高效。

### ✨ 核心功能

- 📱 **微信文章提取** - 自动从微信公众号文章链接提取内容
- 🎨 **小红书风格** - 5+ 种预设视觉风格，支持自定义
- 📊 **PPT 格式** - 生成精美的幻灯片页面
- 🎯 **智能分页** - 自动将长文章拆分为多页
- ✨ **视觉优化** - 卡片式布局、渐变背景、图标装饰
- 📁 **多种输出** - 支持 HTML、PDF、PNG 格式

---

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/jjlikeandroid/xileSkill.git
cd xileSkill

# 确保已安装 Python 3.7+
python --version
```

### 可选依赖

```bash
# 安装 wkhtmltopdf（用于 PDF 导出）
# Windows: https://wkhtmltopdf.org/downloads.html
# macOS: brew install wkhtmltopdf
# Linux: sudo apt-get install wkhtmltopdf
```

### 基础使用

```bash
# 从微信文章链接生成 PPT
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx
```

---

## 📚 使用示例

### 指定风格

```bash
# 可爱风格
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --style cute

# 清新风格
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --style fresh

# 温暖风格
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --style warm

# 简约风格
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --style minimal

# 知识风格
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --style notion
```

### 指定布局

```bash
# 稀疏布局（每页 1-2 个要点）
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --layout sparse

# 平衡布局（每页 3-4 个要点）
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --layout balanced

# 密集布局（每页 5-8 个要点）
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --layout dense
```

### 导出格式

```bash
# 导出为 HTML（默认）
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --format html

# 导出为 PDF
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --format pdf

# 导出为 PNG
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --format png
```

### 完整示例

```bash
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx \
  --style notion \
  --layout balanced \
  --format pdf \
  --output ./output
```

---

## 🎨 视觉风格

| 风格 | 配色 | 适用场景 |
|------|------|---------|
| **Cute** | 粉色、蓝色系 | 生活分享、美妆、美食 |
| **Fresh** | 绿色、蓝色系 | 健康、环保、旅行 |
| **Warm** | 橙色、黄色系 | 情感分享、生活故事 |
| **Minimal** | 黑白灰配色 | 专业内容、技术分享 |
| **Notion** | 蓝色、紫色系 | 干货知识、教程、科普 |

更多风格请查看 [视觉风格指南](.trae/skills/xileSkills/templates/STYLE_GUIDE.md)

---

## 📁 项目结构

```
xileSkill/
├── .github/
│   ├── workflows/
│   │   └── ci-cd.yml          # CI/CD 工作流
│   └── ISSUE_TEMPLATE.md      # Issue 模板
├── .trae/
│   └── skills/
│       └── xileSkills/
│           ├── SKILL.md        # Skill 定义
│           ├── xileSkills.py   # 主程序
│           ├── README.md       # 使用指南
│           └── templates/
│               └── STYLE_GUIDE.md  # 风格指南
├── CONTRIBUTING.md             # 贡献指南
└── README.md                  # 项目说明
```

---

## 🛠️ 开发

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/jjlikeandroid/xileSkill.git
cd xileSkill

# 运行测试
python .trae/skills/xileSkills/xileSkills.py --help
```

### 代码规范

- Python 版本：3.7+
- 代码风格：PEP 8
- 注释语言：中文

### 贡献

欢迎贡献！请查看 [贡献指南](CONTRIBUTING.md)

---

## 📖 文档

- [使用指南](.trae/skills/xileSkills/README.md) - 详细使用说明
- [视觉风格指南](.trae/skills/xileSkills/templates/STYLE_GUIDE.md) - 风格自定义
- [贡献指南](CONTRIBUTING.md) - 如何贡献代码

---

## 🤝 贡献者

感谢所有贡献者！

<a href="https://github.com/jjlikeandroid/xileSkill/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jjlikeandroid/xileSkill" />
</a>

---

## 📝 更新日志

### v1.1.0 (2026-04-01)
- ✅ 添加 GitHub Actions CI/CD 工作流
- ✅ 添加 Issues 模板
- ✅ 优化微信文章提取功能
- ✅ 添加 PDF/PNG 导出功能
- ✅ 添加视觉风格指南

### v1.0.0 (2026-04-01)
- ✅ 初始版本
- ✅ 支持微信文章提取
- ✅ 支持小红书风格 PPT 生成

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

感谢所有使用和贡献 XileSkills 的用户！

---

## 📮 联系方式

- GitHub Issues: https://github.com/jjlikeandroid/xileSkill/issues
- Email: xile@skill.com

---

<div align="center">

**如果觉得有用，请给个 ⭐ Star 支持一下！**

Made with ❤️ by XileSkills Team

</div>

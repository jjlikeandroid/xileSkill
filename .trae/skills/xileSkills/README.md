# XileSkills 使用指南

## 简介

XileSkills 是一个将微信文章转换为小红书风格 PPT 的工具。

## 安装

### 依赖要求
- Python 3.7+
- 无需额外依赖（使用标准库）

### 可选依赖
- **wkhtmltopdf**: 用于 PDF 导出（推荐）
- **wkhtmltoimage**: 用于 PNG 导出（推荐）

安装 wkhtmltopdf：
- Windows: https://wkhtmltopdf.org/downloads.html
- macOS: `brew install wkhtmltopdf`
- Linux: `sudo apt-get install wkhtmltopdf`

### 安装步骤

1. 确保已安装 Python 3.7 或更高版本
2. 技能文件已自动安装到 `.trae/skills/xileSkills/`

## 使用方法

### 基础用法

```bash
# 从微信文章链接生成 PPT
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx
```

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

### 指定输出

```bash
# 指定输出目录
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --output ./my-slides

# 指定每页字数
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --words-per-page 200
```

### 导出格式

```bash
# 导出为 HTML（默认）
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --format html

# 导出为 PDF（需要安装 wkhtmltopdf）
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --format pdf

# 导出为 PNG（需要安装 wkhtmltoimage）
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx --format png
```

### 组合使用

```bash
# 完整示例：指定风格、布局、输出格式和目录
python .trae/skills/xileSkills/xileSkills.py https://mp.weixin.qq.com/s/xxxxx \
  --style notion \
  --layout balanced \
  --format pdf \
  --output ./output
```

## 手动输入模式

如果无法从 URL 提取内容，可以使用手动输入模式：

```bash
python .trae/skills/xileSkills/xileSkills.py https://example.com
```

然后按照提示：
1. 输入文章内容（按 Ctrl+D 结束）
2. 输入文章标题

## 输出文件

生成的文件保存在指定的输出目录（默认：`./xhs-slides/`）：

- `{标题}.html` - 完整的 HTML 幻灯片文件
- `{标题}.pdf` - PDF 格式文件（需要 wkhtmltopdf）
- `{标题}.png` - PNG 图片文件（需要 wkhtmltoimage）

## 功能特点

### 📱 微信文章提取
- 自动从微信公众号文章链接提取内容
- 智能解析 HTML 结构
- 提取标题和正文内容
- 支持手动输入模式

### 🎨 视觉风格
- **Cute**（可爱）- 粉色、蓝色系，适合生活分享
- **Fresh**（清新）- 绿色、蓝色系，适合健康环保
- **Warm**（温暖）- 橙色、黄色系，适合情感分享
- **Minimal**（简约）- 黑白灰配色，适合专业内容
- **Notion**（知识）- 蓝色、紫色系，适合干货知识
- **自定义风格** - 支持创建自定义风格模板

### 📊 输出格式
- **HTML** - 网页格式，支持浏览器直接查看
- **PDF** - 文档格式，适合打印和分享
- **PNG** - 图片格式，适合社交媒体分享

### 🎯 布局选项
- **Sparse**（稀疏）- 每页 1-2 个要点
- **Balanced**（平衡）- 每页 3-4 个要点
- **Dense**（密集）- 每页 5-8 个要点

## 视觉风格预览

### Cute（可爱）
- 🎨 粉色、蓝色系
- 🌸 圆角卡片
- 💕 可爱图标

### Fresh（清新）
- 🌿 绿色、蓝色系
- 🌊 清新线条
- 🍃 自然元素

### Warm（温暖）
- 🌅 橙色、黄色系
- 🌄 温暖渐变
- 🌼 温馨图标

### Minimal（简约）
- ⬛ 黑白灰配色
- 📐 极简设计
- 🎯 大量留白

### Notion（知识）
- 📘 蓝色、紫色系
- 📝 知识卡片
- 🎓 清晰层次

## 常见问题

### Q: 无法提取微信文章
**A**: 部分微信文章可能有访问限制，请尝试：
1. 检查网络连接
2. 确认文章链接是否有效
3. 使用手动输入模式

### Q: 生成的幻灯片样式异常
**A**: 请确认：
1. 浏览器是否支持 CSS3
2. 字体是否正确加载
3. 尝试不同的风格选项

### Q: 如何自定义样式
**A**: 可以创建 `EXTEND.md` 文件来自定义默认样式：

```yaml
---
default_style: cute
default_layout: balanced
default_words_per_page: 300
---
```

## 技术支持

如有问题，请检查：
1. Python 版本是否 ≥ 3.7
2. 文件路径是否正确
3. 输入内容格式是否正确

## 更新日志

### v1.1.0 (2026-04-01)
- ✅ 添加 GitHub Actions CI/CD 工作流
- ✅ 添加 Issues 模板
- ✅ 优化微信文章提取功能
  - 自动解析 HTML 结构
  - 智能提取标题和内容
  - 支持手动输入模式
- ✅ 添加 PDF/PNG 导出功能
  - 支持 wkhtmltopdf 转换
  - 支持浏览器打印/截图
- ✅ 添加视觉风格指南
  - 10 种预设风格
  - 自定义风格支持
  - 颜色方案参考
  - 响应式设计

### v1.0.0 (2026-04-01)
- ✅ 初始版本
- ✅ 支持微信文章提取
- ✅ 支持小红书风格 PPT 生成
- ✅ 支持 5 种视觉风格
- ✅ 支持 3 种布局方式
- ✅ 支持手动输入模式

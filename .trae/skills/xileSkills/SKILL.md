---
name: xileSkills
description: Converts WeChat articles into Xiaohongshu-style PPT pages. Invoke when user provides a WeChat article link or asks to convert WeChat content to XHS-style slides.
---

# XileSkills - 微信文章转小红书 PPT

将微信文章转换为小红书风格的 PPT 页面，支持从微信文章链接提取内容并生成精美的幻灯片。

## 功能特点

- 📱 **微信文章提取**: 从微信公众号文章链接自动提取内容
- 🎨 **小红书风格**: 采用小红书风格的视觉设计
- 📊 **PPT 格式**: 生成幻灯片页面，适合展示和分享
- 🎯 **智能分页**: 自动将长文章拆分为多页幻灯片
- ✨ **视觉优化**: 卡片式布局、渐变背景、图标装饰
- 📁 **多种输出**: 支持 HTML、PDF、PNG 格式
- 🔧 **自动解析**: 智能解析 HTML 结构，提取标题和内容

## 使用方法

### 基础用法

```bash
# 从微信文章链接生成 PPT
xileSkills https://mp.weixin.qq.com/s/xxxxx

# 指定输出目录
xileSkills https://mp.weixin.qq.com/s/xxxxx --output ./slides
```

### 高级选项

```bash
# 指定风格
xileSkills https://mp.weixin.qq.com/s/xxxxx --style cute

# 指定布局
xileSkills https://mp.weixin.qq.com/s/xxxxx --layout balanced

# 指定每页字数
xileSkills https://mp.weixin.qq.com/s/xxxxx --words-per-page 300
```

## 选项说明

| 选项 | 说明 | 可选值 |
|------|------|--------|
| `--style` | 视觉风格 | `cute` (可爱), `fresh` (清新), `warm` (温暖), `minimal` (简约), `notion` (知识) |
| `--layout` | 布局方式 | `sparse` (稀疏), `balanced` (平衡), `dense` (密集) |
| `--words-per-page` | 每页字数 | 数字（默认：300） |
| `--output` | 输出目录 | 路径（默认：./xhs-slides） |
| `--format` | 输出格式 | `html` (网页), `pdf` (文档), `png` (图片) |

## 工作流程

1. **提取内容**: 从微信文章链接获取标题、正文、图片
2. **内容分析**: 分析文章结构、关键点、适合的展示方式
3. **页面规划**: 根据内容长度和结构规划幻灯片数量
4. **生成幻灯片**: 为每页生成 HTML 格式的幻灯片
5. **样式应用**: 应用小红书风格的视觉设计
6. **输出文件**: 生成可查看的幻灯片文件

## 输出格式

### HTML 格式（默认）
- 单个 HTML 文件包含所有幻灯片
- 支持浏览器直接查看
- 支持键盘导航（← → 键）
- 支持点击翻页

### PDF 格式
- 每页一个 PDF 文件
- 适合打印和分享
- 保持小红书风格

### PNG 格式
- 每页一个 PNG 图片
- 适合直接分享到小红书
- 高分辨率（1080x1440）

## 视觉风格

### Cute 风格（可爱）
- 柔和的粉色、蓝色系
- 圆角卡片
- 可爱图标装饰
- 适合：生活分享、美妆、美食

### Fresh 风格（清新）
- 清新的绿色、蓝色系
- 简约线条
- 自然元素装饰
- 适合：健康、环保、旅行

### Warm 风格（温暖）
- 温暖的橙色、黄色系
- 柔和渐变
- 温馨图标
- 适合：情感分享、生活故事

### Minimal 风格（简约）
- 黑白灰配色
- 极简设计
- 大量留白
- 适合：专业内容、技术分享

### Notion 风格（知识）
- 蓝色、紫色系
- 知识卡片布局
- 清晰层次
- 适合：干货知识、教程、科普

## 页面布局

### Sparse（稀疏）
- 每页 1-2 个要点
- 大字体、大图片
- 适合：封面、重点突出

### Balanced（平衡）
- 每页 3-4 个要点
- 中等字体、适中图片
- 适合：大多数内容

### Dense（密集）
- 每页 5-8 个要点
- 小字体、多信息
- 适合：干货知识、对比表格

## 使用示例

### 示例 1：基础转换
```bash
xileSkills https://mp.weixin.qq.com/s/LDYfKTDAFCJPi5YAiXYoBA
```

输出：
```
正在提取微信文章...
文章标题: Android 架构 15 年演进
文章字数: 2000 字
规划幻灯片: 8 页
正在生成幻灯片...
✓ 生成完成: ./xhs-slides/
  - 01-cover.html
  - 02-content-1.html
  - 03-content-2.html
  ...
  - 08-ending.html
```

### 示例 2：指定风格
```bash
xileSkills https://mp.weixin.qq.com/s/LDYfKTDAFCJPi5YAiXYoBA --style cute --layout balanced
```

### 示例 3：输出为 PNG
```bash
xileSkills https://mp.weixin.qq.com/s/LDYfKTDAFCJPi5YAiXYoBA --format png
```

## 技术实现

### 内容提取
- 使用 WebFetch 工具获取微信文章内容
- 解析 HTML 提取标题、正文、图片
- 处理 Markdown 格式

### 幻灯片生成
- 使用 HTML + CSS 生成幻灯片
- 响应式设计，支持不同屏幕
- CSS3 动画和过渡效果

### 样式系统
- 预设风格模板
- 可自定义颜色和布局
- 支持用户自定义样式

## 注意事项

1. **微信文章限制**: 部分微信文章可能有访问限制
2. **图片处理**: 微信文章中的图片会自动下载并引用
3. **字数统计**: 中文字符和英文单词分别统计
4. **分页逻辑**: 根据段落和标题自动分页
5. **网络依赖**: 需要网络连接才能提取微信文章

## 故障排除

### 问题：无法提取微信文章
**解决方案**:
- 检查网络连接
- 确认文章链接是否有效
- 尝试手动复制文章内容

### 问题：幻灯片样式异常
**解决方案**:
- 确认浏览器支持 CSS3
- 检查字体是否正确加载
- 尝试不同的风格选项

### 问题：输出格式不支持
**解决方案**:
- HTML 格式是默认格式，无需额外工具
- PDF 格式需要安装 wkhtmltopdf
- PNG 格式需要安装 puppeteer

## 扩展功能

### 自定义样式
创建 `EXTEND.md` 文件自定义默认样式：

```yaml
---
default_style: cute
default_layout: balanced
default_words_per_page: 300
custom_colors:
  primary: "#3B82F6"
  secondary: "#8B5CF6"
  background: "#F8FAFC"
---
```

### 自定义模板
在项目目录创建 `templates/` 目录，添加自定义模板：

```
templates/
  - custom-template.html
  - another-style.html
```

## 相关文件

- `EXTEND.md` - 自定义配置
- `templates/` - 自定义模板
- `output/` - 默认输出目录

## 版本历史

- **v1.0.0** (2026-04-01)
  - 初始版本
  - 支持微信文章提取
  - 支持小红书风格 PPT 生成
  - 支持 HTML/PDF/PNG 输出

## 许可证

MIT License

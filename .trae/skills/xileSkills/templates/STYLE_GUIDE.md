# XileSkills 视觉风格模板

## 风格列表

### 1. Cute（可爱）
- 🎨 配色：粉色、蓝色系
- 🌸 特点：圆角卡片、可爱图标
- 💕 适用：生活分享、美妆、美食

### 2. Fresh（清新）
- 🌿 配色：绿色、蓝色系
- 🌊 特点：清新线条、自然元素
- 🍃 适用：健康、环保、旅行

### 3. Warm（温暖）
- 🌅 配色：橙色、黄色系
- 🌄 特点：温暖渐变、温馨图标
- 🌼 适用：情感分享、生活故事

### 4. Minimal（简约）
- ⬛ 配色：黑白灰配色
- 📐 特点：极简设计、大量留白
- 🎯 适用：专业内容、技术分享

### 5. Notion（知识）
- 📘 配色：蓝色、紫色系
- 📝 特点：知识卡片、清晰层次
- 🎓 适用：干货知识、教程、科普

### 6. Elegant（优雅）
- 💎 配色：紫色、金色系
- ✨ 特点：精致设计、优雅字体
- 👗 适用：时尚、艺术、高端内容

### 7. Tech（科技）
- 🔵 配色：深蓝、青色系
- 💻 特点：科技感、未来感
- 🚀 适用：技术文章、科技新闻

### 8. Nature（自然）
- 🌲 配色：棕色、绿色系
- 🍂 特点：自然纹理、有机形状
- 🌱 适用：户外、环保、自然主题

### 9. Retro（复古）
- 🎞️ 配色：复古色调
- 📼 特点：复古滤镜、怀旧风格
- 🎵 适用：怀旧内容、复古风格

### 10. Neon（霓虹）
- 🌈 配色：霓虹色系
- 💡 特点：发光效果、高对比度
- 🎮 适用：游戏、潮流、年轻化内容

## 自定义风格

### 创建自定义风格

在 `templates/custom/` 目录下创建新的风格文件：

```python
# templates/custom/my-style.py
STYLE_CONFIG = {
    "name": "My Style",
    "primary": "#FF6B9D",
    "secondary": "#FFB6C1",
    "background": "#FFF0F5",
    "card_bg": "#FFFFFF",
    "text": "#4A4A4A",
    "css": """
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        background: linear-gradient(135deg, #FFF0F5 0%, #FFB6C1 100%);
        margin: 0;
        padding: 20px;
    }
    """
}
```

### 使用自定义风格

```bash
python xileSkills.py https://mp.weixin.qq.com/s/xxxxx --style custom/my-style
```

## 风格配置参数

| 参数 | 说明 | 类型 | 默认值 |
|------|------|------|--------|
| `name` | 风格名称 | string | - |
| `primary` | 主色调 | string | - |
| `secondary` | 次要色调 | string | - |
| `background` | 背景色 | string | - |
| `card_bg` | 卡片背景色 | string | - |
| `text` | 文字颜色 | string | - |
| `css` | 自定义 CSS | string | - |

## 颜色方案参考

### 粉色系
- `#FF6B9D` - 粉红
- `#FFB6C1` - 浅粉
- `#FF69B4` - 热粉
- `#FFC0CB` - 粉色

### 蓝色系
- `#3B82F6` - 亮蓝
- `#60A5FA` - 天蓝
- `#2563EB` - 深蓝
- `#93C5FD` - 浅蓝

### 绿色系
- `#10B981` - 翠绿
- `#34D399` - 草绿
- `#059669` - 深绿
- `#6EE7B7` - 浅绿

### 紫色系
- `#8B5CF6` - 紫罗兰
- `#A78BFA` - 浅紫
- `#7C3AED` - 深紫
- `#C4B5FD` - 淡紫

### 橙色系
- `#F59E0B` - 橙色
- `#FBBF24` - 金黄
- `#D97706` - 深橙
- `#FCD34D` - 浅橙

### 红色系
- `#EF4444` - 红色
- `#F87171` - 浅红
- `#DC2626` - 深红
- `#FCA5A5` - 淡红

## 布局选项

### Sparse（稀疏）
- 每页 1-2 个要点
- 大字体
- 大量留白

### Balanced（平衡）
- 每页 3-4 个要点
- 中等字体
- 适中留白

### Dense（密集）
- 每页 5-8 个要点
- 小字体
- 最小留白

## 字体建议

### 中文
- `-apple-system` - 系统字体
- `'PingFang SC'` - 苹方
- `'Microsoft YaHei'` - 微软雅黑
- `'Hiragino Sans GB'` - 冬青黑体

### 英文
- `-apple-system` - 系统字体
- `'Segoe UI'` - 微软雅黑
- `'Helvetica Neue'` - Helvetica
- `'Arial'` - Arial

## 动画效果

### 淡入效果
```css
.slide {
    animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
```

### 滑动效果
```css
.slide {
    animation: slideIn 0.5s ease-out;
}

@keyframes slideIn {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}
```

### 缩放效果
```css
.slide {
    animation: zoomIn 0.5s ease-out;
}

@keyframes zoomIn {
    from { transform: scale(0.9); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
}
```

## 图标建议

### Emoji 图标
- 📱 - 手机
- 🎨 - 调色板
- 📊 - 图表
- 🎯 - 目标
- ✨ - 闪光
- 💡 - 灯泡
- 🌟 - 星星
- 🔥 - 火焰

### SVG 图标
使用 Feather Icons、Heroicons 或其他图标库

## 响应式设计

### 移动端
```css
@media (max-width: 768px) {
    .slide {
        padding: 30px 20px;
    }
    p {
        font-size: 18px;
    }
}
```

### 平板
```css
@media (min-width: 769px) and (max-width: 1024px) {
    .slide {
        padding: 50px 30px;
    }
    p {
        font-size: 22px;
    }
}
```

### 桌面
```css
@media (min-width: 1025px) {
    .slide {
        padding: 60px 40px;
    }
    p {
        font-size: 24px;
    }
}
```

## 最佳实践

1. **颜色对比度**：确保文字与背景有足够的对比度
2. **字体大小**：根据内容长度调整字体大小
3. **留白**：适当留白提升可读性
4. **一致性**：保持整个幻灯片风格一致
5. **响应式**：确保在不同设备上都能良好显示

## 示例

查看 `templates/examples/` 目录下的示例文件，了解如何创建自定义风格。

## 贡献

欢迎提交新的风格模板！请遵循以下步骤：

1. Fork 本仓库
2. 创建新的风格文件
3. 提交 Pull Request
4. 等待审核

## 许可证

MIT License

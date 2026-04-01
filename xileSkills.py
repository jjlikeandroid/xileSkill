#!/usr/bin/env python3
"""
XileSkills - 微信文章转小红书 PPT
将微信文章转换为小红书风格的幻灯片页面
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Dict, Optional
import json


class WeChatArticleExtractor:
    """微信文章内容提取器"""

    def __init__(self, url: str):
        self.url = url
        self.title = ""
        self.content = ""
        self.images = []

    def extract_from_url(self) -> bool:
        """从 URL 提取文章内容"""
        # 这里应该使用 WebFetch 工具
        # 暂时返回 False，表示需要手动输入
        return False

    def parse_markdown(self, markdown_text: str):
        """解析 Markdown 格式的文章"""
        lines = markdown_text.split('\n')
        self.title = lines[0] if lines else "未命名文章"
        self.content = '\n'.join(lines[1:])


class SlideGenerator:
    """幻灯片生成器"""

    def __init__(self, style: str = "cute", layout: str = "balanced"):
        self.style = style
        self.layout = layout
        self.slides = []

    def plan_slides(self, content: str, words_per_page: int = 300) -> List[Dict]:
        """规划幻灯片页面"""
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        slides = []
        current_slide = {"content": [], "type": "content"}

        word_count = 0

        for para in paragraphs:
            para_words = len(para)
            if word_count + para_words > words_per_page and current_slide["content"]:
                slides.append(current_slide)
                current_slide = {"content": [], "type": "content"}
                word_count = 0

            current_slide["content"].append(para)
            word_count += para_words

        if current_slide["content"]:
            slides.append(current_slide)

        return slides

    def generate_html(self, title: str, slides: List[Dict]) -> str:
        """生成 HTML 格式的幻灯片"""
        style_config = self.get_style_config()
        html_template = self.get_html_template()

        slides_html = ""
        for i, slide in enumerate(slides, 1):
            slide_html = self.generate_slide_html(slide, i, style_config)
            slides_html += slide_html

        html = html_template.format(
            title=title,
            style=style_config["css"],
            slides=slides_html
        )

        return html

    def get_style_config(self) -> Dict:
        """获取风格配置"""
        styles = {
            "cute": {
                "primary": "#FF6B9D",
                "secondary": "#FFB6C1",
                "background": "#FFF0F5",
                "card_bg": "#FFFFFF",
                "text": "#4A4A4A",
                "css": self.get_cute_css()
            },
            "fresh": {
                "primary": "#10B981",
                "secondary": "#34D399",
                "background": "#F0FDF4",
                "card_bg": "#FFFFFF",
                "text": "#4A4A4A",
                "css": self.get_fresh_css()
            },
            "warm": {
                "primary": "#F59E0B",
                "secondary": "#FBBF24",
                "background": "#FFFBEB",
                "card_bg": "#FFFFFF",
                "text": "#4A4A4A",
                "css": self.get_warm_css()
            },
            "minimal": {
                "primary": "#374151",
                "secondary": "#6B7280",
                "background": "#F9FAFB",
                "card_bg": "#FFFFFF",
                "text": "#1F2937",
                "css": self.get_minimal_css()
            },
            "notion": {
                "primary": "#3B82F6",
                "secondary": "#8B5CF6",
                "background": "#F8FAFC",
                "card_bg": "#FFFFFF",
                "text": "#1E293B",
                "css": self.get_notion_css()
            }
        }
        return styles.get(self.style, styles["cute"])

    def generate_slide_html(self, slide: Dict, slide_num: int, style_config: Dict) -> str:
        """生成单个幻灯片的 HTML"""
        content_html = ""
        for para in slide["content"]:
            content_html += f"<p>{para}</p>\n"

        return f"""
        <div class="slide slide-{slide_num}">
            <div class="slide-content">
                <div class="slide-number">{slide_num}</div>
                {content_html}
            </div>
        </div>
        """

    def get_cute_css(self) -> str:
        """可爱风格 CSS"""
        return """
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #FFF0F5 0%, #FFB6C1 100%);
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
            box-shadow: 0 8px 30px rgba(255, 107, 157, 0.2);
        }
        .slide-content {
            position: relative;
        }
        .slide-number {
            position: absolute;
            top: 20px;
            right: 20px;
            background: #FF6B9D;
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

    def get_fresh_css(self) -> str:
        """清新风格 CSS"""
        return """
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #F0FDF4 0%, #34D399 100%);
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
            box-shadow: 0 8px 30px rgba(16, 185, 129, 0.2);
        }
        .slide-content {
            position: relative;
        }
        .slide-number {
            position: absolute;
            top: 20px;
            right: 20px;
            background: #10B981;
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

    def get_warm_css(self) -> str:
        """温暖风格 CSS"""
        return """
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #FFFBEB 0%, #FBBF24 100%);
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
            box-shadow: 0 8px 30px rgba(245, 158, 11, 0.2);
        }
        .slide-content {
            position: relative;
        }
        .slide-number {
            position: absolute;
            top: 20px;
            right: 20px;
            background: #F59E0B;
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

    def get_minimal_css(self) -> str:
        """简约风格 CSS"""
        return """
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: #F9FAFB;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1080px;
            margin: 0 auto;
        }
        .slide {
            background: #FFFFFF;
            border-radius: 16px;
            padding: 60px 40px;
            margin-bottom: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }
        .slide-content {
            position: relative;
        }
        .slide-number {
            position: absolute;
            top: 20px;
            right: 20px;
            background: #374151;
            color: white;
            padding: 8px 16px;
            border-radius: 12px;
            font-weight: 600;
        }
        p {
            font-size: 22px;
            line-height: 1.8;
            color: #1F2937;
            margin-bottom: 16px;
        }
        """

    def get_notion_css(self) -> str:
        """知识风格 CSS"""
        return """
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
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
            box-shadow: 0 8px 30px rgba(59, 130, 246, 0.15);
        }
        .slide-content {
            position: relative;
        }
        .slide-number {
            position: absolute;
            top: 20px;
            right: 20px;
            background: #3B82F6;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 600;
        }
        p {
            font-size: 24px;
            line-height: 1.8;
            color: #1E293B;
            margin-bottom: 16px;
        }
        """

    def get_html_template(self) -> str:
        """获取 HTML 模板"""
        return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        {style}
    </style>
</head>
<body>
    <div class="container">
        {slides}
    </div>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="微信文章转小红书 PPT")
    parser.add_argument("url", help="微信文章链接")
    parser.add_argument("--style", default="cute", choices=["cute", "fresh", "warm", "minimal", "notion"],
                       help="视觉风格")
    parser.add_argument("--layout", default="balanced", choices=["sparse", "balanced", "dense"],
                       help="布局方式")
    parser.add_argument("--words-per-page", type=int, default=300,
                       help="每页字数")
    parser.add_argument("--output", default="./xhs-slides",
                       help="输出目录")
    parser.add_argument("--format", default="html", choices=["html", "pdf", "png"],
                       help="输出格式")

    args = parser.parse_args()

    # 创建输出目录
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 提取文章内容
    extractor = WeChatArticleExtractor(args.url)
    if not extractor.extract_from_url():
        print("❌ 无法从 URL 提取文章内容")
        print("请手动输入文章内容（按 Ctrl+D 结束）：")
        content_lines = []
        try:
            while True:
                line = input()
                if line == "":
                    break
                content_lines.append(line)
        except EOFError:
            pass
        extractor.title = input("请输入文章标题: ")
        extractor.content = "\n".join(content_lines)

    # 生成幻灯片
    generator = SlideGenerator(style=args.style, layout=args.layout)
    slides = generator.plan_slides(extractor.content, args.words_per_page)

    # 添加封面和结尾
    all_slides = [
        {"type": "cover", "title": extractor.title},
        *slides,
        {"type": "ending", "title": "感谢观看"}
    ]

    # 生成 HTML
    html_content = generator.generate_html(extractor.title, slides)

    # 保存文件
    output_file = output_dir / f"{extractor.title.replace(' ', '_')}.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ 生成完成: {output_file}")
    print(f"📊 共生成 {len(slides)} 页幻灯片")
    print(f"🎨 风格: {args.style}")
    print(f"📐 布局: {args.layout}")


if __name__ == "__main__":
    main()

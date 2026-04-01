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
import urllib.request
import urllib.error
from html.parser import HTMLParser
from html import unescape
import subprocess
import os


class WeChatHTMLParser(HTMLParser):
    """微信文章 HTML 解析器"""

    def __init__(self):
        super().__init__()
        self.in_content = False
        self.in_title = False
        self.title = ""
        self.content = ""
        self.current_text = ""
        self.ignore_tags = {'script', 'style', 'meta', 'link', 'noscript'}

    def handle_starttag(self, tag, attrs):
        if tag in self.ignore_tags:
            return

        if tag == 'meta':
            for attr, value in attrs:
                if attr == 'property' and value == 'og:title':
                    self.in_title = True
                elif attr == 'property' and value == 'og:description':
                    self.in_content = True

        if tag == 'div':
            for attr, value in attrs:
                if attr == 'class' and 'rich_media_content' in value:
                    self.in_content = True

    def handle_endtag(self, tag):
        if tag == 'meta':
            self.in_title = False
            self.in_content = False

        if tag == 'div' and self.in_content:
            self.in_content = False

    def handle_data(self, data):
        if self.in_title and not self.title:
            self.title = data.strip()
        if self.in_content:
            self.current_text += data.strip() + '\n'

    def get_content(self):
        return self.title, self.current_text


class WeChatArticleExtractor:
    """微信文章内容提取器"""

    def __init__(self, url: str):
        self.url = url
        self.title = ""
        self.content = ""
        self.images = []

    def extract_from_url(self) -> bool:
        """从 URL 提取文章内容"""
        try:
            # 设置请求头，模拟浏览器访问
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            # 创建请求对象
            req = urllib.request.Request(self.url, headers=headers)

            # 发送请求
            with urllib.request.urlopen(req, timeout=30) as response:
                html_content = response.read().decode('utf-8')

            # 解析 HTML
            parser = WeChatHTMLParser()
            parser.feed(html_content)
            title, content = parser.get_content()

            if title and content:
                self.title = title
                self.content = content
                return True
            elif content:
                # 如果没有标题，尝试从 HTML 中提取
                self.title = self.extract_title_from_html(html_content)
                self.content = content
                return True

            return False

        except urllib.error.URLError as e:
            print(f"❌ URL 错误: {e}")
            return False
        except Exception as e:
            print(f"❌ 提取失败: {e}")
            return False

    def extract_title_from_html(self, html: str) -> str:
        """从 HTML 中提取标题"""
        # 尝试从 meta 标签提取
        title_match = re.search(r'<meta property="og:title" content="([^"]+)"', html)
        if title_match:
            return unescape(title_match.group(1))

        # 尝试从 title 标签提取
        title_match = re.search(r'<title>([^<]+)</title>', html)
        if title_match:
            return unescape(title_match.group(1))

        return "未命名文章"

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

    def export_to_pdf(self, html_content: str, output_path: Path) -> bool:
        """导出为 PDF 格式"""
        try:
            # 检查是否安装了 wkhtmltopdf
            if not self.check_wkhtmltopdf():
                print("⚠️  未找到 wkhtmltopdf，尝试使用浏览器打印...")
                return self.export_to_pdf_via_browser(html_content, output_path)

            # 使用 wkhtmltopdf 转换
            html_file = output_path.with_suffix('.html')
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)

            cmd = [
                'wkhtmltopdf',
                '--page-size', 'A4',
                '--orientation', 'Portrait',
                '--margin-top', '0.5cm',
                '--margin-bottom', '0.5cm',
                '--margin-left', '0.5cm',
                '--margin-right', '0.5cm',
                '--encoding', 'UTF-8',
                str(html_file),
                str(output_path)
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                # 删除临时 HTML 文件
                html_file.unlink()
                return True
            else:
                print(f"❌ PDF 转换失败: {result.stderr}")
                return False

        except Exception as e:
            print(f"❌ PDF 导出失败: {e}")
            return False

    def export_to_png(self, html_content: str, output_path: Path) -> bool:
        """导出为 PNG 格式"""
        try:
            # 检查是否安装了 wkhtmltoimage
            if not self.check_wkhtmltoimage():
                print("⚠️  未找到 wkhtmltoimage，尝试使用浏览器截图...")
                return self.export_to_png_via_browser(html_content, output_path)

            # 使用 wkhtmltoimage 转换
            html_file = output_path.with_suffix('.html')
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)

            cmd = [
                'wkhtmltoimage',
                '--format', 'png',
                '--quality', '95',
                '--width', '1080',
                '--height', '1440',
                '--encoding', 'UTF-8',
                str(html_file),
                str(output_path)
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                # 删除临时 HTML 文件
                html_file.unlink()
                return True
            else:
                print(f"❌ PNG 转换失败: {result.stderr}")
                return False

        except Exception as e:
            print(f"❌ PNG 导出失败: {e}")
            return False

    def check_wkhtmltopdf(self) -> bool:
        """检查是否安装了 wkhtmltopdf"""
        try:
            result = subprocess.run(['wkhtmltopdf', '--version'],
                                  capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False

    def check_wkhtmltoimage(self) -> bool:
        """检查是否安装了 wkhtmltoimage"""
        try:
            result = subprocess.run(['wkhtmltoimage', '--version'],
                                  capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False

    def export_to_pdf_via_browser(self, html_content: str, output_path: Path) -> bool:
        """通过浏览器打印导出 PDF"""
        try:
            # 保存 HTML 文件
            html_file = output_path.with_suffix('.html')
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)

            print(f"💡 请在浏览器中打开 {html_file}")
            print("💡 然后使用浏览器的打印功能（Ctrl+P）保存为 PDF")
            print("💡 打印设置：")
            print("   - 纸张大小：A4")
            print("   - 方向：纵向")
            print("   - 边距：适中")
            print("   - 勾选'背景图形'")

            # 尝试在默认浏览器中打开
            if os.name == 'nt':  # Windows
                os.startfile(str(html_file))
            elif os.name == 'posix':  # macOS/Linux
                subprocess.run(['open', str(html_file)], check=True)

            return True

        except Exception as e:
            print(f"❌ 浏览器打开失败: {e}")
            return False

    def export_to_png_via_browser(self, html_content: str, output_path: Path) -> bool:
        """通过浏览器截图导出 PNG"""
        try:
            # 保存 HTML 文件
            html_file = output_path.with_suffix('.html')
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)

            print(f"💡 请在浏览器中打开 {html_file}")
            print("💡 然后使用截图工具（如 Windows 截图工具、macOS 截图）保存为 PNG")
            print("💡 建议截图尺寸：1080x1440")

            # 尝试在默认浏览器中打开
            if os.name == 'nt':  # Windows
                os.startfile(str(html_file))
            elif os.name == 'posix':  # macOS/Linux
                subprocess.run(['open', str(html_file)], check=True)

            return True

        except Exception as e:
            print(f"❌ 浏览器打开失败: {e}")
            return False


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

    # 根据格式导出
    output_file = output_dir / f"{extractor.title.replace(' ', '_')}"
    success = False

    if args.format == "html":
        # 导出 HTML
        html_file = output_file.with_suffix('.html')
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✅ HTML 生成完成: {html_file}")
        success = True

    elif args.format == "pdf":
        # 导出 PDF
        pdf_file = output_file.with_suffix('.pdf')
        success = generator.export_to_pdf(html_content, pdf_file)
        if success:
            print(f"✅ PDF 生成完成: {pdf_file}")

    elif args.format == "png":
        # 导出 PNG
        png_file = output_file.with_suffix('.png')
        success = generator.export_to_png(html_content, png_file)
        if success:
            print(f"✅ PNG 生成完成: {png_file}")

    if success:
        print(f"📊 共生成 {len(slides)} 页幻灯片")
        print(f"🎨 风格: {args.style}")
        print(f"📐 布局: {args.layout}")
        print(f"📁 输出格式: {args.format.upper()}")


if __name__ == "__main__":
    main()

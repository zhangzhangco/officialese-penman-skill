from html.parser import HTMLParser
from pathlib import Path

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_style_or_script = False

    def handle_starttag(self, tag, attrs):
        if tag in ('style', 'script'):
            self.in_style_or_script = True

    def handle_endtag(self, tag):
        if tag in ('style', 'script'):
            self.in_style_or_script = False

    def handle_data(self, data):
        if not self.in_style_or_script:
            clean = data.strip()
            if clean:
                self.text.append(clean)

extractor = HTMLTextExtractor()
html_content = Path('/Users/zhangxin/.gemini/antigravity/brain/d68c999b-2b2a-4933-9d72-6fb9c263bc19/.system_generated/steps/93/content.md').read_text(encoding='utf-8')
extractor.feed(html_content)
Path('/Users/zhangxin/.gemini/antigravity/brain/d68c999b-2b2a-4933-9d72-6fb9c263bc19/.system_generated/steps/93/text_only.txt').write_text('\n'.join(extractor.text), encoding='utf-8')
print("Extracted text successfully.")

#!/usr/bin/env python3
"""检查 Markdown 或纯文本中是否仍有中文方括号占位符。"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

PATTERN = re.compile(r"〔[^〕\n]+〕|\[[^\]\n]+\]")


def main() -> int:
    parser = argparse.ArgumentParser(description="检查文稿中的未替换占位符")
    parser.add_argument("file", type=Path, help="待检查的 Markdown 或文本文件")
    args = parser.parse_args()

    if not args.file.exists():
        print(f"文件不存在：{args.file}")
        return 2

    text = args.file.read_text(encoding="utf-8")
    matches = list(PATTERN.finditer(text))

    if not matches:
        print("未发现占位符。")
        return 0

    print(f"发现 {len(matches)} 个可能未替换的占位符：")
    for match in matches:
        line_no = text.count("\n", 0, match.start()) + 1
        print(f"第 {line_no} 行：{match.group(0)}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

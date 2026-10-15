#!/usr/bin/env python3
"""Render the repository report with GitHub Markdown and add native audio players."""
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urljoin

ROOT = Path(__file__).resolve().parents[1]
REPO = "Nnnnobel/shu261-audio-practice-2026"
PAGE = "https://Nnnnobel.github.io/shu261-audio-practice-2026/"
markdown = (ROOT / "task/research.md").read_text()
body = subprocess.run(
    ["gh", "api", "markdown", "--input", "-"],
    input=json.dumps({"text": markdown, "mode": "gfm", "context": REPO}),
    capture_output=True, text=True, check=True,
).stdout


def resolve_link(match):
    attr, value = match.groups()
    if value.startswith(("https://", "http://", "#", "mailto:")):
        return match.group(0)
    prefix = "https://raw.githubusercontent.com/" if attr == "src" else "https://github.com/"
    base = f"{prefix}{REPO}/{'main' if attr == 'src' else 'blob/main'}/task/"
    return f'{attr}="{urljoin(base, value)}"'


body = re.sub(r'(href|src)="([^"]+)"', resolve_link, body)
for anchor, file, loop in [
    ("rain", "rain-r02-01.wav", " loop"),
    ("wood-tap", "wood-tap-final.wav", ""),
]:
    # Replace the report's dedicated listening link with the real player.
    pattern = rf'<p[^>]*><a href="{re.escape(PAGE)}#{anchor}"[^>]*>(.*?)</a></p>'
    player = (
        f'<section class="audio-card" id="{anchor}" aria-label="\\1">'
        f'<p class="audio-title">\\1</p>'
        f'<audio controls preload="metadata"{loop} aria-label="\\1">'
        f'<source src="audio/{file}" type="audio/wav">'
        '浏览器不支持音频播放，请使用下方 WAV 链接。'
        f'</audio><p class="audio-link"><a href="audio/{file}">打开 WAV 原文件</a>'
        + (' · 循环播放已开启' if loop else ' · 单次播放')
        + '</p></section>'
    )
    body, count = re.subn(pattern, player, body)
    if count != 1:
        raise RuntimeError(f"Expected one listening link for {anchor}, found {count}")

html = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="聚光灯 GameJam 的真实 AI 音频设计协作记录，附雨声与桌面敲击试听。">
<title>AI 音频设计探索 · 报告与试听</title>
<style>
:root{color-scheme:light;--ink:#303a33;--muted:#647065;--line:#dce1d6;--accent:#44634f}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:20px}
body{margin:0;background:#f5f3eb;color:var(--ink);font:17px/1.85 system-ui,-apple-system,"PingFang SC",sans-serif}
main{max-width:1000px;margin:32px auto;padding:36px 46px;background:#fffefa;border:1px solid var(--line);border-radius:18px}
nav{display:flex;gap:20px;flex-wrap:wrap;font-size:14px;border-bottom:1px solid var(--line);padding-bottom:18px;margin-bottom:28px}
a{color:var(--accent);text-underline-offset:4px}a:hover{color:#213f2c}
h1{font-size:30px;line-height:1.5;margin:0 0 22px}h2{font-size:23px;margin-top:42px}h3{font-size:19px;margin-top:30px}
p{margin:15px 0}blockquote{margin:20px 0;padding:6px 20px;border-left:4px solid #9aaa89;background:#f1f4eb;color:#53604f}
table{border-collapse:collapse;width:100%;display:block;overflow-x:auto;font-size:14px;margin:20px 0}
td,th{border:1px solid var(--line);padding:10px 12px;text-align:left;min-width:96px}th{background:#f1f3ec}
img{max-width:100%;height:auto}pre{overflow-x:auto;background:#f1f3ed;padding:18px;border-radius:8px;font-size:13px}
code{font-size:.88em}.audio-card{border:1px solid #c9d5c4;border-radius:12px;background:#f0f4eb;padding:18px 22px;margin:18px 0;scroll-margin-top:24px}
.audio-title{font-weight:650;margin:0 0 12px}.audio-link{font-size:13px;margin:10px 0 0;color:var(--muted)}audio{display:block;width:100%;height:54px}
footer{margin-top:40px;padding-top:18px;border-top:1px solid var(--line);color:var(--muted);font-size:13px}
@media(max-width:640px){body{font-size:16px}main{margin:0;border:0;border-radius:0;padding:24px 18px}h1{font-size:25px}.audio-card{padding:16px}td,th{padding:8px}}
</style>
</head>
<body><main>
<nav><a href="https://github.com/Nnnnobel/shu261-audio-practice-2026">GitHub 仓库</a><a href="https://github.com/Nnnnobel/shu261-audio-practice-2026/blob/main/task/research.md">Markdown 报告</a><a href="#rain">雨声试听</a><a href="#wood-tap">桌面敲击试听</a></nav>
""" + body + """
<footer>报告依据实际交互与成果，由 Codex 梳理；项目决策与最终取舍由本人控制。音频生成来源：<a href="https://elevenlabs.io">elevenlabs.io</a>。非商业课程展示。<br>本网页从仓库 Markdown 报告生成，最后更新：2026-10-16。</footer>
</main>
<script>
document.querySelectorAll('audio').forEach(current => current.addEventListener('play', () => {
  document.querySelectorAll('audio').forEach(other => { if (other !== current) other.pause(); });
}));
</script></body></html>
"""
(ROOT / "docs/index.html").write_text(html)
(ROOT / "docs/.nojekyll").touch()
print("Built docs/index.html with 2 audio players")

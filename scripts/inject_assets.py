# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<script src="./rabbit-loader.js"></script>'
replacement = """<script src="./rabbit-loader.js"></script>
<link rel="stylesheet" href="./rabbit-feed-2.css">
<link rel="stylesheet" href="./rabbit-sky-2.css">
<script src="./rabbit-catalog-v2.js"></script>
<script src="./rabbit-sky-engine.js"></script>
<script src="./rabbit-sky-canvas.js"></script>
<script src="./rabbit-community-wrapped.js"></script>
<script src="./rabbit-feed-2.js"></script>
<script src="./rabbit-v2-orchestrator.js"></script>"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully injected RABBIT 2.0 assets into index.html!")
else:
    print("Target string not found in index.html")

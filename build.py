# -*- coding: utf-8 -*-
"""
board.html(조각) -> index.html(완전한 웹페이지) 로 감싸 주는 스크립트.

board.html 은 Claude Artifact 용 조각이라 <html>/<head>/<body> 가 없습니다.
GitHub Pages 로 배포하려면 charset·viewport 같은 필수 태그가 있는
'완전한 HTML 문서' 여야 해서 이 스크립트로 감싸 줍니다.

사용법 :  python build.py
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "board.html")
OUT = os.path.join(HERE, "index.html")

HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="유니티로 배우는 게임 프로그래밍 · 13차시 미션보드 by pcteachpc">
<meta property="og:type" content="website">
<meta property="og:title" content="유니티 방과후 미션보드">
<meta property="og:description" content="13번의 미션으로 내 게임 하나 만들기 — 차시별 미션과 코드">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#127918;</text></svg>">
"""

RESET = """
<style>
/* 브라우저 기본 여백 초기화 (Artifact 환경과 동일하게 맞춤) */
html,body{margin:0;padding:0}
</style>
"""

FOOT = """
</body>
</html>
"""


def main():
    if not os.path.exists(SRC):
        print("[!] board.html 이 없습니다:", SRC)
        return 1

    src = io.open(SRC, encoding="utf-8").read()

    marker = "</style>"
    idx = src.rindex(marker) + len(marker)   # 마지막 </style> 뒤에서 자름
    head_part, body_part = src[:idx], src[idx:]

    doc = HEAD + RESET + head_part + "\n</head>\n<body>\n" + body_part.lstrip() + FOOT

    io.open(OUT, "w", encoding="utf-8", newline="\n").write(doc)

    print("[o] index.html 생성 완료 (%d KB)" % (len(doc.encode("utf-8")) // 1024))
    for need in ('<meta charset="utf-8">', 'name="viewport"', "<body>", "</html>"):
        print("    -", need, "OK" if need in doc else "빠짐!")
    return 0


if __name__ == "__main__":
    sys.exit(main())

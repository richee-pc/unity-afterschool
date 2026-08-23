# -*- coding: utf-8 -*-
"""
유니티 방과후 미션보드 — Streamlit 버전 (선택 사항)

⚠️ 되도록 GitHub Pages 를 쓰세요.
   Streamlit 은 페이지를 iframe 안에 넣기 때문에 아래 제약이 있습니다.
     - 차시별 주소(#stage7)로 바로 들어가는 링크가 동작하지 않음
     - 무료 플랜은 접속이 없으면 앱이 잠들어서, 학생이 깨어날 때까지 기다려야 함
     - 스크롤이 이중으로 생김 (바깥 페이지 + 안쪽 iframe)

실행 :  streamlit run streamlit_app.py
"""
import pathlib

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="유니티 방과후 미션보드",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 스트림릿 기본 여백·헤더를 없애서 페이지가 꽉 차게
st.markdown(
    """
    <style>
      .block-container { padding: 0 !important; max-width: 100% !important; }
      header[data-testid="stHeader"] { display: none; }
      [data-testid="stToolbar"] { display: none; }
      footer { visibility: hidden; }
      iframe { border: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

HERE = pathlib.Path(__file__).parent
page = HERE / "index.html"

if not page.exists():
    st.error("index.html 을 찾을 수 없습니다. `python build.py` 를 먼저 실행하세요.")
    st.stop()

components.html(
    page.read_text(encoding="utf-8"),
    height=2400,      # 내용이 길어서 넉넉히. 잘리면 숫자를 더 올리세요
    scrolling=True,
)

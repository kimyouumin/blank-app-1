import streamlit as st

# ==========================================
# 1. 데이터 영역 (Data Configuration)
# ==========================================

# 새로 추가된 가치관 데이터 (6개)
VALUES = ["용기", "성장", "자유", "도전", "연결", "희망"]
VALUES_DATA = {
    "용기": {
        "icon": "https://i.ibb.co/JFRyG4XF/courage.png",
        "desc": "두려움 속에서도<br>한 걸음 앞으로<br>나아가는 힘"
    },
    "성장": {
        "icon": "https://i.ibb.co/yn47G1Jd/grow.png",
        "desc": "작은 순간들이<br>모여 만드는<br>단단한 하루"
    },
    "자유": {
        "icon": "https://i.ibb.co/vxD8zR3v/freedom.png",
        "desc": "나답게 선택하고<br>나아갈 수 있는<br>당신의 권리"
    },
    "도전": {
        "icon": "https://i.ibb.co/fYPfjC21/challenge.png",
        "desc": "새로운 길 위에서<br>스스로를 믿고<br>시작하는 마음"
    },
    "연결": {
        "icon": "https://i.ibb.co/S4fgRTkQ/link.png",
        "desc": "함께하는 순간들이<br>만들어가는<br>따뜻한 관계"
    },
    "희망": {
        "icon": "https://i.ibb.co/8DvMs44h/hope.png",
        "desc": "지금 이 순간에도<br>피어나는<br>작은 가능성"
    }
}

ADJ_WORDS_LIST = [
    "빛나는", "뜨거운", "행복한", "찬란한", "설레는", "특별한",
    "푸르른", "나만의", "성장의", "무한한", "눈부신", "새로운"
]

NOUNS = ["첫걸음", "가능성", "청춘", "비행"]
NOUNS_DATA = {
    "첫걸음": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "두려움 속에서도<br>한 걸음 앞으로<br>나아가는 힘",
        "image": "rose1.png", 
        "color": "rgba(255, 249, 196, 0.9)",
        "bg_img": "https://i.ibb.co/zHCtzXZt/D14-E4-DA9-02-C9-4367-BC45-5-C1-B0-AC1-AC70.png"
    },
    "가능성": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "작은 순간들이<br>모여 만드는<br>단단한 하루",
        "image": "rose2.png", 
        "color": "rgba(255, 255, 240, 0.9)",
        "bg_img": "https://i.ibb.co/p6z6mwYp/865-AFB2-D-5-E7-F-4822-A8-B3-4-C26-B55929-D7.png"
    },
    "청춘": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "나답게 선택하고<br>나아갈 수 있는<br>당신의 권리",
        "image": "https://i.ibb.co/V0PyhcPB/26-A0-FA28-19-BD-419-A-B1-FF-A4-A017-A58-B2-B.jpg",
        "color": "rgba(255, 228, 230, 0.9)",
        "bg_img": "https://i.ibb.co/XZdyVkRs/0-E1-BEFDC-5578-444-C-8288-F80-DB270-C158.png"
    },
    "비행": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "새로운 길 위에서<br>스스로를 믿고<br>시작하는 마음",
        "image": "https://i.ibb.co/nqXqPQp9/IMG-0196.png", 
        "color": "rgba(225, 245, 254, 0.9)",
        "bg_img": "https://i.ibb.co/WWpvTXGs/2716-A5-E8-6670-4233-B564-1-DD0-B5-AA645-E.png"
    },
}

# ==========================================
# 2. 상태 관리 및 유틸리티 함수
# ==========================================

def init_session_state():
    # value(가치관) 상태 추가
    defaults = {"page": "home", "name": "", "value": "", "adj": "", "noun": ""}
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def change_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# ==========================================
# 3. CSS 스타일 모음
# ==========================================

def apply_font():
    """전체 요소(제목, 본문, 버튼 등)에 '고운 돋움' 폰트 강제 적용"""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');
        
        html, body, [class*="css"], [class*="st-"], button, input, p, div, h1, h2, h3, h4, h5, h6, span, label {
            font-family: 'Gowun Dodum', sans-serif !important;
        }
        </style>
    """, unsafe_allow_html=True)

def apply_dark_bg_css():
    apply_font()
    st.markdown("""
        <style>
        .stApp { 
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); 
            color: #E2E8F0;
        }
        hr { border-color: #334155 !important; }
        </style>
    """, unsafe_allow_html=True)

def apply_home_css():
    apply_dark_bg_css()
    st.markdown("""
        <style>
        .sub-title { font-size: 14px; color: #94A3B8; margin-bottom: 5px; }
        .main-title { font-size: 48px; font-weight: 600; col

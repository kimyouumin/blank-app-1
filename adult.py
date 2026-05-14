import streamlit as st

# ==========================================
# 1. 데이터 영역 (PDF 색상 및 키워드 반영)
# ==========================================

VALUES = ["용기", "성장", "자유", "도전", "연결", "희망"]
VALUES_DATA = {
    "용기": {"icon": "https://i.ibb.co/JFRyG4XF/courage.png", "desc": "두려움 속에서도<br>한 걸음 앞으로<br>나아가는 힘"},
    "성장": {"icon": "https://i.ibb.co/yn47G1Jd/grow.png", "desc": "작은 순간들이<br>모여 만드는<br>단단한 하루"},
    "자유": {"icon": "https://i.ibb.co/vxD8zR3v/freedom.png", "desc": "나답게 선택하고<br>나아갈 수 있는<br>당신의 권리"},
    "도전": {"icon": "https://i.ibb.co/fYPfjC21/challenge.png", "desc": "새로운 길 위에서<br>스스로를 믿고<br>시작하는 마음"},
    "연결": {"icon": "https://i.ibb.co/S4fgRTkQ/link.png", "desc": "함께하는 순간들이<br>만들어가는<br>따뜻한 관계"},
    "희망": {"icon": "https://i.ibb.co/8DvMs44h/hope.png", "desc": "지금 이 순간에도<br>피어나는<br>작은 가능성"}
}

ADJ_WORDS_LIST = ["빛나는", "뜨거운", "행복한", "찬란한", "설레는", "특별한", "푸르른", "나만의", "성장의", "무한한", "눈부신", "새로운"]

# PDF 파일의 색상과 문구를 정확히 반영
NOUNS = ["첫걸음", "가능성", "청춘", "비상"] 
NOUNS_DATA = {
    "첫걸음": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "처음이라 서툰 건<br>너무 당연한 일이야",
        "image": "https://i.ibb.co/zHCtzXZt/D14-E4-DA9-02-C9-4367-BC45-5-C1-B0-AC1-AC70.png", 
        "color": "#3B5998",      # PDF 배경: 진청색
        "text_color": "#FFD700", # PDF 글씨: 금색/노랑
        "bg_img": "https://i.ibb.co/zHCtzXZt/D14-E4-DA9-02-C9-4367-BC45-5-C1-B0-AC1-AC70.png"
    },
    "가능성": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "너의 미래는 더<br>자유롭고 빛날 수 있어",
        "image": "https://i.ibb.co/p6z6mwYp/865-AFB2-D-5-E7-F-4822-A8-B3-4-C26-B55929-D7.png", 
        "color": "#2D5A27",      # PDF 배경: 딥그린
        "text_color": "#FFFFFF", # PDF 글씨: 화이트
        "bg_img": "https://i.ibb.co/p6z6mwYp/865-AFB2-D-5-E7-F-4822-A8-B3-4-C26-B55929-D7.png"
    },
    "청춘": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "가장 뜨겁고 찬란한<br>계절 위에 서 있는 너",
        "image": "https://i.ibb.co/V0PyhcPB/26-A0-FA28-19-BD-419-A-B1-FF-A4-A017-A58-B2-B.jpg",
        "color": "#F9D423",      # PDF 배경: 선명한 노랑
        "text_color": "#800000", # PDF 글씨: 와인색
        "bg_img": "https://i.ibb.co/XZdyVkRs/0-E1-BEFDC-5578-444-C-8288-F80-DB270-C158.png"
    },
    "비상": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "너만의 꿈과 방향을<br>천천히 찾아가길 바라",
        "image": "https://i.ibb.co/nqXqPQp9/IMG-0196.png", 
        "color": "#F08080",      # PDF 배경: 코랄/분홍
        "text_color": "#191970", # PDF 글씨: 미드나잇블루
        "bg_img": "https://i.ibb.co/WWpvTXGs/2716-A5-E8-6670-4233-B564-1-DD0-B5-AA645-E.png"
    },
}

# ==========================================
# 2. 상태 관리 및 유틸리티
# ==========================================

def init_session_state():
    defaults = {"page": "home", "name": "", "value": "", "adj": "", "noun": ""}
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

def change_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# ==========================================
# 3. CSS 스타일 정의
# ==========================================

def apply_font():
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
        .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #E2E8F0; }
        </style>
    """, unsafe_allow_html=True)

def apply_card_css():
    apply_dark_bg_css()
    st.markdown("""
        <style>
        button[kind="primary"] { background-color: #FFFFFF !important; border-radius: 0px !important; height: 50px !important; width: 100%; transition: 0.3s; }
        button[kind="primary"] p { color: #0f172a !important; font-weight: 600 !important; }
        button[kind="secondary"] { background-color: transparent !important; border: 1px solid #475569 !important; border-radius: 0px !important; color: #CBD5E1 !important; width: 100%; }
        </style>
    """, unsafe_allow_html=True)

def apply_result_css(board_color, text_color, bg_url):
    apply_font()
    st.markdown(f"""
        <style>
        .stApp {{ background-image: url("{bg_url}"); background-size: cover; background-position: center; background-attachment: fixed; }}
        .block-container {{
            background-color: {board_color}EE !important; /* 약간의 투명도 */
            border-radius: 30px; padding: 50px 30px; max-width: 800px !important; 
            margin-top: 50px; text-align: center; box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
        }}
        /* 결과창 내부 모든 글자 색상을 PDF 색상으로 강제 지정 */
        .block-container h1, .block-container h3, .block-container b, .block-container span, .block-container p {{
            color: {text_color} !important;
        }}
        button[kind="secondary"] {{ background-color: #ffffff !important; border-radius: 0px !important; width: 100%; margin-top: 20px; }}
        button[kind="secondary"] p {{ color: #0f172a !important; font-weight: bold !important; font-size: 18px !important; }}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 4. 페이지 렌더링 함수
# ==========================================

def render_home_page():
    apply_dark_bg_css()
    st.markdown("<br><br><h1 style='text-align:center;'>나의 키워드</h1>", unsafe_allow_html=True)
    name = st.text_input("당신의 이름을 알려주세요", value=st.session_state.name)
    if st.button("검사 시작하기 →"):
        if name.strip():
            st.session_state.name = name.strip()
            change_page("value")
        else: st.warning("이름을 입력해주세요!")

def render_value_page():
    apply_card_css()
    st.markdown("<h3 style='text-align:center;'>중요하게 생각하는 가치는?</h3>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, val in enumerate(VALUES):
        with cols[i % 3]:
            st.markdown(f"<div style='background:#fff; padding:20px; text-align:center; color:#333; height:180px; border:1px solid #ddd;'><b>{val}</b><br><br><small>{VALUES_DATA[val]['desc']}</small></div>", unsafe_allow_html=True)
            if st.button(f"{val} 선택", key=f"v_{val}", type="primary"):
                st.session_state.value = val
                change_page("adj")

def render_adj_page():
    apply_card_css()
    st.markdown("<h3 style='text-align:center;'>어울리는 형용사를 골라주세요</h3>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, adj in enumerate(ADJ_WORDS_LIST):
        with cols[i % 3]:
            if st.button(adj, key=f"a_{i}", type="primary"):
                st.session_state.adj = adj
                change_page("noun")

def render_noun_page():
    apply_card_css()
    st.markdown("<h3 style='text-align:center;'>마지막 키워드 선택</h3>", unsafe_allow_html=True)
    cols = st.columns(2)
    for i, noun in enumerate(NOUNS):
        with cols[i % 2]:
            st.markdown(f"<div style='background:#fff; padding:20px; text-align:center; color:#333; height:150px; border:1px solid #ddd;'><b>{noun}</b><br><br><small>{NOUNS_DATA[noun]['desc']}</small></div>", unsafe_allow_html=True)
            if st.button(f"{noun} 선택", key=f"n_{noun}", type="primary"):
                st.session_state.noun = noun
                change_page("result")

def render_result_page():
    # 에러 방지: 데이터가 없는 경우 홈으로 리다이렉트
    noun_key = st.session_state.noun
    if noun_key not in NOUNS_DATA:
        st.error("데이터를 찾을 수 없습니다. 처음부터 다시 시작해주세요.")
        if st.button("홈으로 이동"):
            st.session_state.clear()
            change_page("home")
        return

    data = NOUNS_DATA[noun_key]
    apply_result_css(data["color"], data["text_color"], data["bg_img"])
    
    st.markdown(f"<h1>🌹 {st.session_state.name}님을 위한 응원 🌹</h1>", unsafe_allow_html=True)
    st.image(data["image"], use_container_width=True)
    
    st.markdown(f"""
        <h3>
        <b>{st.session_state.value}</b>의 가치를 간직한 채<br><br>
        <b>{st.session_state.adj} {st.session_state.noun}</b>으로<br>
        나아갈 당신의 앞날을 응원합니다!
        </h3>
    """, unsafe_allow_html=True)
    
    st.balloons()
    if st.button("🔄 처음부터 다시하기", key="restart"):
        st.session_state.clear()
        change_page("home")

# ==========================================
# 5. 실행부
# ==========================================

def main():
    init_session_state()
    if st.session_state.page == "home": render_home_page()
    elif st.session_state.page == "value": render_value_page()
    elif st.session_state.page == "adj": render_adj_page()
    elif st.session_state.page == "noun": render_noun_page()
    elif st.session_state.page == "result": render_result_page()

if __name__ == "__main__":
    st.set_page_config(page_title="나의 키워드", page_icon="🌹", layout="centered")
    main()

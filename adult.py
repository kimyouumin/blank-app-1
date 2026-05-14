# ==========================================
# 1. 데이터 영역 (수정된 색상 값)
# ==========================================

NOUNS = ["첫걸음", "가능성", "청춘", "비행"]
NOUNS_DATA = {
    "첫걸음": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "하지만 작은 한 걸음이<br>모여 결국 너만의<br>길을 만들어 줄 거야.",
        "image": "rose1.png", 
        "color": "#4A90E2",  # 파란색 배경
        "text_color": "#FFD700", # 노란색 글씨
        "bg_img": "https://i.ibb.co/zHCtzXZt/D14-E4-DA9-02-C9-4367-BC45-5-C1-B0-AC1-AC70.png"
    },
    "가능성": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "스스로를 믿는 마음만<br>잃지 않는다면 넌 어디서든<br>피어날 수 있는 사람이야.",
        "image": "rose2.png", 
        "color": "#2D6A4F",  # 초록색 배경 [cite: 20, 22]
        "text_color": "#FFFFFF", # 흰색 글씨 [cite: 21]
        "bg_img": "https://i.ibb.co/p6z6mwYp/865-AFB2-D-5-E7-F-4822-A8-B3-4-C26-B55929-D7.png"
    },
    "청춘": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "지금의 너는 가장<br>뜨겁고 찬란한<br>계절 위에 서 있어.",
        "image": "https://i.ibb.co/V0PyhcPB/26-A0-FA28-19-BD-419-A-B1-FF-A4-A017-A58-B2-B.jpg", 
        "color": "#F4D03F",  # 노란색 배경 [cite: 10]
        "text_color": "#800000", # 갈색/다크레드 글씨 [cite: 11]
        "bg_img": "https://i.ibb.co/XZdyVkRs/0-E1-BEFDC-5578-444-C-8288-F80-DB270-C158.png"
    },
    "비행": {
        "icon": "https://cdn-icons-png.flaticon.com/512/2926/2926750.png",
        "desc": "너의 앞으로의 날들이<br>멋진 비상으로<br>가득하길 응원할게.",
        "image": "https://i.ibb.co/nqXqPQp9/IMG-0196.png", 
        "color": "#F06292",  # 분홍색 배경 [cite: 1]
        "text_color": "#1A237E", # 남색 글씨 [cite: 2]
        "bg_img": "https://i.ibb.co/WWpvTXGs/2716-A5-E8-6670-4233-B564-1-DD0-B5-AA645-E.png"
    },
}

# ==========================================
# 3. CSS 스타일 (글씨 색상 동적 적용 수정)
# ==========================================

def apply_result_css(board_color, text_color, bg_url):
    apply_font()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{bg_url}"); background-size: cover;
            background-position: center; background-attachment: fixed;
        }}
        .block-container {{
            background-color: {board_color} !important; border-radius: 30px;
            padding: 50px 30px; box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2); 
            max-width: 850px !important; 
            margin-top: 80px;
            text-align: center; color: {text_color} !important;
        }}
        /* 결과창 내 모든 텍스트 색상 강제 적용 */
        .block-container h1, .block-container h3, .block-container b, .block-container p {{
            color: {text_color} !important;
        }}
        button[kind="secondary"] {{
            background-color: #ffffff !important; 
            border: 1px solid #eeeeee !important;
            border-radius: 0px !important; 
            padding: 15px 20px !important;
            transition: all 0.3s ease; 
            margin-top: 20px !important; 
            width: 100%;
        }}
        button[kind="secondary"] p {{
            color: #0f172a !important; 
            font-size: 20px !important; 
            font-weight: bold !important; 
            margin: 0 !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 4. 페이지 렌더링 (매개변수 전달 수정)
# ==========================================

def render_result_page():
    data = NOUNS_DATA.get(st.session_state.noun)
    if not data:
        st.error("데이터 오류")
        if st.button("홈으로"): change_page("home")
        return

    # 배경색과 글자색을 함께 전달
    apply_result_css(data["color"], data["text_color"], data["bg_img"])
    
    st.markdown("<h1 style='text-align: center;'>🌹 당신을 위한 한 마디 🌹</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try: st.image(data["image"], use_container_width=True)
        except: st.warning("이미지 확인 필요")
            
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center;'><b>{st.session_state.name}</b>님의 <b>{st.session_state.value}</b>의 가치가 담긴<br><br><b>{st.session_state.adj} {st.session_state.noun}</b> 응원합니다!</h3>", unsafe_allow_html=True)
    st.balloons()
    
    if st.button("🔄 처음부터 다시하기", key="restart_btn"):
        st.session_state.clear()
        change_page("home")

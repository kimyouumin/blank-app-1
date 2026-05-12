import streamlit as st

# --- 1. 데이터 및 초기 설정 ---
adj_words_list = [
    "빛나는", "뜨거운", "행복한", "찬란한", "설레는", "특별한",
    "푸르른", "나만의", "성장의", "무한한", "눈부신", "새로운"
]

nouns = ["첫걸음", "가능성", "청춘", "날개"]

# 명사별 이미지와 플로팅 보드 배경색
nouns_data = {
    "첫걸음": {"image": "rose1.png", "color": "rgba(255, 249, 196, 0.9)"}, # 연노란색
    "가능성": {"image": "rose2.png", "color": "rgba(255, 255, 240, 0.9)"}, # 아이보리
    "청춘": {"image": "rose3.png", "color": "rgba(255, 228, 230, 0.9)"},   # 연분홍색
    "날개": {"image": "rose4.png", "color": "rgba(225, 245, 254, 0.9)"},   # 하늘색
}

# session_state 초기화
defaults = {"page": "home", "name": "", "adj": "", "noun": ""}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# 페이지 이동 함수
def go(page):
    st.session_state.page = page
    st.rerun()

# --- 2. CSS 스타일 모음 ---

# [공통] 전체 배경색 설정
def apply_global_css():
    st.markdown("""
        <style>
        .stApp { background-color: #FAFAFA; }
        </style>
    """, unsafe_allow_html=True)

# [단어 선택 화면용] 둥둥 떠다니는 금색 테두리 버튼
def apply_floating_css():
    st.markdown("""
        <style>
        @keyframes floating {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
            100% { transform: translateY(0px); }
        }
        div.stButton { animation: floating 3s ease-in-out infinite; margin-bottom: 10px; }
        div[data-testid="column"]:nth-child(1) div.stButton { animation-delay: 0.0s; }
        div[data-testid="column"]:nth-child(2) div.stButton { animation-delay: 0.4s; }
        div[data-testid="column"]:nth-child(3) div.stButton { animation-delay: 0.8s; }

        div.stButton > button {
            background-color: transparent !important;
            border: 2px solid #FFD700 !important;
            border-radius: 20px;
            font-size: 20px !important;
            font-weight: bold;
            padding: 15px 10px;
            transition: all 0.3s ease;
            width: 100%;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            background-color: #FFF9E1 !important;
        }
        </style>
    """, unsafe_allow_html=True)

# [결과 화면용] 배경 이미지 + 동적 색상 플로팅 보드
def apply_result_css(board_color):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1518152006812-edab29b069ac?q=80&w=2000"); 
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .block-container {{
            background-color: {board_color};
            border-radius: 30px;
            padding: 50px 30px;
            box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2); 
            max-width: 600px !important; 
            margin-top: 80px;
            text-align: center; 
        }}
        div.stButton > button {{
            background-color: #FFB6C1 !important;
            border: none !important;
            border-radius: 20px;
            color: #fff !important;
            font-size: 20px !important;
            font-weight: bold;
            padding: 10px 20px;
            transition: all 0.3s ease;
            margin-top: 20px;
            width: 100%;
        }}
        div.stButton > button:hover {{
            background-color: #FF69B4 !important;
            transform: scale(1.05);
        }}
        </style>
    """, unsafe_allow_html=True)


# --- 3. 페이지별 화면 구성 ---

# [홈 화면] - 애니메이션 효과 없음
if st.session_state.page == "home":
    apply_global_css() # 기본 배경색만 적용
    st.title("📖 새로운 페이지 📖")
    st.write("---")
    
    # 입력창과 버튼을 중앙으로 모으기 위해 컬럼 사용
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        name = st.text_input("이름을 입력해주세요", value=st.session_state.name)
        # 일반적인 스트림릿 버튼 (애니메이션/테두리 없음)
        if st.button("입장하기", use_container_width=True):
            if not name.strip():
                st.warning("이름을 입력해주세요!")
            else:
                st.session_state.name = name.strip()
                go("adj")

# [형용사 선택] - 애니메이션 효과 적용
elif st.session_state.page == "adj":
    apply_floating_css()
    st.title("단어를 골라주세요 ✨")
    st.write("---")

    cols = st.columns(3)
    for i, adj in enumerate(adj_words_list):
        with cols[i % 3]:
            if st.button(adj, use_container_width=True): 
                st.session_state.adj = adj
                go("noun")

    st.write("---")
    if st.button("← 뒤로"):
        go("home")

# [명사 선택] - 애니메이션 효과 적용
elif st.session_state.page == "noun":
    apply_floating_css()
    st.title("단어를 골라주세요 ✨")
    st.write("---")
    
    n_cols = st.columns(2)
    for i, noun in enumerate(nouns):
        with n_cols[i % 2]:
            if st.button(noun, use_container_width=True):
                st.session_state.noun = noun
                go("result")
                
    st.write("---")
    if st.button("← 뒤로"):
        go("adj")

# [결과 화면]
elif st.session_state.page == "result":
    data = nouns_data[st.session_state.noun]
    apply_result_css(data["color"])
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image(data["image"], use_column_width=True)
        except:
            st.info("이미지 파일을 찾을 수 없습니다.")
            
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("🌹 당신을 위한 한 마디 🌹")
    st.markdown(f"### **{st.session_state.name}**님의 **{st.session_state.adj} {st.session_state.noun}** 응원합니다!")
    
    if st.button("🔄 처음부터"):
        for key, val in defaults.items():
            st.session_state[key] = val
        go("home")

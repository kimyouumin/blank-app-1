import streamlit as st  # 소문자로 수정

# --- 1. 배경 및 스타일 정의 (BG_첫걸음 정의 추가) ---
BG_첫걸음 = """
<style>
.stApp {
   background-color: #FAFAFA;
}
</style>
"""

# --- 2. 데이터 및 초기 설정 ---
adj_words_list = ["빛나는", "뜨거운", "행복한", "찬란한", "설레는", "특별한","푸르른","나만의","성장의","무한한","눈부신","새로운"]
nouns = ["첫걸음", "가능성", "청춘", "날개"]
nouns_data = {
    "첫걸음": {"image": "rose1.png", "bg": BG_첫걸음},
    "가능성": {"image": "rose2.png", "bg": BG_첫걸음},
    "청춘": {"image": "rose3.png", "bg": BG_첫걸음},
    "날개": {"image": "rose4.png", "bg": BG_첫걸음},
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

# --- 3. 공통 애니메이션 CSS (버튼이 있는 페이지에 적용) ---
def apply_floating_css():
    st.markdown("""
        <style>
        @keyframes floating {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        div.stButton { animation: floating 3s ease-in-out infinite; }
        div[data-testid="column"]:nth-child(1) div.stButton { animation-delay: 0.0s; }
        div[data-testid="column"]:nth-child(2) div.stButton { animation-delay: 0.5s; }
        div[data-testid="column"]:nth-child(3) div.stButton { animation-delay: 1.0s; }
        div[data-testid="column"]:nth-child(4) div.stButton { animation-delay: 1.5s; }

        div.stButton > button {
            background-color: transparent !important;
            border: 2px solid #FFD700 !important;
            border-radius: 20px;
            font-size: 22px !important;
            font-weight: bold;
            padding: 10px 20px;
            transition: all 0.3s ease;
            width: 100%;
        }
        div.stButton > button:hover {
            transform: scale(1.1);
            background-color: #FFF9E1 !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 4. 페이지별 화면 구성 ---

# [홈 화면]
if st.session_state.page == "home":
    st.title("📖 새로운 페이지 📖")
    name = st.text_input("이름을 입력해주세요", value=st.session_state.name)
    if st.button("입장하기"):
        if not name.strip():
            st.warning("이름을 입력해주세요!")
        else:
            st.session_state.name = name.strip()
            go("adj")

# [형용사 선택 - 애니메이션 및 레이아웃 적용]
elif st.session_state.page == "adj":
    apply_floating_css()
    st.title("단어를 골라주세요 ✨")
    st.write("---")

    # 6개 단어를 흩어지게 배치 (2-2-2 구조)
    row1_c1, row1_c2, row1_c3, row1_c4 = st.columns([1, 2, 1, 2])
    with row1_c2:
        if st.button(adj_words_list[0]): # 빛나는
            st.session_state.adj = adj_words_list[0]; go("noun")
    with row1_c4:
        if st.button(adj_words_list[1]): # 따뜻한
            st.session_state.adj = adj_words_list[1]; go("noun")

    st.write("") 

    row2_c1, row2_c2, row2_c3 = st.columns([1, 2, 1])
    with row2_c2:
        if st.button(adj_words_list[2]): # 행복한
            st.session_state.adj = adj_words_list[2]; go("noun")

    st.write("")

    row3_c1, row3_c2, row3_c3, row3_c4 = st.columns([2, 1, 1, 2])
    with row3_c1:
        if st.button(adj_words_list[3]): # 찬란한
            st.session_state.adj = adj_words_list[3]; go("noun")
    with row3_c3:
        if st.button(adj_words_list[4]): # 설레는
            st.session_state.adj = adj_words_list[4]; go("noun")
    with row3_c4:
        if st.button(adj_words_list[5]): # 특별한
            st.session_state.adj = adj_words_list[5]; go("noun")

    st.write("---")
    if st.button("← 뒤로"):
        go("home")

# [명사 선택]
elif st.session_state.page == "noun":
    apply_floating_css()
    st.title("단어를 골라주세요 ✨")
    
    # 명사들도 2x2로 배치
    n_c1, n_c2 = st.columns(2)
    for i, noun in enumerate(nouns):
        with (n_c1 if i % 2 == 0 else n_c2):
            if st.button(noun):
                st.session_state.noun = noun
                go("result")
                
    st.write("---")
    if st.button("← 뒤로"):
        go("adj")

# [결과 화면]
elif st.session_state.page == "result":
    data = nouns_data[st.session_state.noun]
    st.markdown(data["bg"], unsafe_allow_html=True)
    
    # 이미지가 없을 경우 에러 방지
    try:
        st.image(data["image"])
    except:
        st.info("이미지를 불러올 수 없습니다. (파일명 확인 필요)")
        
    st.title("🌹 당신을 위한 한 마디 🌹")
    st.header(f"{st.session_state.name}님의 {st.session_state.adj} {st.session_state.noun} 응원합니다!")
    
    if st.button("🔄 처음부터"):
        for key, val in defaults.items():
            st.session_state[key] = val
        go("home")

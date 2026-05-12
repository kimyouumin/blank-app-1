import streamlit as st

# --- 1. 배경 및 스타일 정의 ---
BG_첫걸음 = """
<style>
.stApp {
   background-color: #FAFAFA;
}
</style>
"""

# --- 2. 데이터 및 초기 설정 ---
# 추가된 형용사들을 포함한 리스트 (총 12개)
adj_words_list = [
    "빛나는", "뜨거운", "행복한", "찬란한", "설레는", "특별한",
    "푸르른", "나만의", "성장의", "무한한", "눈부신", "새로운"
]

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

# --- 3. 공통 애니메이션 CSS ---
def apply_floating_css():
    st.markdown("""
        <style>
        @keyframes floating {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        div.stButton { animation: floating 3s ease-in-out infinite; }
        
        /* 컬럼별 엇박자 애니메이션 효과 */
        div[data-testid="column"]:nth-child(odd) div.stButton { animation-delay: 0.0s; }
        div[data-testid="column"]:nth-child(even) div.stButton { animation-delay: 0.5s; }

        div.stButton > button {
            background-color: transparent !important;
            border: 2px solid #FFD700 !important;
            border-radius: 20px;
            font-size: 20px !important;
            font-weight: bold;
            padding: 10px 15px;
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

# [형용사 선택 - 12개 단어 배치]
elif st.session_state.page == "adj":
    apply_floating_css()
    st.title("단어를 골라주세요 ✨")
    st.write("---")

    # --- 첫 번째 줄 (3개) ---
    r1_c1, r1_c2, r1_c3 = st.columns([2, 1, 2])
    with r1_c1:
        if st.button(adj_words_list[0]): # 빛나는
            st.session_state.adj = adj_words_list[0]; go("noun")
    with r1_c2:
        if st.button(adj_words_list[1]): # 뜨거운
            st.session_state.adj = adj_words_list[1]; go("noun")
    with r1_c3:
        if st.button(adj_words_list[2]): # 행복한
            st.session_state.adj = adj_words_list[2]; go("noun")

    st.write("") # 간격

    # --- 두 번째 줄 (3개) ---
    r2_c1, r2_c2, r2_c3, r2_c4 = st.columns([1, 2, 2, 1])
    with r2_c2:
        if st.button(adj_words_list[3]): # 찬란한
            st.session_state.adj = adj_words_list[3]; go("noun")
    with r2_c3:
        if st.button(adj_words_list[4]): # 설레는
            st.session_state.adj = adj_words_list[4]; go("noun")
    with r2_c1: # 특별한 (살짝 왼쪽)
        if st.button(adj_words_list[5]): 
            st.session_state.adj = adj_words_list[5]; go("noun")

    st.write("") 

    # --- 세 번째 줄 (3개) ---
    r3_c1, r3_c2, r3_c3 = st.columns([1, 1, 1])
    with r3_c1:
        if st.button(adj_words_list[6]): # 푸르른
            st.session_state.adj = adj_words_list[6]; go("noun")
    with r3_c2:
        if st.button(adj_words_list[7]): # 나만의
            st.session_state.adj = adj_words_list[7]; go("noun")
    with r3_c3:
        if st.button(adj_words_list[8]): # 성장의
            st.session_state.adj = adj_words_list[8]; go("noun")

    st.write("")

    # --- 네 번째 줄 (3개) ---
    r4_c1, r4_c2, r4_c3, r4_c4 = st.columns([2, 1, 1, 2])
    with r4_c1:
        if st.button(adj_words_list[9]): # 무한한
            st.session_state.adj = adj_words_list[9]; go("noun")
    with r4_c3:
        if st.button(adj_words_list[10]): # 눈부신
            st.session_state.adj = adj_words_list[10]; go("noun")
    with r4_c4:
        if st.button(adj_words_list[11]): # 새로운
            st.session_state.adj = adj_words_list[11]; go("noun")

    st.write("---")
    if st.button("← 뒤로"):
        go("home")

# [명사 선택]
elif st.session_state.page == "noun":
    apply_floating_css()
    st.title("단어를 골라주세요 ✨")
    
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


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
# 총 12개의 형용사
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
        /* 둥둥 떠다니는 애니메이션 */
        @keyframes floating {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
            100% { transform: translateY(0px); }
        }
        
        div.stButton { 
            animation: floating 3s ease-in-out infinite; 
            margin-bottom: 10px;
        }
        
        /* 컬럼 순서대로 파도 타듯 엇박자 애니메이션 */
        div[data-testid="column"]:nth-child(1) div.stButton { animation-delay: 0.0s; }
        div[data-testid="column"]:nth-child(2) div.stButton { animation-delay: 0.4s; }
        div[data-testid="column"]:nth-child(3) div.stButton { animation-delay: 0.8s; }

        /* 버튼 디자인 (크기 통일) */
        div.stButton > button {
            background-color: transparent !important;
            border: 2px solid #FFD700 !important;
            border-radius: 20px;
            font-size: 20px !important;
            font-weight: bold;
            padding: 15px 10px;
            transition: all 0.3s ease;
            width: 100%; /* 버튼이 컬럼 너비에 꽉 차게 맞춰 크기 통일 */
        }
        
        /* 마우스 오버 시 효과 */
        div.stButton > button:hover {
            transform: scale(1.05);
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

# [형용사 선택 - 깔끔한 3x4 그리드 정렬]
elif st.session_state.page == "adj":
    apply_floating_css()
    st.title("단어를 골라주세요 ✨")
    st.write("---")

    # 3개의 동일한 너비를 가진 컬럼 생성
    cols = st.columns(3)
    
    # 12개의 단어를 3개의 컬럼에 순서대로 배치
    for i, adj in enumerate(adj_words_list):
        with cols[i % 3]:
            # use_container_width=True 로 버튼 크기를 완벽하게 통일
            if st.button(adj, use_container_width=True): 
                st.session_state.adj = adj
                go("noun")

    st.write("---")
    
    # 뒤로 가기 버튼은 레이아웃에 영향받지 않게 별도 처리
    if st.button("← 뒤로"):
        go("home")

# [명사 선택 - 동일하게 깔끔한 정렬]
elif st.session_state.page == "noun":
    apply_floating_css()
    st.title("단어를 골라주세요 ✨")
    st.write("---")
    
    # 명사 4개는 2개의 컬럼으로 크게 배치
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

import streamlit as st  # <-- 1. NameError를 해결하는 필수 코드

if "page" not in st.sessinon_state:
    st.session_state.page="새로 피는 페이지"
    
# (선택) 페이지 이동을 위한 go() 함수가 다른 곳에 없다면 이 코드가 필요합니다.
def go(page_name):
    st.session_state.page = page_name
    st.rerun()

# 2. 대문자 'If'를 소문자 'if'로 수정
if st.session_state.page == "adj":
    # --- 1. 배경 및 버튼 스타일 커스텀 ---
    st.markdown("""
        <style>
        /* 1) 둥둥 떠다니는 애니메이션 정의 (위아래로 10px 이동) */
        @keyframes floating {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }

        /* 2) 버튼 컨테이너에 애니메이션 적용 */
        div.stButton {
            animation: floating 3s ease-in-out infinite;
        }

        /* 3) 각 컬럼마다 엇박자로 움직이도록 딜레이 추가 (자연스러운 연출) */
        div[data-testid="column"]:nth-child(1) div.stButton { animation-delay: 0.0s; }
        div[data-testid="column"]:nth-child(2) div.stButton { animation-delay: 0.5s; }
        div[data-testid="column"]:nth-child(3) div.stButton { animation-delay: 1.0s; }
        div[data-testid="column"]:nth-child(4) div.stButton { animation-delay: 1.5s; }

        /* 기존 버튼 디자인 */
        div.stButton > button {
            background-color: transparent !important;
            border: 2px solid #FFD700 !important; /* 금색 테두리 */
            border-radius: 20px;
            font-size: 24px !important;
            font-weight: bold;
            padding: 10px 20px;
            transition: all 0.3s ease;
        }
        
        /* 마우스 오버 시 효과 (애니메이션과 충돌 없이 커짐) */
        div.stButton > button:hover {
            transform: scale(1.1); /* 마우스 올리면 커짐 */
            background-color: #FFF9E1 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("단어를 골라주세요 ✨")
    st.write("---")

    # --- 2. 흩어져 있는 레이아웃 구성 ---
    # 첫 번째 줄
    c1, c2, c3, c4 = st.columns([1, 2, 1, 2])
    with c2: 
        if st.button("뜨거운"):
            st.session_state.adj = "뜨거운"; go("noun")
    with c4:
        if st.button("무한한"):
            st.session_state.adj = "무한한"; go("noun")

    st.write("") # 간격 띄우기

    # 두 번째 줄 (가운데 배치)
    c_mid1, c_mid2, c_mid3 = st.columns([2, 1, 2])
    with c_mid2:
        if st.button("빛나는"):
            st.session_state.adj = "빛나는"; go("noun")

    st.write("") # 간격 띄우기

    # 세 번째 줄
    c5, c6, c7, c8 = st.columns([2, 1, 1, 2])
    with c5:
        if st.button("찬란한"):
            st.session_state.adj = "찬란한"; go("noun")
    with c8:
        if st.button("눈부신"):
            st.session_state.adj = "눈부신"; go("noun")

    # 뒤로 가기 버튼 (하단 고정)
    st.write("---")
    if st.button("← 뒤로"):
        go("home")

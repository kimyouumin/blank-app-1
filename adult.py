import streamlit as st

# --- 1. 데이터 및 초기 설정 ---
adj_words_list = [
    "빛나는", "뜨거운", "행복한", "찬란한", "설레는", "특별한",
    "푸르른", "나만의", "성장의", "무한한", "눈부신", "새로운"
]

nouns = ["첫걸음", "가능성", "청춘", "비행"]

# [수정포인트 1] bg_img 항목을 추가하여 단어별 배경 이미지 URL을 넣습니다.
nouns_data = {
    "첫걸음": {
        "image": "rose1.png", 
        "color": "rgba(255, 249, 196, 0.9)", # 연노랑 보드
        "bg_img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2000" # 첫걸음 배경
    },
    "가능성": {
        "image": "rose2.png", 
        "color": "rgba(255, 255, 240, 0.9)", # 아이보리 보드
        "bg_img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2000" # 가능성 배경 
    },
    "청춘": {
        "image": "https://i.ibb.co/V0PyhcPB/26-A0-FA28-19-BD-419-A-B1-FF-A4-A017-A58-B2-B.jpg",
        "color": "rgba(255, 228, 230, 0.9)", # 연분홍 보드
        "bg_img": "https://i.ibb.co/XZdyVkRs/0-E1-BEFDC-5578-444-C-8288-F80-DB270-C158.png" # 청춘 배경 
    },
    "비행": {
        "image": "https://i.ibb.co/nqXqPQp9/IMG-0196.png", 
        "color": "rgba(225, 245, 254, 0.9)", # 하늘색 보드
        "bg_img": "https://i.ibb.co/WWpvTXGs/2716-A5-E8-6670-4233-B564-1-DD0-B5-AA645-E.png" # 날개 배경
    },
}

# session_state 초기값 설정
defaults = {"page": "home", "name": "", "adj": "", "noun": ""}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# 페이지 이동 함수
def go(page):
    st.session_state.page = page
    st.rerun()

# --- 2. CSS 스타일 모음 ---

def apply_global_css():
    st.markdown("<style>.stApp { background-color: #FAFAFA; }</style>", unsafe_allow_html=True)

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

# [수정포인트 2] bg_url 매개변수를 추가하여 배경 이미지를 동적으로 받습니다.
def apply_result_css(board_color, bg_url):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{bg_url}"); 
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
            background-color: #ffffff !important;
            border: 1px solid #eeeeee !important;
            border-radius: 20px;
            color: #333333 !important;
            font-size: 20px !important;
            font-weight: bold;
            padding: 10px 20px;
            transition: all 0.3s ease;
            margin-top: 20px;
            width: 100%;
        }}
        div.stButton > button:hover {{
            background-color: #f9f9f9 !important;
            transform: scale(1.02);
        }}
        </style>
    """, unsafe_allow_html=True)


# --- 3. 페이지별 화면 구성 ---

if st.session_state.page == "home":
    apply_global_css()
    st.title("📖 새로운 페이지 📖")
    st.write("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        name = st.text_input("이름을 입력해주세요", value=st.session_state.name)
        if st.button("입장하기", use_container_width=True):
            if not name.strip(): st.warning("이름을 입력해주세요!")
            else:
                st.session_state.name = name.strip()
                go("adj")

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
    if st.button("← 뒤로"): go("home")

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
    if st.button("← 뒤로"): go("adj")

elif st.session_state.page == "result":
    # [수정포인트 3] 선택된 명사의 데이터를 가져와서 보드 색상과 배경 URL을 함께 전달합니다.
    data = nouns_data[st.session_state.noun]
    apply_result_css(data["color"], data["bg_img"])
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try: st.image(data["image"], use_column_width=True)
        except: st.info("이미지 파일을 찾을 수 없습니다.")
            
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("🌹 당신을 위한 한 마디 🌹")
    st.markdown(f"### **{st.session_state.name}**님의 **{st.session_state.adj} {st.session_state.noun}** 응원합니다!")
    
    if st.button("🔄 처음부터"):
        for key, val in defaults.items(): st.session_state[key] = val
        go("home")

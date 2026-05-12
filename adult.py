import streamlit as st

# --- 1. 데이터 및 초기 설정 ---
adj_words_list = [
    "빛나는", "뜨거운", "행복한", "찬란한", "설레는", "특별한",
    "푸르른", "나만의", "성장의", "무한한", "눈부신", "새로운"
]

nouns = ["첫걸음", "가능성", "청춘", "비행"]

nouns_data = {
    "첫걸음": {
        "image": "rose1.png", 
        "color": "rgba(255, 249, 196, 0.9)",
        "bg_img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2000"
    },
    "가능성": {
        "image": "rose2.png", 
        "color": "rgba(255, 255, 240, 0.9)",
        "bg_img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2000"
    },
    "청춘": {
        "image": "https://i.ibb.co/V0PyhcPB/26-A0-FA28-19-BD-419-A-B1-FF-A4-A017-A58-B2-B.jpg",
        "color": "rgba(255, 228, 230, 0.9)",
        "bg_img": "https://i.ibb.co/XZdyVkRs/0-E1-BEFDC-5578-444-C-8288-F80-DB270-C158.png"
    },
    "비행": {
        "image": "https://i.ibb.co/nqXqPQp9/IMG-0196.png", 
        "color": "rgba(225, 245, 254, 0.9)",
        "bg_img": "https://i.ibb.co/WWpvTXGs/2716-A5-E8-6670-4233-B564-1-DD0-B5-AA645-E.png"
    },
}

defaults = {"page": "home", "name": "", "adj": "", "noun": ""}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

def go(page):
    st.session_state.page = page
    st.rerun()

# --- 2. CSS 스타일 모음 ---

def apply_font():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Hahmlet:wght@300;400;600&display=swap');
        html, body, [class*="css"]  {
            font-family: 'Hahmlet', serif;
        }
        </style>
    """, unsafe_allow_html=True)

def apply_home_css():
    apply_font()
    st.markdown("""
        <style>
        .stApp { 
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); 
            color: #E2E8F0;
        }
        
        /* 텍스트 타이포그래피 */
        .sub-title { font-size: 14px; color: #94A3B8; margin-bottom: 5px; }
        .main-title { font-size: 48px; font-weight: 600; color: #FFFFFF; margin-bottom: 30px; letter-spacing: -1px; }
        .desc { font-size: 16px; color: #CBD5E1; line-height: 1.6; margin-bottom: 40px; }
        
        .quote {
            font-size: 18px;
            color: #E2E8F0;
            line-height: 1.8;
            font-style: italic;
            text-align: center;
            margin-top: 50px;
        }
        
        /* 버튼 스타일링 (투명 배경, 흰색 테두리) */
        div.stButton > button {
            background-color: transparent !important;
            border: 1px solid #475569 !important;
            color: #F8FAFC !important;
            border-radius: 0px !important; 
            padding: 10px 30px !important;
            width: auto;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            border-color: #FFFFFF !important;
            background-color: rgba(255,255,255,0.1) !important;
        }
        
        /* 입력창 라벨 텍스트 색상(흰색) 변경 */
        div[data-testid="stTextInput"] label p {
            color: #FFFFFF !important;
            font-size: 15px;
        }

        /* 입력창 스타일링 */
        div[data-testid="stTextInput"] input {
            background-color: rgba(0,0,0,0.2);
            color: white;
            border: none;
            border-bottom: 1px solid #475569;
            border-radius: 0;
        }
        </style>
    """, unsafe_allow_html=True)

def apply_global_css():
    apply_font()
    st.markdown("<style>.stApp { background: #FAFAFA; color: #333; }</style>", unsafe_allow_html=True)

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
            border: 2px solid #334155 !important;
            border-radius: 20px !important;
            color: #1E293B !important;
            font-size: 20px !important;
            font-weight: bold;
            padding: 15px 10px;
            transition: all 0.3s ease;
            width: 100%;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            background-color: #F1F5F9 !important;
        }
        </style>
    """, unsafe_allow_html=True)

def apply_result_css(board_color, bg_url):
    apply_font()
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
            color: #333;
        }}
        div.stButton > button {{
            background-color: #ffffff !important;
            border: 1px solid #eeeeee !important;
            border-radius: 20px !important;
            color: #333333 !important;
            font-size: 20px !important;
            font-weight: bold;
            padding: 10px 20px;
            transition: all 0.3s ease;
            margin-top: 20px;
            width: 100%;
        }}
        </style>
    """, unsafe_allow_html=True)


# --- 3. 페이지별 화면 구성 ---

if st.session_state.page == "home":
    apply_home_css()
    
    # 본문 레이아웃 2단 분할 (상단 여백 추가)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, spacer, col2 = st.columns([1, 0.2, 1])
    
    with col1:
        st.markdown("<div class='sub-title'>성년의 날, 나에게 전하는 한 문장</div>", unsafe_allow_html=True)
        st.markdown("<div class='main-title'>나의 키워드</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='desc'>
            간이검사 결과를 바탕으로<br>
            당신에게 어울리는 키워드를 추천해드려요.<br>
            마음에 드는 키워드를 골라 책갈피에 새겨보세요.
            </div>
        """, unsafe_allow_html=True)
        
        name = st.text_input("당신의 이름을 알려주세요 (Enter)", value=st.session_state.name)
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("검사 시작하기 →"):
            if not name.strip(): 
                st.warning("이름을 입력해주세요!")
            else:
                st.session_state.name = name.strip()
                go("adj")

    with col2:
        # 오른쪽 인용구
        st.markdown("""
            <div class='quote'>
                "흐리고 어두운 날에도<br>
                피어나는 장미처럼,<br>
                당신의 이야기도 언젠가<br>
                아름답게 피어날 거에요."
            </div>
        """, unsafe_allow_html=True)
        
        # 오른쪽 이미지 (책갈피 이미지 임시 URL)
        st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=600&auto=format&fit=crop", use_column_width=True)

elif st.session_state.page == "adj":
    apply_global_css()
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
    apply_global_css()
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
    data = nouns_data[st.session_state.noun]
    apply_result_css(data["color"], data["bg_img"])
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try: st.image(data["image"], use_column_width=True)
        except: st.info("이미지 파일을 찾을 수 없습니다.")
            
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("🌹 당신을 위한 한 마디 🌹")
    st.markdown(f"### **{st.session_state.name}**님의 **{st.session_state.adj} {st.session_state.noun}** 응원합니다!")
    
    if st.button("🔄처음부터"):
        for key, val in defaults.items(): st.session_state[key] = val
        go("home")

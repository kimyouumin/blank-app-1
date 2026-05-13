import streamlit as st

# ==========================================
# 1. 데이터 영역 (Data Configuration)
# ==========================================

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
    defaults = {"page": "home", "name": "", "adj": "", "noun": ""}
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
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Hahmlet:wght@300;400;600&display=swap');
        html, body, [class*="css"]  {
            font-family: 'Hahmlet', serif;
        }
        </style>
    """, unsafe_allow_html=True)

def apply_dark_bg_css():
    """홈, 형용사, 명사 페이지 공통 네이비 배경"""
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
        .main-title { font-size: 48px; font-weight: 600; color: #FFFFFF; margin-bottom: 30px; letter-spacing: -1px; }
        .desc { font-size: 16px; color: #CBD5E1; line-height: 1.6; margin-bottom: 40px; }
        
        .quote { font-size: 18px; color: #E2E8F0; line-height: 1.8; font-style: italic; text-align: center; margin-top: 0px; margin-bottom: 20px; }
        
        /* 시작 버튼 (명사 페이지 뒤로가기 버튼과 완벽히 동일한 포맷으로 통일) */
        button[kind="secondary"] {
            background-color: transparent !important;
            border: 1px solid #475569 !important;
            border-radius: 0px !important;
            padding: 8px 20px !important;
            height: auto !important;
        }
        button[kind="secondary"] p {
            color: #CBD5E1 !important;
            margin: 0 !important;
        }
        button[kind="secondary"]:hover {
            background-color: rgba(255,255,255,0.1) !important;
        }
        
        div[data-testid="stTextInput"] label p { color: #FFFFFF !important; font-size: 15px; }
        div[data-testid="stTextInput"] input {
            background-color: rgba(0,0,0,0.2); color: white; border: none;
            border-bottom: 1px solid #475569; border-radius: 0;
        }

        @media (max-width: 768px) {
            .main-title { font-size: 32px; margin-bottom: 20px; }
            .desc { font-size: 14px; margin-bottom: 25px; }
            .quote { font-size: 15px; margin-top: 10px; }
            button[kind="secondary"] { width: 100%; }
        }
        </style>
    """, unsafe_allow_html=True)

def apply_adj_css():
    apply_dark_bg_css()
    st.markdown("""
        <style>
        @keyframes floating {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
            100% { transform: translateY(0px); }
        }
        div.stButton { animation: floating 3s ease-in-out infinite; margin-bottom: 10px; }
        
        /* 형용사 선택 버튼 (Primary 속성) */
        button[kind="primary"] {
            background-color: #FFFFFF !important; 
            border: none !important;
            border-radius: 0px !important; 
            padding: 15px 0px !important; 
            transition: all 0.3s ease; 
            width: 100%;
        }
        button[kind="primary"] p {
            color: #0f172a !important; 
            font-size: 18px !important; 
            font-weight: bold !important; 
            margin: 0 !important;
        }
        button[kind="primary"]:hover {
            transform: scale(1.05); 
            background-color: #E2E8F0 !important;
        }

        /* 뒤로가기 버튼 (명사 페이지 뒤로가기 버튼과 완벽히 동일한 포맷으로 통일) */
        button[kind="secondary"] {
            background-color: transparent !important;
            border: 1px solid #475569 !important;
            border-radius: 0px !important;
            padding: 8px 20px !important;
            height: auto !important;
            width: 100%;
        }
        button[kind="secondary"] p {
            color: #CBD5E1 !important;
            margin: 0 !important;
        }
        button[kind="secondary"]:hover {
            background-color: rgba(255,255,255,0.1) !important;
        }

        @media (max-width: 768px) {
            button[kind="primary"] p { font-size: 16px !important; }
        }
        </style>
    """, unsafe_allow_html=True)

def apply_noun_css():
    apply_dark_bg_css()
    st.markdown("""
        <style>
        div.stButton { margin-top: -16px !important; }

        /* Primary 버튼: 카드 하단의 '이 키워드 선택' 버튼 */
        button[kind="primary"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-top: none !important; 
            border-radius: 0px !important; 
            padding: 0px !important; 
            height: 50px !important; 
            margin: 0px !important;
            transition: all 0.3s ease;
            width: 100%;
        }
        button[kind="primary"] p {
            color: #0f172a !important; 
            font-size: 15px !important;
            font-weight: 600 !important;
            line-height: 50px !important; 
            margin: 0 !important;
        }
        button[kind="primary"]:hover {
            background-color: #F8FAFC !important;
        }
        
        /* Secondary 버튼: 뒤로 가기 버튼 */
        button[kind="secondary"] {
            background-color: transparent !important;
            border: 1px solid #475569 !important;
            border-radius: 0px !important;
            padding: 8px 20px !important;
            height: auto !important;
        }
        button[kind="secondary"] p {
            color: #CBD5E1 !important;
            margin: 0 !important;
        }
        button[kind="secondary"]:hover {
            background-color: rgba(255,255,255,0.1) !important;
        }
        </style>
    """, unsafe_allow_html=True)

def apply_result_css(board_color, bg_url):
    apply_font()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{bg_url}"); background-size: cover;
            background-position: center; background-attachment: fixed;
        }}
        .block-container {{
            background-color: {board_color}; border-radius: 30px;
            padding: 50px 30px; box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2); 
            max-width: 850px !important; 
            margin-top: 80px;
            text-align: center; color: #333;
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
        @media (max-width: 768px) {{
            .block-container {{ padding: 30px 20px; margin-top: 40px; border-radius: 20px; }}
            button[kind="secondary"] p {{ font-size: 16px !important; }}
            h1 {{ font-size: 24px !important; }}
        }}
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 4. 페이지 렌더링 함수 모음
# ==========================================

def render_home_page():
    apply_home_css()
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
                change_page("adj")

    with col2:
        st.markdown("""
            <div class='quote'>
                "흐리고 어두운 날에도 피어나는 장미처럼,<br>
                당신의 이야기도 언젠가 아름답게 피어날 거에요."
            </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=600&auto=format&fit=crop", use_container_width=True)

def render_adj_page():
    apply_adj_css()
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #FFFFFF;'>단어를 골라주세요 ✨</h2>", unsafe_allow_html=True)
    st.write("---")
    
    cols = st.columns(3)
    for i, adj in enumerate(ADJ_WORDS_LIST):
        with cols[i % 3]:
            # 형용사 선택 버튼에 type="primary"를 추가하여 흰색 스타일과 매핑
            if st.button(adj, use_container_width=True, type="primary"): 
                st.session_state.adj = adj
                change_page("noun")
                
    st.write("---")
    
    back_col, _, _ = st.columns([1, 4, 1])
    with back_col:
        # 뒤로 버튼은 기본값인 type="secondary"로 유지되어 투명한 회색 테두리 스타일 적용
        if st.button("← 뒤로"): 
            change_page("home")

def render_noun_page():
    apply_noun_css()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-weight: 600; color: #FFFFFF;'>당신에게 어울리는 키워드예요</h3>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center; color: #CBD5E1; font-size: 15px; line-height: 1.6;'>
            마음에 드는 키워드를 확인하고,<br>
            하단의 <b>'이 키워드 선택'</b>을 눌러 키워드를 선택해주세요.
        </p>
    """, unsafe_allow_html=True)
    st.write("---")
    
    cols = st.columns(4)
    
    for i, noun in enumerate(NOUNS):
        with cols[i]:
            data = NOUNS_DATA[noun]
            
            st.markdown(f"""
            <div style='
                background-color: #FFFFFF; 
                border: 1px solid #E2E8F0;
                border-bottom: none;
                padding: 40px 15px; 
                text-align: center; 
                height: 250px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                margin-bottom: 0px; 
            '>
                <img src='{data["icon"]}' width='35' style='margin-bottom: 25px;'/>
                <div style='font-size: 20px; font-weight: 600; color: #1e293b; margin-bottom: 15px;'>{noun}</div>
                <div style='font-size: 13px; color: #64748b; line-height: 1.6;'>{data["desc"]}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("이 키워드 선택", key=f"btn_{noun}", use_container_width=True, type="primary"):
                st.session_state.noun = noun
                change_page("result")
                
    st.write("---")
    
    back_col, _, _ = st.columns([1, 4, 1])
    with back_col:
        if st.button("← 뒤로"): 
            change_page("adj")

def render_result_page():
    data = NOUNS_DATA.get(st.session_state.noun)
    if not data:
        st.error("데이터를 불러오는 데 문제가 발생했습니다.")
        if st.button("처음으로 돌아가기"): change_page("home")
        return

    apply_result_css(data["color"], data["bg_img"])
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try: 
            st.image(data["image"], use_container_width=True)
        except Exception as e: 
            st.warning("이미지 파일을 찾을 수 없습니다. (경로를 확인해주세요)")
            
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("🌹 당신을 위한 한 마디 🌹")
    st.markdown(f"### **{st.session_state.name}**님의 **{st.session_state.adj} {st.session_state.noun}** 응원합니다!")
    
    st.balloons()
    
    if st.button("🔄 처음부터 다시하기"):
        st.session_state.clear()
        change_page("home")

# ==========================================
# 5. 메인 앱 실행부
# ==========================================

def main():
    init_session_state()
    
    if st.session_state.page == "home":
        render_home_page()
    elif st.session_state.page == "adj":
        render_adj_page()
    elif st.session_state.page == "noun":
        render_noun_page()
    elif st.session_state.page == "result":
        render_result_page()

if __name__ == "__main__":
    st.set_page_config(page_title="나의 키워드", page_icon="🌹", layout="wide")
    main()

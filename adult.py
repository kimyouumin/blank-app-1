import streamlit as st

# ==========================================
# 1. 데이터 영역 (Data Configuration)
# ==========================================

# 새로 추가된 가치관 데이터 (6개)
VALUES = ["용기", "성장", "자유", "도전", "연결", "희망"]
VALUES_DATA = {
    "용기": {
        "icon": "https://i.ibb.co/JFRyG4XF/courage.png",
        "desc": "두려움 속에서도<br>한 걸음 앞으로<br>나아가는 힘"
    },
    "성장": {
        "icon": "https://i.ibb.co/yn47G1Jd/grow.png",
        "desc": "작은 순간들이<br>모여 만드는<br>단단한 하루"
    },
    "자유": {
        "icon": "https://i.ibb.co/vxD8zR3v/freedom.png",
        "desc": "나답게 선택하고<br>나아갈 수 있는<br>당신의 권리"
    },
    "도전": {
        "icon": "https://i.ibb.co/fYPfjC21/challenge.png",
        "desc": "새로운 길 위에서<br>스스로를 믿고<br>시작하는 마음"
    },
    "연결": {
        "icon": "https://i.ibb.co/S4fgRTkQ/link.png",
        "desc": "함께하는 순간들이<br>만들어가는<br>따뜻한 관계"
    },
    "희망": {
        "icon": "https://i.ibb.co/8DvMs44h/hope.png",
        "desc": "지금 이 순간에도<br>피어나는<br>작은 가능성"
    }
}

ADJ_WORDS_LIST = [
    "빛나는", "뜨거운", "행복한", "찬란한", "설레는", "특별한",
    "푸르른", "나만의", "성장의", "무한한", "눈부신", "새로운"
]

NOUNS = ["첫걸음", "가능성", "청춘", "비상"]
NOUNS_DATA = {
    "첫걸음": {
        "icon": "https://i.ibb.co/vxXb6qr3/80155699-F795-4231-87-EF-5-A94-F9-B88455.png",
        "desc": "두려움 속에서도<br>한 걸음 앞으로<br>나아가는 힘",
        "image":"https://i.ibb.co/Y74nCHLQ/Talk-File.png", 
        "color": "rgba(240, 208, 16, 0.9)",       # 원래 장미 색상
        "text_color": "#3962AD",                  # 원래 책갈피 배경색(파란색)
        "bg_img": "https://i.ibb.co/svNWnR89/firststep.png"
    },
    "가능성": {
        "icon": "https://i.ibb.co/sJvzv6Tm/B9-AAD50-B-C09-F-465-A-ABF4-18-E186-D8-E65-B.png",
        "desc": "작은 순간들이<br>모여 만드는<br>단단한 하루",
        "image": "https://i.ibb.co/GvgnR60T/Talk-File.png",
        "color": "rgba(255, 255, 255, 0.9)",      # 원래 장미 색상(흰색)
        "text_color": "#2C6B37",                  # 원래 책갈피 배경색(초록색)
        "bg_img": "https://i.ibb.co/sdL17hZD/IMG-0215.png"
    },
    "청춘": {
        "icon": "https://i.ibb.co/V0YYtKps/6-F7-B3-B88-2-C79-48-FC-AE3-D-C2397-C63-C62-D.png",
        "desc": "나답게 선택하고<br>나아갈 수 있는<br>당신의 권리",
        "image": "https://i.ibb.co/5h3dGKNn/Talk-File.png",
        "color": "rgba(120, 24, 22, 0.9)",        # 원래 장미 색상(검붉은색) 
        "text_color": "#EAD531",                  # 원래 책갈피 배경색(노란색)
        "bg_img": "https://i.ibb.co/jvrxCPpx/youth.png"
    },
    "비상": {
        "icon": "https://i.ibb.co/QF4qQRBm/D5-D9-CEEB-936-C-4687-9215-4042-E53-A0-F1-F.png",
        "desc": "새로운 길 위에서<br>스스로를 믿고<br>시작하는 마음",
        "image": "https://i.ibb.co/KZJpbst/Talk-File.png",
        "color": "rgba(16, 29, 56, 0.9)",         # 원래 장미 색상(남색) 
        "text_color": "#EAAAC9",                  # 원래 책갈피 배경색(분홍색)
        "bg_img": "https://i.ibb.co/3ygK4PQ5/bisang.png"
    },
}

# ==========================================
# 2. 상태 관리 및 유틸리티 함수
# ==========================================

def init_session_state():
    # value(가치관) 상태 추가
    defaults = {"page": "home", "name": "", "value": "", "adj": "", "noun": ""}
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
    """전체 요소(제목, 본문, 버튼 등)에 '고운 돋움' 폰트 강제 적용"""
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
        
        /* 버튼 스타일 통일 */
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
            transform: scale(1.02); 
            background-color: #E2E8F0 !important;
        }

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
        </style>
    """, unsafe_allow_html=True)

def apply_card_css():
    """가치관 및 명사 페이지 공통 카드 스타일"""
    apply_dark_bg_css()
    st.markdown("""
        <style>
        div.stButton { margin-top: -16px !important; }

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

def apply_result_css(board_color, bg_url, text_color):
    apply_font()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{bg_url}"); background-size: cover;
            background-position: center; background-attachment: fixed;
        }}
        .block-container {{
            /* 배경색에 이미 rgba와 투명도가 포함되어 있습니다 */
            background-color: {board_color}; 
            border-radius: 30px;
            padding: 50px 30px; box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2); 
            max-width: 600px !important; 
            margin-top: 80px;
            text-align: center; color: {text_color};
            /* 보드 내부 요소들의 글자색 강제 적용 */
        }}
        .block-container h1, .block-container h3 {{
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
# 4. 페이지 렌더링 함수 모음
# ==========================================

def render_home_page():
    apply_home_css()
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    col1, spacer, col2 = st.columns([1, 0.1, 1])
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
        
        if st.button("검사 시작하기 →", key="start_btn"):
            if not name.strip(): 
                st.warning("이름을 입력해주세요!")
            else:
                st.session_state.name = name.strip()
                # 홈 화면 다음은 가치관(value) 선택 페이지로 이동
                change_page("value")

    with col2:
        st.markdown("""
            <div class='quote'>
                "흐리고 어두운 날에도 피어나는 장미처럼,<br>
                당신의 이야기도 언젠가 아름답게 피어날 거에요."
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="display: flex; justify-content: center;">
                <img src="https://i.ibb.co/zTxK90QJ/IMG-0203.jpg" 
                     style="width: 480px; height: 320px; object-fit: cover;">
            </div>
        """, unsafe_allow_html=True)

def render_value_page():
    """새로 추가된 가치관 선택 페이지"""
    apply_card_css()
    st.markdown("<br>", unsafe_allow_html=True)

    # --- 장미 진행 가이드 (꽃봉오리) ---
    _, img_col, _ = st.columns([1, 0.2, 1])
    with img_col:
        st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 20px;">
            <img src="https://i.ibb.co/5xsSsqX5/IMG-0209.jpg" style="width: 45px; height: auto; margin-bottom: 5px;">
            <p style='color: #94A3B8; font-size: 13px; margin: 0;'>1 / 3 단계</p>
        </div>
    """, unsafe_allow_html=True)
    # -----------------------------------
    
    st.markdown("<h3 style='text-align: center; font-weight: 600; color: #FFFFFF;'>당신이 중요하게 생각하는 가치는 무엇인가요?</h3>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center; color: #CBD5E1; font-size: 15px; line-height: 1.6;'>
            가장 마음에 와닿는 가치관을 확인하고,<br>
            하단의 <b>'이 가치관 선택'</b>을 눌러주세요.
        </p>
    """, unsafe_allow_html=True)
    st.write("---")
    
    # 총 6개를 3개씩 2줄로 배치
    for row in range(2):
        cols = st.columns(3)
        for col in range(3):
            idx = row * 3 + col
            if idx < len(VALUES):
                val = VALUES[idx]
                data = VALUES_DATA[val]
                
                with cols[col]:
                    st.markdown(f"""
                    <div style='
                        background-color: #FFFFFF; border: 1px solid #E2E8F0; border-bottom: none;
                        padding: 40px 15px; text-align: center; height: 250px;
                        display: flex; flex-direction: column; justify-content: center; align-items: center;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 0px; 
                    '>
                        <img src='{data["icon"]}' width='35' style='margin-bottom: 25px;'/>
                        <div style='font-size: 20px; font-weight: 600; color: #1e293b; margin-bottom: 15px;'>{val}</div>
                        <div style='font-size: 13px; color: #64748b; line-height: 1.6;'>{data["desc"]}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button("이 가치관 선택", key=f"btn_val_{val}", use_container_width=True, type="primary"):
                        st.session_state.value = val
                        change_page("adj")
        st.markdown("<br>", unsafe_allow_html=True) # 줄바꿈 여백 추가

    st.write("---")
    back_col, _, _ = st.columns([1, 4, 1])
    with back_col:
        if st.button("← 뒤로", key="back_to_home_from_val"): 
            change_page("home")

def render_adj_page():
    apply_adj_css()
    st.markdown("<br>", unsafe_allow_html=True)

    # --- 장미 진행 가이드 (개화 중) ---
    _, img_col, _ = st.columns([1, 0.2, 1])
    with img_col:
        st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 20px;">
            <img src="https://i.ibb.co/27cPzfYm/IMG-0210.jpg" style="width: 45px; height: auto; margin-bottom: 5px;">
            <p style='color: #94A3B8; font-size: 13px; margin: 0;'>2 / 3 단계</p>
        </div>
    """, unsafe_allow_html=True)
    # -----------------------------------
    
    st.markdown("<h2 style='text-align: center; color: #FFFFFF;'>✨스물에 가장 걸맞는 형용사를 골라주세요 ✨</h2>", unsafe_allow_html=True)
    st.write("---")
    
    cols = st.columns(3)
    for i, adj in enumerate(ADJ_WORDS_LIST):
        with cols[i % 3]:
            if st.button(adj, use_container_width=True, type="primary", key=f"adj_{i}"): 
                st.session_state.adj = adj
                change_page("noun")
                
    st.write("---")
    back_col, _, _ = st.columns([1, 4, 1])
    with back_col:
        # 형용사 페이지의 뒤로가기는 이제 가치관(value) 페이지로 향함
        if st.button("← 뒤로", key="back_to_val"): 
            change_page("value")

def render_noun_page():
    apply_card_css()
    st.markdown("<br>", unsafe_allow_html=True)

    # --- 장미 진행 가이드 (만개) ---
    _, img_col, _ = st.columns([1, 0.2, 1])
    with img_col:
        st.markdown("""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 20px;">
            <img src="https://i.ibb.co/MD31QLnv/IMG-0211.jpg" style="width: 45px; height: auto; margin-bottom: 5px;">
            <p style='color: #94A3B8; font-size: 13px; margin: 0;'>3 / 3 단계</p>
        </div>
    """, unsafe_allow_html=True)
    # -----------------------------------
    
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
                background-color: #FFFFFF; border: 1px solid #E2E8F0; border-bottom: none;
                padding: 40px 15px; text-align: center; height: 250px;
                display: flex; flex-direction: column; justify-content: center; align-items: center;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 0px; 
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
        if st.button("← 뒤로", key="back_to_adj"): 
            change_page("adj")

def render_result_page():
    data = NOUNS_DATA.get(st.session_state.noun)
    if not data:
        st.error("데이터 오류")
        if st.button("홈으로"): change_page("home")
        return

    # 배경색과 글자색 인자를 모두 전달
    apply_result_css(data["color"], data["bg_img"], data.get("text_color", "#333"))
    
    st.markdown(f"<h1 style='text-align: center;'>🌹 당신을 위한 한 마디 🌹</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try: st.image(data["image"], use_container_width=True)
        except: st.warning("이미지 확인 필요")
            
    st.markdown("<br>", unsafe_allow_html=True)
    # 가치관, 형용사, 명사가 모두 포함된 응원 문구
    st.markdown(f"<h3 style='text-align: center;'><b>{st.session_state.name}</b>님의 <b>{st.session_state.value}</b>의 가치가 담긴<br><br><b>{st.session_state.adj} {st.session_state.noun}</b> 응원합니다!</h3>", unsafe_allow_html=True)
    st.balloons()
    
    if st.button("🔄 처음부터 다시하기", key="restart_btn"):
        st.session_state.clear()
        change_page("home")

# ==========================================
# 5. 메인 앱 실행부
# ==========================================

def main():
    init_session_state()
    
    # 페이지 라우팅
    if st.session_state.page == "home": 
        render_home_page()
    elif st.session_state.page == "value": 
        render_value_page()
    elif st.session_state.page == "adj": 
        render_adj_page()
    elif st.session_state.page == "noun": 
        render_noun_page()
    elif st.session_state.page == "result": 
        render_result_page()

if __name__ == "__main__":
    st.set_page_config(page_title="나의 키워드", page_icon="🌹", layout="wide")
    main()

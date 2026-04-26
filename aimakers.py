import streamlit as st
from io import BytesIO

# ─────────────────────────────────────────────
# 페이지 기본 설정
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="🔮 AI 마법 거울",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# 1. 테마 데이터베이스 (각 계열별 디자인)
# ─────────────────────────────────────────────
THEMES = {
    "default": {
        "bg_img": "none",
        "bg_gradient": "linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%)",
        "block_bg": "white",
        "text_main": "#3b0764",
        "btn_bg": "#a855f7",
        "btn_hover": "#7e22ce",
        "border": "#d8b4fe",
        "progress": "#a855f7"
    },
    "A": { # 지혜의 서고
        "bg_img": "url('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjEwMjBfNTkg%2FMDAxNjY2MjYzNjEzODc1.6bB7jVJM22VH18FbqVUkvl9lbwsQOddk_qmaGQR_v1Ig.-JyIK3km2ZAkaY6suPlliHs3iHLcF12QsLcP-qjpCsgg.JPEG.goodsemedu%2FScreenshot_2022-10-20_at_19.59.24.JPG&type=sc960_832')",
        "bg_gradient": "none",
        "block_bg": "rgba(255, 250, 240, 0.95)",
        "text_main": "5D4037",
        "btn_bg": "#4E342E",
        "btn_hover": "#3E2723",
        "border": "rgba(255, 255, 255, 0.3)",
        "progress": "#4E342E"
    },
    "B": { # 발명의 작업실 
        "bg_img": "url('https://plus.unsplash.com/premium_photo-1661434779070-cf8fc0e253ab?q=80&w=1172&auto=format&fit=crop')",
        "bg_gradient": "none",
        "block_bg": "rgba(13, 27, 42, 0.95)",
        "text_main": "#F8FCFF",
        "btn_bg": "#2F9AC2",
        "btn_hover": "#4FB3D3",
        "border": "rgba(0, 180, 216, 0.4)",
        "progress": "#2F9AC2"
    },
    "C": { # 예술의 정원
        "bg_img": "linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)), url('https://i.pinimg.com/1200x/28/0c/9f/280c9f73f62a4e4e0bceaae4a7248cfb.jpg')",
        "bg_gradient": "none",
        "block_bg": "rgba(241, 248, 233, 0.95)",
        "text_main": "#1B5E20",
        "btn_bg": "#81C784",
        "btn_hover": "#1B5E20",
        "border": "rgba(46, 125, 50, 0.18)",
        "progress": "#388E3C"
    }
}

def apply_theme(cat_key):
    t = THEMES.get(cat_key, THEMES["default"])
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    html, body, [class*="css"] {{ font-family: 'Gowun Batang', 'Noto Sans KR', sans-serif; }}

    /* 전체 배경 */
    [data-testid="stAppViewContainer"] {{
        background-image: {t['bg_img']} !important;
        background: {t['bg_gradient']};
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}
   
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0); }}

    /* 메인 플로팅 컨테이너 */
    .block-container {{
        background-color: {t['block_bg']} !important;
        padding: 3rem 4rem !important;
        border-radius: 40px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
        margin-top: 50px;
        margin-bottom: 50px;
        border: 2px solid {t['border']};
    }}

    /* 텍스트 색상 */
    h1, h2, h3, p, span, .stMarkdown, .question-number {{ color: {t['text_main']} !important; }}

    /* 버튼 스타일 */
    div.stButton > button {{
        background-color: {t['btn_bg']} !important;
        color: #ffffff !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 15px !important;
        font-weight: 700 !important;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
        height: auto !important;
        white-space: normal !important;
    }}
    div.stButton > button:hover {{
        background-color: {t['btn_hover']} !important;
        transform: translateY(-2px);
    }}

    /* 진행률 바 */
    .stProgress > div > div > div {{ background-color: {t['progress']} !important; }}

    /* 질문 박스 및 카드 UI */
    .question-box {{
        background: rgba(255, 255, 255, 0.1); border-radius: 20px;
        padding: 30px; border: 1px solid {t['border']}; text-align: center; margin-bottom: 30px;
    }}
    .custom-card {{
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 25px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
        overflow: hidden; border: 1px solid {t['border']};
        transition: transform 0.3s; margin: 10px auto; width: 100%;
        display: flex; flex-direction: column; align-items: center;
    }}
    .card-text {{
        text-align: center; padding: 15px 10px; font-weight: bold;
        color: {t['text_main']}; width: 100%; font-size: 1.1rem;
    }}
    [data-testid="stImage"] {{ border-radius: 25px; padding: 10px !important; }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 2. 데이터 정의 (직업 결과, 카테고리 정보)
# ─────────────────────────────────────────────
magic_data = {
    "A": {
        "INFJ": ["신비로운 예언가", "상담 심리사", "사람의 마음속 깊은 곳을 비추는 등불이로다."],
        "INFP": ["꿈꾸는 음유시인", "소설가/작가", "그대의 따뜻한 문장이 세상을 치유하는구나."],
        "INTJ": ["고대의 현자", "전략 기획자", "보이지 않는 미래를 설계하는 눈을 가졌도다."],
        "INTP": ["지혜의 탐구자", "인문학 연구원", "진리를 향한 그대의 갈증이 세상을 깨우는도다."],
        "ISFJ": ["서고의 수호자", "사회복지사", "묵묵히 자리를 지키는 그대의 헌신이 아름답구나."],
        "ISFP": ["영혼의 조각가", "전시 기획자", "그대의 손끝에서 세상의 미학이 완성되도다."],
        "ISTJ": ["기록 보관소장", "법무사/사서", "한 치의 오차도 없는 정직함이 그대의 힘이로다."],
        "ISTP": ["무명의 기술자", "고고학자", "복잡한 세상을 단순하게 정리하는 기술을 가졌구나."],
        "ENFJ": ["요정들의 왕", "교육자", "사람들을 이끄는 따뜻한 리더십이 참으로 눈부시도다."],
        "ENFP": ["축제의 전령사", "홍보 전문가", "그대의 밝은 미소가 닫힌 문을 여는 마법이로다."],
        "ENTJ": ["제국의 총사령관", "경영자/CEO", "대륙을 호령하는 그대의 결단력이 세상을 움직이리라."],
        "ENTP": ["지식의 모험가", "변호사/정치인", "편견을 깨뜨리는 그대의 논리가 참으로 날카롭구나."],
        "ESFJ": ["평화의 중재자", "인사 전문가", "모두를 화합하게 하는 그대의 마음이 따뜻하도다."],
        "ESFP": ["빛의 무희", "엔터테이너", "그대의 존재 자체가 세상의 기쁨이자 축제로다."],
        "ESTJ": ["서고의 총책임자", "행정 전문가", "흐트러짐 없는 그대의 질서가 세상을 바로잡는도다."],
        "ESTP": ["전설의 탐험가", "기자/특파원", "거침없이 나아가는 그대의 용기가 길을 만드리라."]
    },
    "B": {
        "INFJ": ["마법 원리 분석가", "데이터 과학자", "데이터 속 숨겨진 의미를 찾아내는 통찰력이 있구나."],
        "INFP": ["낭만적 천문학자", "환경 엔지니어", "지구를 사랑하는 그대의 마음이 기술을 숨 쉬게 하는도다."],
        "INTJ": ["전설의 연금술사", "시스템 반도체 설계자", "보이지 않는 칩 위에 새로운 세상을 설계할 자로다."],
        "INTP": ["마법 공학자", "AI 알고리즘 개발자", "끝없는 질문 끝에 진리의 답을 찾아낼 자로다."],
        "ISFJ": ["도구의 수호자", "품질 관리 엔지니어", "작은 결함도 놓치지 않는 세심함이 신뢰를 만드는도다."],
        "ISFP": ["감성 발명가", "제품 디자이너", "기술에 온기를 불어넣는 그대의 감각이 특별하구나."],
        "ISTJ": ["철저한 시계공", "임베디드 엔지니어", "정교한 설계로 마법 같은 기계를 만드는도다."],
        "ISTP": ["기계의 지배자", "로봇 공학자", "무엇이든 고쳐내는 그대의 손은 마법사의 손이로다."],
        "ENFJ": ["발명 연합 의장", "기술 교육자", "어려운 기술을 희망으로 바꾸는 힘을 가졌구나."],
        "ENFP": ["아이디어 뱅크", "혁신가/기획자", "그대의 상상이 미래를 바꾸는 시작점이 되리라."],
        "ENTJ": ["기술 제국의 왕", "기술 경영인", "거대한 시스템을 통치하는 카리스마를 가졌도다."],
        "ENTP": ["괴짜 발명왕", "스타트업 창업가", "불가능을 비웃으며 새로운 가치를 창출하겠구나."],
        "ESFJ": ["발명의 협력자", "기술 영업 전문가", "사람과 기술을 잇는 가장 튼튼한 다리가 되도다."],
        "ESFP": ["실험실 분위기 메이커", "테크 유튜버", "기술의 즐거움을 온 세상에 알릴 운명이로다."],
        "ESTJ": ["공정의 감독관", "제조 공정 전문가", "효율적인 흐름으로 세상을 막힘없이 돌리겠구나."],
        "ESTP": ["필드의 해결사", "현장 엔지니어", "어떤 위기 상황도 정면 돌파할 에너지를 가졌도다."]
    },
    "C": {
        "INFJ": ["영혼의 화가", "아트 디렉터", "작품 속에 깊은 철학을 담아내는 눈을 가졌도다."],
        "INFP": ["숲속의 몽상가", "일러스트레이터", "그대의 그림은 지친 영혼을 달래는 쉼터로다."],
        "INTJ": ["건축의 거장", "공간 디자이너", "조화와 완벽함을 갖춘 그대의 미학이 참으로 높도다."],
        "INTP": ["추상 예술가", "사운드 디자이너", "소리와 빛의 근원을 탐구하는 천재성을 가졌구나."],
        "ISFJ": ["정원의 관리인", "큐레이터", "소중한 가치를 보존하고 가꾸는 그대가 귀하도다."],
        "ISFP": ["빛과 색의 조각가", "비주얼 디자이너", "찰나의 아름다움을 영원으로 기록할 재능이로다."],
        "ISTJ": ["고전 무용수", "교향악단 연주자", "반복되는 연습 끝에 완벽한 선율을 빚어내는구나."],
        "ISTP": ["무대 장인", "영상 편집 전문가", "흩어진 조각들을 모아 하나의 환상을 만드는도다."],
        "ENFJ": ["예술학교 교장", "예술 치료사", "예술로 상처받은 마음을 어루만지는 고귀한 자로다."],
        "ENFP": ["무지개 마술사", "공연 기획자", "세상에 즐거움을 퍼뜨리는 그대가 곧 예술이로다."],
        "ENTJ": ["예술단의 단장", "콘텐츠 프로듀서", "세상을 열광시킬 트렌드를 이끄는 선구자로다."],
        "ENTP": ["파격의 예술가", "팝아트 작가", "기존의 틀을 부수는 그대의 도발이 신선하구나."],
        "ESFJ": ["정원의 호스트", "파티 플래너", "사람들을 행복하게 만드는 법을 아는 마법사로다."],
        "ESFP": ["축제의 주인공", "뮤지컬 배우", "그대의 몸짓 하나에 세상이 환호하리라."],
        "ESTJ": ["예술제 위원장", "무대 감독", "완벽한 공연을 만드는 그대의 통솔력이 놀랍도다."],
        "ESTP": ["거리의 예술가", "스포츠 스타", "역동적인 그대의 에너지가 세상을 흔들어 놓으리라."]
    }
}

CAT_INFO = {
    "A": {"label": "A. 지혜의 서고",  "emoji": "📚", "ex":"📚 글을 읽거나 역사·사회 얘기를 할 때!","image": "https://i.ibb.co/tPN8RhDy/IMG-4001.jpg"},
    "B": {"label": "B. 발명의 작업실", "emoji": "⚙️", "ex":"⚙️ 과학 실험을 하거나 수학 문제를 풀 때!","image": "https://i.ibb.co/pBWPnr23/IMG-4002.jpg"},
    "C": {"label": "C. 예술의 정원",  "emoji": "🎨", "ex":"🎨 그림 그리거나 음악·춤을 즐길 때!","image": "https://i.ibb.co/N2r7RTp1/IMG-4003.jpg"},
}

# ─────────────────────────────────────────────
# 3. 질문 데이터 구조 변경 (UI 카드용)
# 구조: (질문, [(카드제목, 이미지URL, 버튼텍스트), ...], 차원)
# ─────────────────────────────────────────────
QUESTIONS = {
    "A": [
        ("Q1. 도서관에 무서운 마녀가 나타났다! 너라면?",
         [("함께 맞서 싸운다", "https://i.ibb.co/VWPfxcNx/IMG-3905.png", "마을 사람들을 모아 함께 맞서 싸운다"),
          ("약점을 연구한다", "https://i.ibb.co/5gRfygT5/IMG-3907.png", "혼자 조용히 마녀의 약점을 연구한다")], "EI"),
        ("Q2. 오래된 마법서를 발견했다. 너는 무엇을 볼래?",
         [("역사적 사실", "https://i.ibb.co/TDcmsVnQ/40-F69-F62-71-B0-4852-8236-CB20-B90-A416-E.jpg", "책에 적힌 역사적 사실과 기록들"),
          ("신비로운 미래", "https://i.ibb.co/Kpnpgd3m/IMG-3976.png", "이 마법이 불러올 신비로운 미래")], "SN"),
        ("Q3. 마녀에게 잡힌 친구가 울고 있다. 너는?",
         [("냉철한 계획", "https://i.ibb.co/fGLNJxS6/IMG-0155.jpg", "냉철하게 탈출 계획을 세워준다"),
          ("따뜻한 위로", "https://i.ibb.co/Z1Lfxznw/IMG-3911.png", "친구를 꽉 안아주며 위로해준다")], "TF"),
        ("Q4. 마법 주문을 외워야 한다면?",
         [("완벽한 암기", "https://i.ibb.co/1tHv7KKW/D95520-F2-6-DC3-4222-AE19-55-B51-A3-DCFE3.png", "주문서를 꼼꼼히 읽고 순서대로 외운다"),
          ("즉흥적인 감각", "https://i.ibb.co/V0xrkrMb/IMG-3982.jpg", "느낌이 오는 대로 즉흥적으로 외친다")], "JP"),
    ],
    "B": [
        ("Q1. 마을의 거대 로봇이 고장 났다! 너라면?",
         [("기술자 소집", "https://i.ibb.co/xSB6CmJM/IMG-3983.jpg", "기술자들을 소집해 회의를 연다"),
          ("혼자 수리", "https://i.ibb.co/VYYpFqV8/IMG-3984.png", "방 안에 틀어박혀 혼자 부품을 뜯어본다")], "EI"),
        ("Q2. 새로운 발명품 설계도를 보게 되었다. 너는?",
         [("정확한 수치", "https://i.ibb.co/7Ny1ZfGJ/IMG-3988.jpg", "설계도의 수치가 정확한지 체크한다"),
          ("멋진 상상", "https://i.ibb.co/Mk6TcRJQ/D2-DB53-DE-CDC2-4-B32-85-A0-8-DF4-DF7-A376-D.png", "이 발명품이 바꿀 멋진 세상을 상상한다")], "SN"),
        ("Q3. 로봇이 슬픈 눈을 하고 쳐다본다면?",
         [("결함 수리", "https://i.ibb.co/dsg9zqqx/IMG-3919.png", "기계적 결함이 있는지 즉시 수리한다"),
          ("마음 걱정", "https://i.ibb.co/tw4W1W1s/IMG-3920.png", "로봇의 마음이 아픈 건 아닐지 걱정한다")], "TF"),
        ("Q4. 중요한 실험을 앞두고 너는?",
         [("단계별 정리", "https://i.ibb.co/v4GZV4LL/IMG-3975.png", "실험 단계를 1번부터 10번까지 정리한다"),
          ("일단 실행", "https://i.ibb.co/4g3qw91r/IMG-3990.jpg", "일단 버튼을 누르며 직접 배워본다")], "JP"),
    ],
    "C": [
        ("Q1. 숲속에서 요정들의 축제가 열렸다! 너는?",
         [("함께 춤추기", "https://i.ibb.co/k2K1m3QJ/IMG-3986.jpg", "무대 한가운데서 춤을 추며 즐긴다"),
          ("조용히 관찰", "https://i.ibb.co/xtFMDCBB/IMG-3991.jpg", "조용한 구석에서 축제를 관찰한다")], "EI"),
        ("Q2. 신비로운 꽃을 발견했다. 너는?",
         [("형태 관찰", "https://i.ibb.co/TMDqQjhX/IMG-3981.png", "꽃잎의 개수와 모양을 관찰한다"),
          ("전설 상상", "https://i.ibb.co/sLK0zqc/IMG-3925.png", "이 꽃에 담긴 전설을 떠올려본다")], "SN"),
        ("Q3. 요정 여왕이 내 작품을 평가한다면?",
         [("솔직한 피드백", "https://i.ibb.co/d4qF8R9J/IMG-3926.png", "고쳐야 할 점을 솔직하게 말해주길 바란다"),
          ("따뜻한 칭찬", "https://i.ibb.co/G1RY2Ph/IMG-3927.png", "내 노력을 칭찬해주길 바란다")], "TF"),
        ("Q4. 내일 열릴 공연을 위해 너는?",
         [("완벽한 스케줄", "https://i.ibb.co/6c4wXj7F/IMG-3992.png", "연습 스케줄을 완벽하게 짜놓는다"),
          ("그날의 영감", "https://i.ibb.co/XxMQBf6k/IMG-3929.png", "그날의 영감에 따라 공연하기로 한다")], "JP"),
    ],
}

# ─────────────────────────────────────────────
# MBTI 계산 및 상태 초기화
# ─────────────────────────────────────────────
def calc_mbti(answers):
    first  = {"EI": "E", "SN": "S", "TF": "T", "JP": "J"}
    second = {"EI": "I", "SN": "N", "TF": "F", "JP": "P"}
    result = ""
    for idx, dim in answers:
        result += first[dim] if idx == 0 else second[dim]
    return result

def init_state():
    defaults = {
        "step": "start", "cat": None, "name": "", "q_idx": 0,
        "answers": [], "mbti": None, "fairy_job": "", "real_job": "", "prophecy": ""
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def reset_state():
    for k in list(st.session_state.keys()): del st.session_state[k]
    init_state()

init_state()
apply_theme(st.session_state.cat) # 테마 상시 적용

# ═══════════════════════════════════════════════════════════
# ① 시작 화면 — 계열(카테고리) 선택
# ═══════════════════════════════════════════════════════════
if st.session_state.step == "start":
    st.markdown('<h1 style="text-align: center;">🔮 AI 마법 거울</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">동화 속 세상에 온 걸 환영해! 너는 어떨 때 가장 즐거워?</p>', unsafe_allow_html=True)

    cols = st.columns(3)
    for col, (cat_key, info) in zip(cols, CAT_INFO.items()):
        with col:
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            try:
                st.image(info["image"], use_container_width=True)
            except Exception:
                st.write(f"<div style='font-size:3rem; text-align:center;'>{info['emoji']}</div>", unsafe_allow_html=True)
           
            st.markdown(f'<div class="card-text">{info["label"]}</div>', unsafe_allow_html=True)
            st.caption(f"<div style='text-align:center; padding-bottom:10px;'>{info['ex']}</div>", unsafe_allow_html=True)
           
            if st.button("이 문으로 들어가기", key=f"cat_{cat_key}", use_container_width=True):
                st.session_state.cat  = cat_key
                st.session_state.step = "name"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════
# ② 이름 입력 화면
# ═══════════════════════════════════════════════════════════
elif st.session_state.step == "name":
    cat  = st.session_state.cat
    info = CAT_INFO[cat]

    st.markdown('<h1 style="text-align: center;">🔮 AI 마법 거울</h1>', unsafe_allow_html=True)
   
    st.markdown(f"""
    <div class="question-box">
        <h3>{info['emoji']} {info['label']} 에 오신 걸 환영합니다!</h3>
        <p>✨ 마법 거울이 그대의 이름을 묻고 있어요</p>
    </div>""", unsafe_allow_html=True)

    name_input = st.text_input("너의 이름은?", placeholder="이름을 입력하세요", value=st.session_state.name)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✨ 모험 시작!", use_container_width=True):
            if name_input.strip():
                st.session_state.name    = name_input.strip()
                st.session_state.step    = "question"
                st.session_state.q_idx   = 0
                st.session_state.answers = []
                st.rerun()
            else:
                st.warning("이름을 입력해주렴!")
    with col2:
        if st.button("← 문 선택으로", use_container_width=True):
            reset_state()
            st.rerun()

# ═══════════════════════════════════════════════════════════
# ③ 질문 화면 (이미지 카드 UI 적용)
# ═══════════════════════════════════════════════════════════
elif st.session_state.step == "question":
    cat       = st.session_state.cat
    q_idx     = st.session_state.q_idx
    questions = QUESTIONS[cat]
    total     = len(questions)

    # 타이틀 및 진행바
    st.markdown(f"<h1 style='text-align: center;'>{CAT_INFO[cat]['label']}</h1>", unsafe_allow_html=True)
    st.progress((q_idx + 1) / total)
    st.markdown(f"<div class='question-number' style='text-align:right'>질문 {q_idx + 1} / {total}</div>", unsafe_allow_html=True)

    q_text, choices, dim = questions[q_idx]

    # 질문 박스
    st.markdown(f"""
    <div class="question-box">
        <h2 style="font-size: 22px; line-height: 1.5; margin: 0;">{q_text}</h2>
    </div>""", unsafe_allow_html=True)

    # 선택지 렌더링 (카드 이미지 + 버튼 조합)
    col1, col2 = st.columns(2, gap="large")
   
    for idx, (col, choice) in enumerate(zip([col1, col2], choices)):
        card_title, img_url, btn_text = choice
        with col:
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            st.image(img_url, use_container_width=True)
            st.markdown(f'<div class="card-text">{card_title}</div>', unsafe_allow_html=True)
           
            # 버튼 클릭 시 다음 로직으로 이동
            if st.button(btn_text, use_container_width=True, key=f"q{q_idx}_c{idx}"):
                st.session_state.answers.append((idx, dim))
               
                if q_idx + 1 < total:
                    st.session_state.q_idx += 1
                    st.rerun()
                else:
                    # 모든 질문 완료 시 결과 계산
                    mbti = calc_mbti(st.session_state.answers)
                    result = magic_data[cat][mbti]
                    st.session_state.mbti      = mbti
                    st.session_state.fairy_job = result[0]
                    st.session_state.real_job  = result[1]
                    st.session_state.prophecy  = result[2]
                    st.session_state.step      = "result"
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← 처음으로 돌아가기", use_container_width=True):
        reset_state()
        st.rerun()

# ═══════════════════════════════════════════════════════════
# ④ 결과 화면
# ═══════════════════════════════════════════════════════════
elif st.session_state.step == "result":
    cat       = st.session_state.cat
    mbti      = st.session_state.mbti
    name      = st.session_state.name
    fairy_job = st.session_state.fairy_job
    real_job  = st.session_state.real_job
    prophecy  = st.session_state.prophecy

    st.balloons()
    st.markdown('<h1 style="text-align: center;">✨ 운명의 예언서</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center;"><b>{name}</b> 님의 진로 추천 결과입니다</p>', unsafe_allow_html=True)

    # ── 계열 이미지 출력
    try:
        img_map = {"A": "tarot1.jpg", "B": "tarot2.jpg", "C": "tarot3.jpg"}
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            st.image(img_map[cat], use_container_width=True, caption=CAT_INFO[cat]["label"])
    except Exception:
        st.write(f"<div style='font-size:3rem; text-align:center;'>{CAT_INFO[cat]['emoji']}</div>", unsafe_allow_html=True)

    st.divider()

    st.markdown(f"### 나의 MBTI 유형: **{mbti}**")
    st.markdown(f"선택 계열: **{CAT_INFO[cat]['label']}**")

    st.divider()

    st.success(f"✨ {name} 님의 운명적 예언")
    st.markdown(f"#### 🏰 동화 속 당신은: [{fairy_job}]")
    st.markdown(f"#### 💼 현실에서의 모습은: **{real_job}**")

    st.info(
        f"📜 마법 거울의 한마디:\n\n"
        f"'{name}'아, {prophecy}\n\n"
        f"지금의 그 마음을 잃지 않는다면 현실에서도 멋진 **{real_job}**이 될 것이로다!"
    )

    st.divider()

    if st.button("🔄 다시하기", use_container_width=True):
        reset_state()
        st.rerun()

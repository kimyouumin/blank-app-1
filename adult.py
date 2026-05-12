import streamlit as st

# 1. CSS 변수 정의 
BG_첫걸음 = """ 
<style>
.stApp {
    background-color: #F0F2F6; /* 기본 배경색 예시 */
    background-image: url("https://www.transparenttextures.com/patterns/cubes.png"); /* 배경 이미지 예시 */
    background-size: cover;
}
</style>
"""

# 키워드 데이터
adj_words_list = ["빛나는", "따뜻한", "행복한", "찬란한", "설레는", "특별한"]
nouns = ["첫걸음", "가능성", "청춘", "날개"]

# nouns_data 정의 (BG_첫걸음 변수가 위에 정의되어 있어야 합니다)
nouns_data = {
    "첫걸음": {"image": "rose1.png", "bg": BG_첫걸음},
    "가능성": {"image": "rose2.png", "bg": BG_첫걸음},
    "청춘": {"image": "rose3.png", "bg": BG_첫걸음},
    "날개": {"image": "rose4.png", "bg": BG_첫걸음},
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

# 홈 화면
if st.session_state.page == "home":
    st.title("📖 새로운 페이지 📖")
    name = st.text_input("이름을 입력해주세요", value=st.session_state.name)
    if st.button("입장하기"):
        if not name.strip():
            st.warning("이름을 입력해주세요!")
        else:
            st.session_state.name = name.strip()
            go("adj")

# 형용사 선택 
elif st.session_state.page == "adj":
    st.title("단어를 골라주세요 ✨")
    for adj in adj_words_list:
        if st.button(adj):
            st.session_state.adj = adj
            go("noun")
    if st.button("← 뒤로"):
        go("home")

# 명사 선택 
elif st.session_state.page == "noun":
    st.title("단어를 골라주세요 ✨")
    for noun in nouns:
        if st.button(noun):
            st.session_state.noun = noun
            go("result")
    if st.button("← 뒤로"):
        go("adj")

# 결과 화면 
elif st.session_state.page == "result":
    data = nouns_data[st.session_state.noun]
    
    # 배경 스타일 적용
    st.markdown(data["bg"], unsafe_allow_html=True) 
    
    # 이미지 출력 (파일이 같은 경로에 있어야 함)
    try:
        st.image(data["image"])
    except:
        st.error(f"이미지 파일({data['image']})을 찾을 수 없습니다.")
        
    st.title("🌹 당신을 위한 한 마디 🌹")
    st.header(f"{st.session_state.name}님의 {st.session_state.adj} {st.session_state.noun} 응원합니다!")
    
    if st.button("🔄 처음부터"):
        for key, val in defaults.items():
            st.session_state[key] = val
        go("home")

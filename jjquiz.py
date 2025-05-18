import streamlit as st

st.title("🎯 간단 퀴즈 서비스")

# 객관식
st.subheader("1. 객관식 퀴즈: 파이썬의 자료형 중 숫자가 아닌 것은?")
options = ["int", "float", "str", "bool"]
mc_answer = st.radio("답을 골라주세요:", options)

# 주관식
st.subheader("2. 주관식 퀴즈: 파이썬에서 리스트를 만드는 키워드는?")
sa_answer = st.text_input("정답을 입력해주세요:")

if st.button("제출하기"):
    score = 0
    if mc_answer == "str":
        score += 1
        st.success("1번 정답입니다! ⭕")
    else:
        st.error("1번 오답입니다 ❌")

    if sa_answer.strip().lower() == "list":
        score += 1
        st.success("2번 정답입니다! ⭕")
    else:
        st.error("2번 오답입니다 ❌")

    st.info(f"총 점수: {score}/2")

import streamlit as st

st.title("한지영에 대한 퀴즈")

# 객관식
st.subheader("1. 한지영이 좋아하는 음식은?")
options = ["두찜마라로제", "짜장면", "샐러드", "뿌링클"]
mc_answer = st.radio("답을 골라주세요:", options)

# 주관식
st.subheader("2. 한지영이 좋아하는 아이돌 그룹은? (영어로 쓰세요)")
sa_answer = st.text_input("정답을 입력해주세요:")

if st.button("제출하기"):
    score = 0
    if mc_answer == "두찜마라로제":
        score += 1
        st.success("1번 정답")
    else:
        st.error("1번 오답")

    if sa_answer.strip().lower() == "ATEEZ":
        score += 1
        st.success("2번 정답")
    else:
        st.error("2번 오답")

    st.info(f"총 점수: {score}/2")

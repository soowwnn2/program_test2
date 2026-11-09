import streamlit as st

# 1. 퀴즈 데이터
quiz_data = {
    "인상주의": {
        "question": "다음 중 인상주의 화풍의 특징은 무엇인가요?",
        "options": ["1. 정밀한 인체 묘사", "2. 빛과 색채의 표현", "3. 극사실적 표현"],
        "answer": "2",
        "code": "b"
    },
    "추상화": {
        "question": "추상화는 어떤 특징을 가지고 있나요?",
        "options": ["1. 실제 대상을 사실적으로 묘사", "2. 색과 형태로 감정을 표현", "3. 고전적인 원근법 사용"],
        "answer": "2",
        "code": "a"
    },
    "현대미술": {
        "question": "현대 설치미술의 주요 목적은 무엇인가요?",
        "options": ["1. 감정을 억제한 정적 표현", "2. 공간과 상호작용", "3. 전통 재현"],
        "answer": "2",
        "code": "c"
    }
}

# 2. 상태 저장소(Session State) 초기화
# 웹은 버튼을 누를 때마다 새로고침 되므로, 획득한 암호와 현재 방 위치를 저장해두어야 합니다.
if "codes" not in st.session_state:
    st.session_state.codes = []
if "room" not in st.session_state:
    st.session_state.room = "main"

st.title("🎨 미술관 탈출 게임")

# 3. 메인 화면 (복도)
if st.session_state.room == "main":
    st.write("각 전시실에서 퀴즈를 풀어 암호 조각을 모으고, 마지막 방에서 암호를 맞혀 탈출하세요!!")
    st.write(f"**현재 모은 암호 조각: {len(st.session_state.codes)} / 3**")
    
    st.write("---")
    
    # 버튼을 누르면 해당 방으로 이동하도록 상태(room) 변경 후 새로고침(rerun)
    if st.button("1. 인상주의 전시실"):
        st.session_state.room = "인상주의"
        st.rerun()
    if st.button("2. 추상화 전시실"):
        st.session_state.room = "추상화"
        st.rerun()
    if st.button("3. 현대 설치미술 전시실"):
        st.session_state.room = "현대미술"
        st.rerun()
        
    st.write("---")
    if st.button("🚪 4. 마지막 방으로 이동"):
        if len(st.session_state.codes) == 3:
            st.session_state.room = "마지막방"
            st.rerun()
        else:
            st.warning("⚠️ 암호 조각이 부족합니다. 모든 전시실의 퀴즈를 풀어 조각을 3개 모으세요.")

# 4. 퀴즈 화면 (인상주의, 추상화, 현대미술)
elif st.session_state.room in quiz_data:
    topic = st.session_state.room
    q = quiz_data[topic]
    
    st.subheader(f"[{topic} 전시실]")
    st.write(q["question"])
    for opt in q["options"]:
        st.write(opt)
        
    # 터미널 input() 대신 웹 전용 텍스트 입력창 사용
    user_answer = st.text_input("정답 번호를 입력하고 확인 버튼을 누르세요:")
    
    if st.button("정답 확인"):
        if user_answer == q["answer"]:
            if q["code"] not in st.session_state.codes:
                st.session_state.codes.append(q["code"])
                st.success(f"🎉 정답입니다! 암호 조각 '{q['code']}'를 획득했습니다.")
            else:
                st.info("이미 획득한 암호 조각입니다.")
        else:
            st.error("❌ 오답입니다.")
            
    st.write("---")
    if st.button("메인 복도로 돌아가기"):
        st.session_state.room = "main"
        st.rerun()

# 5. 마지막 방 (탈출)
elif st.session_state.room == "마지막방":
    st.subheader("🚪 마지막 방")
    st.write("모은 암호 조각을 조합하여 탈출 암호를 입력하세요.")
    
    escape_code = st.text_input("암호를 입력하세요:").strip().lower()
    
    if st.button("탈출 시도"):
        if escape_code == "bac":
            st.balloons() # 정답 시 풍선 이펙트
            st.success("🎉 암호가 맞았습니다. 미술관에서 탈출에 성공했습니다! 🎉")
        else:
            st.error("❌ 암호가 틀렸습니다.")
            
    st.write("---")
    if st.button("메인 복도로 돌아가기"):
        st.session_state.room = "main"
        st.rerun()

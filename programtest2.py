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

codes_collected = []

def ask_quiz(topic):
    q = quiz_data[topic]
    print()
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    user = input("정답 번호를 입력하세요: ")
    if user == q["answer"]:
        if q["code"] not in codes_collected:
            codes_collected.append(q["code"])
            print(f"정답입니다! 암호 조각 '{q['code']}'를 획득했습니다.")
        else:
            print("이미 획득한 암호 조각입니다.")
    else:
        print("오답입니다.")

def enter_gallery():
    while True:
        print()
        print("1. 인상주의 전시실")
        print("2. 추상화 전시실")
        print("3. 현대 설치미술 전시실")
        print("4. 마지막 방으로 이동 (암호 조각 필요)")
        choice = input("선택: ")

        if choice == "1":
            ask_quiz("인상주의")
        elif choice == "2":
            ask_quiz("추상화")
        elif choice == "3":
            ask_quiz("현대미술")
        elif choice == "4":
            if len(codes_collected) > 0:
                attempt_escape()
                break
            else:
                print("암호 조각이 필요합니다. 먼저 퀴즈를 풀어 암호 조각을 모으세요.")
        else:
            print("잘못된 입력입니다.")

def attempt_escape():
    user_code = input("\n암호를 입력하세요: ").strip().lower()
    correct_code = "bac"

    if user_code == correct_code:
        print("암호가 맞았습니다. 미술관에서 탈출에 성공했습니다!")
    else:
        print("암호가 틀렸습니다. 다시 시도하세요.")
        enter_gallery()

def start_game():
    print("미술관 탈출 게임에 오신 것을 환영합니다.")
    print("각 전시실에서 퀴즈를 풀어 암호 조각을 모으고,")
    print("마지막 방에서 암호를 맞혀 미술관을 탈출하세요!!.")
    enter_gallery()

start_game()
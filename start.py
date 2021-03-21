import random  # 랜덤 모듈 호출


def lotto():  # lotto() 라는 함수 생성
    num = int(random.random() * 36)  # 0부터 36까지의 숫자를 생성
    return num  # 변수 num 을 전달


lotto_array = []  # 배열을 생성하고 변수 선언

while True:
    num = lotto()  # lotto()에서 전달받은 값은 num에 저장

    if num != 0 and num not in lotto_array:  # 변수 num이 0이 아니고 lotto_array 안에 있어 중복되는지 확인
        if len(lotto_array) < 6:  # lotto_array의 길이가 6보다 작을때만 실행
            lotto_array.append(num)  # lotto_array에 num변수 추가
        else:  # lotto_array의 길이가 6보다 크거나 같을때만 실행
            break  # while 문을 강제로 종료

lotto_array.sort()  # lotto_array 작은 수부터 정렬

for num in lotto_array:  # for 문으로 lotto_array에서 값을 하나씩 받아오기
    print(num)  # 받아온 값을 출력

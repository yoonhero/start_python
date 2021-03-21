# 파이썬의 기초

class Calculation():  # 클래스 생성
    def __init__(self, first, second):  # 처음에 실행됨
        self.first = first
        self.second = second

    def add(self):  # 더하기
        result = self.first + self.second
        return result

    def mul(self):  # 곱하기
        result = self.first * self.second
        return result

    def sub(self):  # 빼기
        result = self.first - self.second
        return result

    def div(self):  # 나누기
        result = self.first / self.second
        return result


calculationA = Calculation(1, 2)  # self.first에 1 self.second 에 2를 저장

print(calculationA.add())  # 1 + 2
print(calculationA.mul())  # 1 * 2
print(calculationA.sub())  # 1 - 2
print(calculationA.div())  # 1 / 2

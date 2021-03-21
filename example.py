import random


def lottoo():

    i = 0
    while True:
        i += 1
        if i < 7:
            print(int(random.random() * 36))
        else:
            return


def lotto():
    lottoNum = []
    while True:
        if len(lottoNum) > 6:
            return lottoNum
        randomNum = int(random.random() * 36)
        if randomNum != 0 and randomNum not in lottoNum:
            lottoNum.append(randomNum)


num = lotto()
num.sort()

print(num)

# userArray = []
# passwordArray = []


# def createAccount():
#     username = input("username: ")
#     password = input("password: ")
#     userArray.append(username)
#     passwordArray.append(password)


# def login():
#     username = input("username: ")
#     password = input("password: ")
#     if username in userArray and password in passwordArray:
#         print("success")


# while True:
#     user_input = input("login or createAccount: ")

#     if user_input == "createAccount":
#         createAccount()
#     elif user_input == "login":
#         login()

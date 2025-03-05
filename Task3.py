# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ...

START = 0
END = 1000
USER_FRAZE = ['да', "нет", "угодал"]


def user_input(midl):
    while True:
        answer = input(f"Твое число больше {midl} ? Ты можешь отвечать только так {USER_FRAZE} \n")
        answer = answer.lower()
        if answer in USER_FRAZE:
            return answer
        print("Вы ввели не корректные данные!")


def binary_search():
    start = START
    end = END
    while True:
        midl = (start + end) // 2
        user_answer = user_input(midl)
        if user_answer == "угодал":
            print("Ура, ура ...")
            return
        if user_answer == "да":
            start = midl + 1
        if user_answer == "нет":
            end = midl - 1


binary_search()

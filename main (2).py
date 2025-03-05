def user_input():
    while True:
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        if num1.isdigit():
            num1 = int(num1)
        else:
            print("Первое число не цифры")
            continue

        if num2.isdigit():
            num2 = int(num2)
        else:
            print("Второе число не цифры")
            continue

        if num2 < num1:
            print("Начало диапозона должно быть меньше")
            continue
        return num1, num2


def is_simple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def task1(start, stop):
    result = []

    for num in range(start, stop):
        if is_simple(num):
            result.append(num)

    return result

def main():
    start, end = user_input()
    task1(start, end)
    result = task1(start, end)
    print(result)

    main()
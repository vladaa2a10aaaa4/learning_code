try:
    n = float(input("Сколько лет вашей собаке? "))

    if n < 0:
        print("Возраст не может быть отрицательным.")
    elif n <= 1:
        n = 15
    elif n <= 2:
        n = 24
    else:
        n = 24 + (n - 2) * 4
    
    n = int(n)

    if n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        print(f"Вашей собаке {n} года")
    elif n % 10 == 1:
        print(f"Вашей собаке {n} год")
    else:
        print(f"Вашей собаке {n} лет")
except ValueError:
    print("Пожалуйста, введите корректное число.")

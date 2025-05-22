try:
    n = float(input("Сколько лет вашей кошке? "))

    if n < 0:
        print("Возраст не может быть отрицательным.")
    elif n <= 1:
        n = 15
    elif n <= 2:
        n = 24
    elif n >= 2 and n <= 16:
        n = 24 + (n - 2) * 4
    else:
        n = 80 + (n - 16) * 3
    
    n = int(n)

    if n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        print(f"Вашей кошке {n} года")
    elif n % 10 == 1:
        print(f"Вашей кошке {n} год")
    else:
        print(f"Вашей кошке {n} лет")
except ValueError:
    print("Пожалуйста, введите корректное число.")

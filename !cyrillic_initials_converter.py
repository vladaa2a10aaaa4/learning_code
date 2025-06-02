full_name = input('Ваше ФИО: ').split()
if len(full_name) == 3:
    print(f"{full_name[0]} {full_name[1][0].upper()}.{full_name[2][0].upper()}.")
else:
    print("Ошибка ввода")

# Считываем строку с ввода
string = input()

# Инициализируем счётчик одинаковых соседних символов
count = 0

# Получаем длину строки
length = len(string)

# Инициализируем переменную для хранения последнего символа
last_char = None

# Проходим по всем символам строки от первого до последнего
for i in range(length):
    # Проверяем, не равен ли текущий символ последнему символу
    if string[i] == last_char:
        # Если равны, увеличиваем счётчик на 1
        count += 1
    # Обновляем последний символ
    last_char = string[i]

# Выводим общее количество одинаковых соседних символов
print(count)

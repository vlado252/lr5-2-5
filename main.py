# Запрашиваем у пользователя ввод строки
str = input("Введи строку:")

# Инициализируем счетчик для подсчета букв 'и'
count = 0

# Преобразуем строку в нижний регистр, чтобы учитывать все варианты написания буквы 'и'
str1 = str.lower()

# Проходим по каждому символу в строке
for i in str1:
    # Если символ равен 'и', увеличиваем счетчик на 1
    if i == "и":
        count += 1

# Выводим количество букв 'и' в строке
print("Количество букв и:", count)

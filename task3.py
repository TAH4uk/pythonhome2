# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
str3 = None

list = []
for i in range(len(str1)):
    count = 0
    for z in range(len(str2)):
        if str1[i] == str2[z]:
            count += 1
    str3 = f"{str1[i]} - {count}"
    list.append(str3)

print()
print(list)
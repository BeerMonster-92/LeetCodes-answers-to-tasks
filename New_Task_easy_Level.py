dict = {1:2, 2:4, 3:6, 4:8, 5:10}
# нет чисел 7 и 9
# key = (1, 2, 3, 4, 5)
# value = (2, 4, 6, 8, 10)

if 5 in dict:
    print("yes")
else:
    print("no")
# выведет "yes" так как in проверяет ключи


if 10 in dict:
    print("yes")
else:
    print("no")

# выведет "no" так как in не проверяет значения
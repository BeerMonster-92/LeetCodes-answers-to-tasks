# Ожидаемый результат: {85: ['Alice', 'Charlie'], 92: ['Bob', 'Diana']}

grades = {'Alice': 85, 'Bob': 92, 'Charlie': 85, 'Diana': 92}

inv_grades = {}
for key, value in grades.items():
    if value not in inv_grades:
        inv_grades[value] = []   # создаём новый список
    inv_grades[value].append(key)
print(inv_grades)
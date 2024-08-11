num = int(input('Введите число от 3 до 20: '))
result = ''

for i in range(1, num):
    for j in range(i + 1, num):
        if num % (i + j) == 0:
            result += str(i)
            result += str(j)
print('Пароль:', result)

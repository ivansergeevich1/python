number = int(input('Введите целое положительное число: '))
a = number % 10
b = number // 10
while a < b:
    print(f'Самая большая цифра в вашем числе: {a}')
    break

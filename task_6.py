a = int(input('Ваш результат в первый день: '))
b = int(input('Ваш желаемый результат : '))
day = 1
print(f'{day}-й день результат:{a}')
while a < b:
    a *= 1.1
    day += 1
    print(f'{day}-й день результат: {a:.2f}')

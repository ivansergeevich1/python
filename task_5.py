plus = int(input('Ваша выручка: '))
minus = int(input('Ваши издержки: '))
total = plus - minus
percent = int((total / plus) * 100)

if total > 0:
    print(f'Вы работаете в плюс, Ваша рентабельность {percent}%')
    how_much = int(input('Численность Вашего штата сотрудников: '))
    plus_2 = int(plus / how_much)
    print(f'Прибыль фирмы в расчете на одного сотрудника = {plus_2}')
else:
    print('Вы работаете в убыток')

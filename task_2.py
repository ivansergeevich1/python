# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
your_time_seconds = int(input('Введите время в секундах: '))
a = your_time_seconds % 3600
hours = your_time_seconds // 3600
minutes = a // 60
seconds = a % 60
print(f'Ваше время {hours}:{minutes}:{seconds}')

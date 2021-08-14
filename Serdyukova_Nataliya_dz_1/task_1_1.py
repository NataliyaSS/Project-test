duration = int(input('Введите промежуток времени в секундах: '))
second = duration % 60
minute = duration // 60 % 60
hour = duration % 86400 // 3600
day = duration // 86400

if duration < 60:
    print(second, 'сек')
elif duration > 60 and duration < 3600:
    print(minute, 'мин', second, 'сек')
elif duration > 3600 and duration < 86400:
    print(hour, 'час', minute, 'мин', second, 'сек')
else:
    print(day, 'дн', hour, 'час', minute, 'мин', second, 'сек')

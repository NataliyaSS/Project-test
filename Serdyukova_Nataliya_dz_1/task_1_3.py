i = 0
for i in range(1, 101):
    if i % 10 ==1 and i % 100 != 11:
        print(i, 'процент')
    elif i % 10 >= 2 and i % 10 <= 4 and (i % 100 < 10 or i % 100 > 20):
        print(i, 'процента')
    else:
        print(i, 'процентов')


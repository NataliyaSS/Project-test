list_cube = []
for i in range(100):
    if i % 2 != 0:
        list_cube.append(i**3)
print(list_cube)


list_2 = []
for number in list_cube:
    num_1 = number
    amount = 0
    while number != 0:
        amount = amount + number % 10
        number = number // 10
    if amount % 7 == 0:
        list_2.append(num_1)
amount_2 = 0
for el in list_2:
    amount_2 += el
print(amount_2)


for ind in range(len(list_cube)):
    list_cube[ind] += 17
print(list_cube)

list_2 = []
for number in list_cube:
    num_1 = number
    amount = 0
    while number != 0:
        amount = amount + number % 10
        number = number // 10
    if amount % 7 == 0:
        list_2.append(num_1)
amount_2 = 0
for el in list_2:
    amount_2 += el
print(amount_2)



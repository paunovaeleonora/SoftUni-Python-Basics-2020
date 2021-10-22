projection = input()
rows = int(input())
colons = int(input())

capacity = rows * colons
price = 0

if projection == 'Premiere':
    price = capacity * 12
elif projection == 'Normal':
    price = capacity * 7.50
elif projection == 'Discount':
    price = capacity * 5
print(f'{price:.2f} leva')
count_drives = int(input())
sum_tons = 0
average_price = 0
bus_price = 0
truck_price = 0
train_price = 0
bus_percent = 0
truck_percent = 0
train_percent = 0
total = 0
for times in range(1, count_drives + 1):
    tons = int(input())
    sum_tons += tons

    if tons <= 3:
        bus_price = 200
        total += tons * bus_price
        bus_percent += tons / sum_tons * 100
    if 4<= tons <= 11:
        truck_price = 175
        total += tons * train_price
        train_percent += tons / sum_tons * 100
    if tons >= 12:
        train_price = 120
        total += train_price * tons
        train_percent += tons / sum_tons * 100
average_price = total / sum_tons
print(f'{average_price:.2f}')
print(f'{bus_percent:.2f}%')
print(f'{truck_percent:.2f}%')
print(f'{train_percent:.2f}%')

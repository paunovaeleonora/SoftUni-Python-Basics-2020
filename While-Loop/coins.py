total = float(input())

counter = 0

total_change = total * 100
while total_change > 0:
    if total_change >= 200:
        counter += total_change // 200
        total_change %= 200
    elif 100 <= total_change < 200:
        counter += total_change // 100
        total_change %= 100
    elif 50 <= total_change < 100:
        counter += total_change // 50
        total_change %= 50
    elif 20 <= total_change < 50:
        counter += total_change // 20
        total_change %= 20
    elif 10 <= total_change < 20:
        counter += total_change // 10
        total_change %= 10
    elif 5 <= total_change < 10:
        counter += total_change // 5
        total_change %= 5
    elif 2 <= total_change < 5:
        counter += total_change // 2
        total_change %= 2
    elif total_change < 2:
        counter += total_change // 1
        break

print(f'{counter:.0f}')

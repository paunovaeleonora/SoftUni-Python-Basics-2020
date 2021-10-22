age = int(input())
washing_machine = float(input())
toy_price = int(input())
count_toys = 0
amount = 10
money = 0
for year in range(1, age + 1):

    if not year % 2 == 0:
        count_toys += 1
    else:
        money += amount - 1
        amount += 10

money += toy_price * count_toys    # money = money + toy_price * count_toys
diff = abs(money - washing_machine)
if money >= washing_machine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')






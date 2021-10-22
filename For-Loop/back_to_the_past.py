money = float(input())
year_past = int(input())
age = 17

spent_money = 0

for year in range(1800, year_past + 1):
    age += 1
    if year % 2 == 1:
        spent_money = 12000 + age * 50
        money -= spent_money
    elif year % 2 == 0:
        spent_money = 12000
        money -= spent_money

if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    print(f'He will need {(abs(money)):.2f} dollars to survive.')

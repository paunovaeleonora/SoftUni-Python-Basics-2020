needed_money = float(input())
money = float(input())
amount = 0
spending_counter = 0
days_counter = 0

while needed_money > money and spending_counter < 5:
    command = input()
    amount = float(input())
    days_counter += 1
    if command == 'save':
        money += amount
        spending_counter = 0
    elif command == 'spend':
        money -= amount
        spending_counter += 1
    if amount > money:
        money = 0
if spending_counter == 5:
    print(f"You can't save the money.")
    print(f'{days_counter}')
if needed_money <= money:
    print(f'You saved the money for {days_counter} days.')

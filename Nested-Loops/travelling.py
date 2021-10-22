while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    money = 0
    while money < budget:
        saved_money = float(input())
        money += saved_money
    else:
        print(f'Going to {destination}!')

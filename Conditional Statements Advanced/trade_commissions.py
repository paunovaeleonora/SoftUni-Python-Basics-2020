city = input()
sales = float(input())
commission = 0

name = city == 'Sofia' or city == 'Varna' or city == 'Plovdiv'

if 0 <= sales <= 500 and name:
    if city == 'Sofia':
        commission = 0.05 * sales
    elif city == 'Varna':
        commission = 0.045 * sales
    elif city == 'Plovdiv':
        commission = 0.055 * sales
    print(f'{commission:.2f}')

elif 500 < sales <= 1000 and name:
    if city == 'Sofia':
        commission = 0.07 * sales
    elif city == 'Varna':
        commission = 0.075 * sales
    elif city == 'Plovdiv':
        commission = 0.08 * sales
    print(f'{commission:.2f}')
elif 1000< sales <= 10000 and name:
    if city == 'Sofia':
        commission = 0.08 * sales
    elif city == 'Varna':
        commission = 0.1 * sales
    elif city == 'Plovdiv':
        commission = 0.12 * sales
    print(f'{commission:.2f}')
elif sales > 10000 and name:
    if city == 'Sofia':
        commission = 0.12 * sales
    elif city == 'Varna':
        commission = 0.13 * sales
    elif city == 'Plovdiv':
        commission = 0.145 * sales
    print(f'{commission:.2f}')
else:

        print('error')

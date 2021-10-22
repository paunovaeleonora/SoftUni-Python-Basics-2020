open_tabs = int(input())
wages = int(input())

for page in range(1, open_tabs + 1):
    page = input()

    if page == 'Facebook':
        wages -= 150
    elif page == 'Instagram':
        wages -= 100
    elif page == 'Reddit':
        wages -= 50
    if wages <= 0:
        print('You have lost your salary.')
        break
if wages > 0:
    print(wages)

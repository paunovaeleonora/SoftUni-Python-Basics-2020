day = input()
work = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday'
rest = day == 'Saturday' or day == 'Sunday'

if work:
    print(f'Working day')
elif rest:
    print(f'Weekend')
else:
    print(f'Error')
hour = int(input())
day = input()

open_hours = 10 <= hour <= 18
open_days = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday'

if open_hours and open_days:
    print('open')
else:
    print('closed')
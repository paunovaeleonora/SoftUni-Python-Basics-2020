days = {
    'Monday': 'Working day',
    'Tuesday': 'Working day',
    'Wednesday': 'Working day',
    'Thursday': 'Working day',
    'Friday': 'Working day',
    'Saturday': 'Weekend',
    'Sunday': 'Weekend'
}
day = input()
try:
    print(days[day])
except KeyError:
    print('Error')
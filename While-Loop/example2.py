plates = 3

while plates > 0:
    doorbell = bool(input())
    # if there is sth in input() is taken as True
    # to be taken as False leave it empty
    if doorbell: # if doorbell == True
        break
    print('washing the dishes')
    plates -= 1

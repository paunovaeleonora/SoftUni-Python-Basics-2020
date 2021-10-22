total_tickets = 0
total_kid = 0
total_standard = 0
total_student = 0
count_standard = 0
count_kid = 0
count_student = 0

while True:
    movie = input()

    if movie == 'Finish':
        break

    seats = int(input())
    count_ticket = 0

    for type_tickets in range(1, seats + 1):
        type_ticket = input()

        if type_ticket == 'standard':
            count_standard += 1
        elif type_ticket == "kid":
            count_kid += 1
        elif type_ticket == 'student':
            count_student += 1
        elif type_ticket == 'End' or count_ticket == seats:
            break
        count_ticket += 1
    print(f'{movie} - {(count_ticket / seats * 100):.2f}% full.')

    total_tickets += count_ticket
    total_kid += count_kid
    total_standard += count_standard
    total_student += count_student
standard_p = count_standard / total_tickets * 100
kid_p = count_kid / total_tickets* 100
student_p = count_student / total_tickets * 100


print(f'Total tickets: {total_tickets}')
print(f'{student_p:.2f}% student tickets.')
print(f'{standard_p:.2f}% standard tickets.')
print(f'{kid_p:.2f}% kids tickets.')
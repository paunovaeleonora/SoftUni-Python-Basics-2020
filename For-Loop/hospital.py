period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
sum_untreated = 0
sum_treated = 0
for day in range(1, period + 1):
    patients = int(input())
    sum_untreated += untreated_patients
    sum_treated += treated_patients
    if day != 3:
        treated_patients = doctors
        untreated_patients = patients - treated_patients
    elif day == 3:
        if sum_treated < sum_untreated:
            doctors += 1
            treated_patients = doctors
            untreated_patients = patients - treated_patients


print(f'Treated patients: {sum_treated}.')
print(f'Untreated patients: {sum_untreated}.')




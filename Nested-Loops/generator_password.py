a = int(input())
b = int(input())
max_count_passwords = int(input())
comb = 0
secret_password = ''
all_possible_combinations = a * b
is_reached = False
for upper_a in range(35, 56):
    for upper_b in range(64, 97):
        for x in range(1, a + 1):
            for y in range(1, b + 1 ):
                secret_password = chr(upper_a) + chr(upper_b) + str(x) + str(y) + chr(upper_b) + chr(upper_a)
                print(f'{secret_password}|', end='')
                upper_a += 1
                if upper_a > 55:
                    upper_a = 35
                upper_b += 1
                if upper_b > 96:
                    upper_b = 64
                comb += 1
                if max_count_passwords > all_possible_combinations == comb:
                    is_reached = True
                    break
                if all_possible_combinations > max_count_passwords and comb == max_count_passwords:
                    is_reached = True
                    break
            if is_reached:
                break
        if is_reached:
            break
    if is_reached:
        break


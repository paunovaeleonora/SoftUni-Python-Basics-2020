letter = input()
count_c = 0
count_n = 0
count_o = 0

while letter != 'End':
    letter = ord(letter)
    word = str()
    while count_c < 3 and count_n < 3 and count_o < 3:
        if 64 < letter < 91 or 96 < letter < 123:
            if letter == 99:
                count_c += 1
                if count_c > 1:
                    letter = chr(letter)
                    word += letter
            if letter == 110:
                count_n += 1
                if count_n > 1:
                    letter = chr(letter)
                    word += letter
            if letter == 111:
                count_o += 1
                if count_o > 1:
                    letter = chr(letter)
                    word += letter
            letter = chr(letter)
            word += letter

    print(f'{word} ', end='')
    letter = input()

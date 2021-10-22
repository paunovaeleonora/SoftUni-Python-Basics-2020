wanted_book = input()
book = input()
book_counter = 0
while book != wanted_book:
    book = input()
    book_counter += 1
    if book == 'No More Books':
        print(f'The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break
else:
    print(f'You checked {book_counter} books and found it.')



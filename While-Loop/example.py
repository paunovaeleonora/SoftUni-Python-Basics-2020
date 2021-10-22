command = input()
cFound = False
oFound = False
nFound = False
word = ""
while command != "End":
    mustBeAdded = False
    if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
        if command == "c":
            if cFound:
                word += command
            else:
                cFound = True
        elif command == "o":
            if oFound:
                word += command
            else:
                oFound = True
        elif command == "n":
            if nFound:
                word += command
            else:
                nFound = True
        else:
            word += command
        if cFound and oFound and nFound:
            print(f"{word}", end=" ")
            word = ""
            cFound = False
            oFound = False
            nFound = False
    command = input()
print('character checker')
num = int(input('enter count: '))

for i in range(1, num + 1):
    character = input('enter character: ')
    if character.isupper():
        print("All Capital Letter")
    elif character.islower():
        print("All Small Letter")
    else:
        print("MIX")
def print_menu():
    c = 0
    print('Menu')
    for i in range (0,12):
        print('-',end='')
    print('\n1. Encode')
    print('2. Decode')
    print('3. Quit')
    c = int(input('\nPlease enter an option: '))
    if c == 1:
        number = input("Please enter the number to encode: ")
        print(f"Your encoded number is {encode(number)}")
    elif c == 2:
        number = input("Please enter the number to decode: ")
        print(f"Your decoded number is {decode(number)}")
    elif c == 3:
        print('Goodbye!')
    else:
        print("Please enter a valid option.")

def encode(string):
    encoded_string = ''
    lis = list(string)
    for i in range (len(lis)):
        lis[i] = int(lis[i])
        lis[i] = (lis[i] + 3) % 10
    for i in range (len(lis)):
        lis[i] = str(lis[i])
        encoded_string += ''.join(lis[i])
    return encoded_string

def decode(user):
    user = str(user)
    decoding_list = [7,8,9,0,1,2,3,4,5,6]
    decoded_user = ""

    for i in user:
        decoded_user = decoded_user + str(decoding_list[int(i)])

    print(decoded_user)

print_menu()

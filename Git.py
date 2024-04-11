def print_menu():
    c = 0
    print('Menu')
    for i in range (0,12):
        print('-',end='')
    print('\n1. Encode')
    print('2. Decode')
    print('3. Quit')
    c = int(input('\nPlease enter an option: '))


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



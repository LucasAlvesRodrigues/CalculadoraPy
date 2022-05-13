#LUCAS ALVES RODRIGUES - RGM: 29714893



from math import *

while True:
    print('Menu')
    print('[1] Decimal para outras bases\n[2] Outras bases para Decimal\n[0] Sair')
    op = int(input('Digite uma opção: '))
    if op == 0:
        break
    elif op == 1:

        while True:
            print('Decimal para outras bases')
            print('[1] Decimal para Binário\n[2] Decimal para Octal\n[3] Decimal para Hexadecimal\n[0] Sair')
            op = int(input('Digite uma opção: '))
            if op == 0:
                break
            elif op == 1:
                num = int(input('Digite um número: '))
                print('O número {} em binário é {}'.format(num, bin(num)[2:]))
                break
            elif op == 2:
                num = int(input('Digite um número: '))
                print('O número {} em octal é {}'.format(num, oct(num)[2:]))
                break
            elif op == 3:
                num = int(input('Digite um número: '))
                print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:]))
                break
            else:
                print('Opção inválida')

    elif op == 2:
        while True:
            print('Outras bases para Decimal')
            print('[1] Binário para Decimal\n[2] Octal para Decimal\n[3] Hexadecimal para Decimal\n[0] Sair')
            op = int(input('Digite uma opção: '))
            if op == 0:
                break
            elif op == 1:
                num = input('Digite um número: ')
                print('O número {} em decimal é {}'.format(num, int(num, 2)))
                break
            elif op == 2:
                num = input('Digite um número: ')
                print('O número {} em decimal é {}'.format(num, int(num, 8)))
                break
            elif op == 3:
                num = input('Digite um número: ')
                print('O número {} em decimal é {}'.format(num, int(num, 16)))
                break
            
            else:
                print('Opção inválida')
    break                   
          
            
                






    


          



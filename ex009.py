import converter as converter

n1 = int(input('Digite um numero '))
print('''Escolhe uma das bases para conversão: 
[ 1 ] converter para Binario
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para Binario é igual a {}'.format(n1, bin(n1)))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(n1, oct(n1)))
elif opção == 3:
    print('{} convertido para Octal é igual a {}'.format(n1, hex(n1)))
else:
    print('Opção invalida')
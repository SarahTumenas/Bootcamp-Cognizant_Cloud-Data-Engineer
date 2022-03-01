#Operadores Aritméticos
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
#print(type(soma))
#soma = str(soma)
#print(type(soma))

# print('soma: ' + str(soma))
# print('subtração: {}'.format(subtracao))
# print('Soma: {}, Subtração: {}'.format(soma, subtracao))
#
# print(multiplicacao)
# print(type(divisao))
# print(int(divisao))
# print(divisao)
# print(resto)
# print('Divisão: {div} \nResto: {resto}'.format(div=divisao, resto=resto))
#
#
# x = '1'
# soma2 = int(x) + 1
# print('Soma2: {}'.format(soma2))

# print('Soma: {soma} \nSubtração: {sub} \nMultiplicação: {multi} '
#       '\nDivisão: {div} \nResto: {resto}'.format(div=divisao,
#                                                  resto=resto,
#                                                  soma=soma,
#                                                  sub=subtracao,
#                                                  multi=multiplicacao))

resultado = 'Soma: {soma} \nSubtração: {sub}' \
            ' \nMultiplicação: {multi} ' \
            '\nDivisão: {div} ' \
            '\nResto: {resto}'.format(div=divisao,
                                                 resto=resto,
                                                 soma=soma,
                                                 sub=subtracao,
                                                 multi=multiplicacao)
print(resultado)

#Sintaxes Básicas,Condicionais e Operadores Lógicos
 a = int(input('Primeiro valor: '))
 b = int(input('Segundo valor: '))
 c = int(input('Terceiro valor: '))

 if a > b and a > c:
     print('O maior número é: {}'.format(a))
 elif b > a and b > c:
     print('O maior número é: {}'.format(b))
 else:
     print('o maior número é: {}'.format(c))
 print('final do programa')

 x = int(input('Entre com o primeiro valor: '))
 y = int(input('Entre com o segundo valor: '))
 resto_x = x % 2
 resto_y = y % 2
 if resto_x == 0 or resto_y == 0:
     print('foi digitado número par')
 else:
     print('nenhum número par foi digitado')

# Solicitar as notas bimestrais de um aluno, validando se notas são <= 10  e calcular a média
bim_1 = float(input(('Digite a nota do 1º Bimestre: ')))
if bim_1 > 10:
    bim_1 = float(input(('Nota inválida. Digite novamente a nota do 1º Bimestre: ')))
bim_2 = float(input(('Digite a nota do 2º Bimestre: ')))
if bim_2 > 10:
    bim_2 = float(input(('Nota inválida. Digite novamente a nota do 1º Bimestre: ')))
bim_3 = float(input(('Digite a nota do 3º Bimestre: ')))
if bim_3 > 10:
    bim_3 = float(input(('Nota inválida. Digite novamente a nota do 1º Bimestre: ')))
bim_4 = float(input(('Digite a nota do 4º Bimestre: ')))
if bim_4 > 10:
    bim_4 = float(input(('Nota inválida. Digite novamente a nota do 1º Bimestre: ')))

media = (bim_1 + bim_2 + bim_3 + bim_4) / 4

if media >= 6.5:
    print('Aluno aprovado. Média: {}'.format(media))
elif 3.0 < media <= 6.49:
    print('Aluno em recuperação. Média {}'.format(media))
else:
    print('Aluno reprovado. Média: {}'.format(media))



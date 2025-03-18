nome = input('Qual o seu nome? ')
sobrenome = input('Qual o seu sobrenome? ')
idade = input('Qual é a sua idade? ')
int_idade = int(idade)
ano_de_nascimento = input('Em que ano você nasceu? ')
int_ano_de_nascimento = int(ano_de_nascimento)
altura_em_metros = input('Qual é sua altura? ')
float_altura_em_metros = float(altura_em_metros)
peso = input('Quanto você pesa? ')
float_peso = float(peso)
print( )
maior_de_idade = int_idade >= 18
imc = float_peso / float_altura_em_metros ** 2
imc_baixo = imc <= 18.6
imc_alto = imc >= 24.9
imc_regular = imc >= 18.6, imc <= 24.9

print(f'O seu nome é {nome}')
print(f'O seu sobrenome é {sobrenome}')
print(f'O seu nome completo é {nome + str(" ") + sobrenome}')
print( )
print(f'Você tem {idade} anos')
print(f'Você nasceu no ano de {ano_de_nascimento}')
print(f'É maior de idade? {maior_de_idade}')
print( )
print(f'A sua altura é {float_altura_em_metros:.2f} m')
print(f'O seu peso é {float_peso:.2f} quilos')
print(f'O seu imc é {imc}')
print( )
print(f'Você está abaixo do peso? {imc_baixo}')
print(f'Você está acima do peso? {imc_alto}')
print(f'O seu imc está ideal? {imc_regular}')

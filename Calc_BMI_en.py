nome = input("What's your name? ")
sobrenome = input("What's your last name? ")
idade = input("How old are you? ")
int_idade = int(idade)
ano_de_nascimento = input("What year were you born? ")
int_ano_de_nascimento = int(ano_de_nascimento)
altura_em_metros = input("How tall are you? ")
float_altura_em_metros = float(altura_em_metros)
peso = input("How much do you weigh? ")
float_peso = float(peso)
print( )
maior_de_idade = int_idade >= 18
imc = float_peso / float_altura_em_metros ** 2
imc_baixo = imc <= 18.6
imc_alto = imc >= 24.9
imc_regular = imc >= 18.6, imc <= 24.9

print(f'Your name is {nome}')
print(f'Your last name is {sobrenome}')
print(f'Your full name is {nome + str(" ") + sobrenome}')
print( )
print(f'You are {idade} years old')
print(f'You were born in the year of {ano_de_nascimento}')
print(f'Are you of legal age? {maior_de_idade}')
print( )
print(f'Your height in meters is {float_altura_em_metros:.2f}m')
print(f'Your weight in kilograms is {float_peso:.2f} kg')
print(f'Your bmi is {imc}')
print( )
print(f'Are you underweight? {imc_baixo}')
print(f'Are you overweight? {imc_alto}')
print(f'Is your BMI ideal? {imc_regular}')
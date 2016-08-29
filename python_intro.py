print('Hello, Django girls!')

numero = 6
n2 = 2

if numero > n2:
	print('O primeiro número')
	print (numero)
	print ('é maior que o segundo')
else:
	print('O primeiro número não é maior que o segundo')


def hi(name):
	print('Hi ' + name + '!')

girls = ['Veronica','Isadora','Joana','Fernanda']

for name in girls:
	hi(name)
	print('Next girl')


hi(name)

def ola(nome):
	print('Oi '+ nome + '!')

ola("Isadora")

for i in range(1,99):
	print(i)
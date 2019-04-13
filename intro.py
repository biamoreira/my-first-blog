print('Hello, Django girls!')
5+2
5>2
participante={'name':'beatriz', 'idade': '25', 'cidade': 'Fortaleza'}
print(participante)
if 3>2:
	print('Funciona')


#CRIANDO FUNÇÃO
def oi():
	print('ola')
	print('tudo bem')


oi()

def oi(nome):
	if nome == 'ola':
		print('ola ola!')
	elif nome == 'bia':
		print('ola bia')
	else:
		print('ola estranho')

oi('bia')
oi('sis')

def oi(name):
	print('ola' + name + '!')

oi('Sis')

def oi(nome):
	print('oi'+nome+'!')

girl=['rachel', 'monica', 'phoebe', 'ola', 'voce']
for name in girl:
	oi(name)
	print('proxima')




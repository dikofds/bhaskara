import math

print('-------------------------------------------------------------------')
print('RESOLUÇÃO BÁSKHARA by dikofds :)')
print('-------------------------------------------------------------------')

print('INSIRA OS VALORES:')
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

delta = b **2-4*a*c
print ('-O VALOR DE DELTA É: ', delta, '-')

doisA = 2*a

if delta == 0:
    x = -b / 2*a
    print('-O VALOR DE "X" É', x, '-')
    
elif delta > 0:
    raiz = math.sqrt(delta)
    x1 = -b + raiz 
    x2 =  -b - raiz
    print('-"X1" É IGUAL A: ', x1 / doisA, '-\n-X2 É IGUAL A: ', x2 / doisA, '-')

else:
    print('-DELTA É NEGATIVO, SEM SOLUÇÃO.')
    

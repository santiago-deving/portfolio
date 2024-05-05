print('\nBem-vindo à calculadora de médias amortizadas!')
X = int(input('qual é o fator de amortização?\n'))
N = []
Decis = False
N.append(float(input('insira o primeiro número: ')))

while Decis == False:
    novoval = input('\nDigite o próximo número (ou "n" caso não precise): ')
    if  str(novoval) == "n":
        Decis = True
        num = len(N)
        print('\nCalculando para',N, '...\n')

    else:
        Decis = False
        N.append(float(novoval))

som = 0
for v in N:
    som = float(som) + 1/(float(v) + int(X))
    res = int(num)/float(som) - int(X)

print('O resultado é: ', res)
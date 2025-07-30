from datetime import datetime

decis = 0
total_pontos = ['horarios']
cadastro_func = [{'nome' : 'f1', 'id' : 'm1'}]

decis = int(input ('Escolha uma opção:\n\n1. Novo Funcionário\n2. Mostrar meus dados\n3. Registrar ponto na hora atual\n'))

if decis == int(1):
    nome = input('Seu nome: ')
    id = input('Sua matrícula: ')
    novo_func = {'nome' : nome, 'id' : id}
    cadastro_func.append(novo_func)
    print(cadastro_func)

if decis == (2):
    print(cadastro_func)
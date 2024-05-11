import telebot
from datetime import datetime
# import json

CHAVE_API = '6874492595:AAEELvm4sTYLMjv2OvIUena8warMR6NJASI'
bot = telebot.TeleBot(CHAVE_API)

decis = 0
total_pontos = {'func_id1': ['horarios'] , 'func_id2': ['horarios']}
cadastro_func = [{'nome' : 'f1', 'id' : 'chat id', 'num func' : 'num empresa'},{'nome' : 'f2', 'id' : 'chat id', 'num func' : 'num empresa'}]

@bot.message_handler(commands=["reg"])
def reg(mensagem):
    bot.send_message(mensagem.chat.id, "O que deseja fazer?\n/cad - cadastrar dados funcionario\n/mha - marcar ponto no horário atual\n/mhp - marcar horário personalizado\n/edit - Editar uma marcação de ponto\n/exc - Excluir uma marcação\n/ver - ver dias marcados")
#/mha - marca ponto agora
#/mhp - marca horário personaizado
#[ainda não ativo!!!!!] /edit - edita uma marcação
#[ainda não ativo!!!!!] /ver - vê pontos marcados

@bot.message_handler(commands=["cad"])
# Função Cadastrar Funcionário
def cad(mensagem):
    #Busca o id na lista de cadastros, se não encontrar, vai p/ o register_next_step_handler
    for i in cadastro_func:
        if i['id'] == mensagem.chat.id:
            bot.send_message(mensagem.chat.id, "Usuário já Cadastrado!")
            return
    resposta = bot.send_message(mensagem.chat.id, "Digite o seu nome:")
    bot.register_next_step_handler(resposta, cad_nome)

# Chamado em @bot.message_handler(commands=["cad"])
def cad_nome(mensagem):
    novo_func = {'nome' : mensagem.text, 'id' : mensagem.chat.id}
        #Adiciona o número empresarial ao cadastro
    resposta = bot.send_message(mensagem.chat.id, "Digite o seu número: ")  
    bot.register_next_step_handler(resposta, cad_num, novo_func)
        #Direciona a resposta para cad_num

def cad_num(mensagem, novo_func):
    novo_func['num func'] = mensagem.text
    cadastro_func.append(novo_func)
    bot.send_message(mensagem.chat.id, "Usuário cadastrado com sucesso!")
    print(cadastro_func)


@bot.message_handler(commands=["mha"])
# Função Marcar Hora Atual

def reg_mha(mensagem):
    func_id = mensagem.chat.id
    hora_ponto = datetime.now()

    for i in total_pontos:
        if i == func_id:
            total_pontos[func_id].append(hora_ponto)
            bot.send_message(func_id, "O seu ponto foi marcado!")
            # print(total_pontos)
            # print(mensagem)
            return #caso o funcionario seja encontrado
    
    total_pontos[func_id] = [hora_ponto] #caso não seja encontrado, é criada uma lista no dicionario para o funcionário
    bot.send_message(mensagem.chat.id, "O seu ponto foi marcado!")

@bot.message_handler(commands=["mhp"])
# Função Marcar Hora Personalizada

def reg_mhp(mensagem):
    resposta = bot.send_message(mensagem.chat.id, "Digite o dia e a hora que deseja marcar:\n(formato: DD/MM/AAAA - hh:mm)")
    bot.register_next_step_handler(resposta, mhp_reg)
    
def mhp_reg(mensagem):
    data_mhp = mensagem.text
    func_id = mensagem.chat.id
    
    for i in total_pontos:
        if i == func_id:
            total_pontos[func_id].append(data_mhp)
            bot.send_message(func_id, "O seu ponto foi marcado!")
            #print(total_pontos)
            #print(mensagem)
            return
    
    total_pontos[func_id] = [data_mhp]
    bot.send_message(func_id, "O seu ponto foi marcado!")
    #print(total_pontos)
    #print(mensagem)

#Busca nova mensagem
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem,'Bem-vindo ao point EC HMC!\nPara registrar digite /reg')

bot.polling()
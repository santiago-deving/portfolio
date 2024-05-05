import telebot
import datetime
import json

CHAVE_API = '6874492595:AAEELvm4sTYLMjv2OvIUena8warMR6NJASI'
bot = telebot.TeleBot(CHAVE_API)

decis = 0
total_pontos = {'func_id1': ['horarios'] , 'func_id2': ['horarios']}
cadastro_func = [{'nome' : 'f1', 'id' : 'chat id', 'num func' : 'num empresa'},{'nome' : 'f2', 'id' : 'chat id', 'num func' : 'num empresa'}]

@bot.message_handler(commands=["reg"])
def reg(mensagem):
    bot.send_message(mensagem.chat.id, "O que deseja fazer?\n/cad - cadastrar dados funcionario\n/mha - marcar ponto no horário atual\n/mhp - marcar horário personalizado\n/edit - Editar uma marcação de ponto\n/exc - Excluir uma marcação\n/ver - ver dias marcados")
#mha - marca ponto agora
#mhp - marca horário personaizado
#[ainda não ativo!!!!!] edit - edita uma marcação
#[ainda não ativo!!!!!] ver - vê pontos marcados

@bot.message_handler(commands=["cad"])
def reg(mensagem):
    #Busca o id na lista de cadastros, se não encontrar, vai p/ o register_next_step_handler
    for i in cadastro_func:
        if i['id'] == mensagem.chat.id:
            bot.send_message(mensagem.chat.id, "Usuário já Cadastrado!")
            break
    resposta = bot.send_message(mensagem.chat.id, "Digite o seu nome:")
    bot.register_next_step_handler(resposta, cad_nome)

@bot.message_handler(commands=["mha"])
# Função Marcar Hora Atual

def reg(mensagem):
    func_id = mensagem.chat.id
    hora_ponto = mensagem.date
    func_encontrado = False

    for i in total_pontos:
        if i == func_id:
            func_encontrado = True
            total_pontos[func_id].append(hora_ponto)
            bot.send_message(func_id, "O seu ponto foi marcado!")
            break
    
    if func_encontrado == False:
        total_pontos[func_id] = [hora_ponto]
        bot.send_message(mensagem.chat.id, "O seu ponto foi marcado!")
    ## print(total_pontos)
    func_encontrado = False
    ## print(mensagem)

@bot.message_handler(commands=["mhp"])
def reg(mensagem):
    bot.send_message(mensagem.chat.id, "digite o dia e o horário que deseja marcar")

#Busca nova mensagem
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem,'Bem-vindo ao point EC HMC!\nPara registrar digite /reg')

def cad_nome(mensagem):
    novo_func = {'nome' : mensagem.text, 'id' : mensagem.chat.id}
    #Adiciona o número empresarial ao cadastro
    resposta = bot.send_message(mensagem.chat.id, "Digite o seu número: ")  
    bot.register_next_step_handler(resposta, cad_num, novo_func)    #Direciona a resposta para cad_num

def cad_num(mensagem, novo_func):
    novo_func['num func'] = mensagem.text
    cadastro_func.append(novo_func)
    bot.send_message(mensagem.chat.id, "Usuário cadastrado com sucesso!")
    print(cadastro_func)

bot.polling()
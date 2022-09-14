#Instituto Federal de Rondônia
#Projeto Integrador
#GRUPO: Geovanna Batista dos Santos, Thalita Golçalves da Costa, Ítalo Eduardo Maciel, Renato Ferreira Martins

#Biblioteca usada para "limpar"
import os
#Criando a classe usuário, do ator do diagrama
class Usuario:
  #Construtor
  def __init__(self, nome, data_nascimento, telefone, email, senha):
    #Atributos da nossa classe
    self.__nome=nome
    self.__data_nascimento=data_nascimento
    self.__telefone=telefone
    self.__email=email
    self.__senha=senha

  #Métodos acessores (get)
  def getNome(self):
    return self.__nome

  def getData_nascimento(self):
    return self.__data_nascimento

  def getTelefone(self):
    return self.__telefone

  def getEmail(self):
    return self.__email

  def getSenha(self):
    return self.__senha

  #Métodos modificadores (set)
  def setNome(self, nome):
    self.__nome=nome

  def setData_nascimento(self, data_nascimento):
    self.__data_nascimento=data_nascimento

  def setTelefone(self, telefone):
    self.__telefone=telefone

  def setEmail(self, email):
    self.__email=email

  def setSenha(self, senha):
    self.__senha=senha

#Classe adicional, específica para o sistema poder gerenciar os eventos
class eventos():
  def __init__(self, indice, evento, data):
   self.__indice = indice
   self.__evento = evento
   self.__data = data
  def getIndice(self):
    return self.__indice
  def getEvento(self):
    return self.__evento
  def getData(self):
    return self.__data

#Listas para armazenar as informações dos usuários
lista_usuarios = []
Eventos = []

j = 0

#Função menu(), tela principal, onde o usuário deseja ir
def menu():
  print('\n\033[1;49;34m --- Planner TIGR --- \033[m')
  print('\n\033[1;49;92m 1° --> CADASTRO \033[m')
  print('\n\033[1;49;92m 2° --> LOGIN \033[m')
  print('\n\033[1;49;92m 3° --> PERFIL \033[m')
  print('\n\033[1;49;92m 4° --> ENCERRAR \033[m')
  r=input('\n\033[1;49;34m Você deseja ir para onde? Digite: \n(1) para fazer CADASTRO. \n(2) para fazer LOGIN. \n(3) para ver seu PERFIL. \n(4) para ENCERRAR. \n\n\033[m')
  return r

#Função início(), específica somente para o CADASTRO
def inicio():
  global j
  print('\033[1;49;34m --- Planner TIGR --- \033[m')
  print('\n\033[1;49;92m CADASTRO \033[m')
  print('\033[0;92m Faça seu cadastro: ')
  nome = input('\n\033[0;92m Nome: ')
  data_nascimento = input('\033[0;92m Idade: ')
  telefone = input('\033[0;92m Telefone: ')
  email = input('\033[0;92m E-mail: ')
  senha = input('\033[0;92m Senha: ')
  lista_usuarios.append(Usuario(nome, data_nascimento, telefone, email, senha))
  exibirinfo(len(lista_usuarios)-1)
  login()

#Função login(), específica somente para o LOGIN
def login():
  import time
  global j
  os.system('clear')
  print('\033[1;49;34m --- Planner TIGR --- \033[m')
  print('\n\033[1;49;92m LOGIN \033[m')
  print("\033[0;92m Efetue o login ")
  login_email=input('\n\033[0;92m Digite seu E-mail: ')
  loginsenha=input('\033[0;92m Digite sua Senha: ')

  if (len(lista_usuarios) == 0):
    print('\n\033[1;31m Não há nenhum perfil cadastrado!')
    time.sleep(0.5)
    os.system('clear')
    
  else:
    for x in range(len(lista_usuarios)):
      if login_email == lista_usuarios.__getitem__(x).getEmail():
        j = x
        break
  
    while login_email != lista_usuarios.__getitem__(x).getEmail() or loginsenha !=   lista_usuarios.__getitem__(x).getSenha():
      import time
      os.system('clear')
      print('\033[1;49;34m --- Planner TIGR --- \033[m')
      print('\n\033[1;49;92m LOGIN \033[m')
      print('\n\033[1;49;92m Salvando alterações... \033[m')
      time.sleep(1)
      print('\n\033[0;31m  ERRO!!!')
      print('\n\033[1;49;92m Seu E-mail ou senha estão incorretos!')
      print('\033[1;49;92m Efetue o login novamente')
      login_email=input('\n\033[0;92m Digite seu E-mail: ')
      loginsenha=input('\033[0;92m Digite sua Senha: ')
      os.system('clear')
    if login_email == (lista_usuarios.__getitem__(x).getEmail()) and loginsenha == (lista_usuarios.__getitem__(x).getSenha()):
        evento(j)

#Função exibirinfo(), específica para mostrar as informações do usário na telab
def exibirinfo(y):
  import time
  time.sleep(0.5)
  print('\n\033[1;49;92m Salvando alterações... \033[m')
  time.sleep(0.5)
  print('\033[1;49;92m As informações salvas foram: \033[m')
  print('\n\033[0;92m Nome:', lista_usuarios.__getitem__(y).getNome())
  print('\033[0;92m Idade:', lista_usuarios.__getitem__(y).getData_nascimento())
  print('\033[0;92m Telefone:', lista_usuarios.__getitem__(y).getTelefone())
  print('\033[0;92m E-mail', lista_usuarios.__getitem__(y).getEmail())
  print('\033[0;92m Senha:', lista_usuarios.__getitem__(y).getSenha())
  time.sleep(1)

#Função evento(), específica para o usuário criar um evento
def evento(k):
   os.system('clear')
   print('\033[1;49;34m --- Planner TIGR --- \033[m')
   print('\n\033[1;49;92m EVENTO \033[m')
   nn=input('\n\033[0;92m Você deseja agendar um evento? (S)-Sim ou (N)-Não):  ')
   os.system('clear')
   if nn == 's' or nn == 'S':
     while True:
       os.system('clear')
       print('\033[1;49;34m --- Planner TIGR --- \033[m')
       print('\n\033[1;49;92m EVENTO \033[m')
       agendarevento=input('\n\033[0;92m Digite seu evento: ')
       dataevento=input('\033[0;92m Adicione a data do seu evento: ')
       Eventos.append(eventos(k, agendarevento, dataevento))
       nn=input('\033[0;92m Você deseja agendar um novo evento? (S)-Sim ou (N)-Não: ')
       if nn == 'n' or nn == 'N':
         infoatualizadas(k)
         os.system('clear')
         break

#Função infoatualizadas(), específica para mostrar os dados do usuário atualizados, junto com o evento desejado (caso houver)
def infoatualizadas(j):
  import time
  os.system('clear')
  print('\033[1;49;34m --- Planner TIGR --- \033[m')
  if len(lista_usuarios) == 0:
    print('\n\033[1;31m Não há nenhum perfil cadastrado!')
  else:
    print('\n\033[1;49;92m PERFIL \033[m')
    print('\n\033[0;92m Nome:', lista_usuarios.__getitem__(j).getNome())
    print('\033[0;92m Idade: ', lista_usuarios.__getitem__(j).getData_nascimento())
    print('\033[0;92m Telefone/Contato: ', lista_usuarios.__getitem__(j).getTelefone())
    print('\033[0;92m E-mail cadastrado: ',lista_usuarios.__getitem__(j).getEmail())
    if len(Eventos) != 0:
      for x in range(len(Eventos)):
        if Eventos.__getitem__(x).getIndice() == j:
          print('\n\033[0;92m Posição:', x, '; \033[0;92m Evento:', Eventos.__getitem__(x).getEvento(), '; \033[0;92m Data:', Eventos.__getitem__(x).getData())
      op = input('\n\033[0;92m Você deseja excluir algum? (S)-Sim ou (N)-Não: ')
      if op == 's' or op == 'S':
        d = int(input('\033[0;92m Digite a posição (Apenas a posição do evento que deseja excluir!): ')) 
        Eventos.pop(d)
      for y in range(len(Eventos)):
        if Eventos.__getitem__(y).getIndice() == j:
          print('\n\033[0;92m Posição:', y, '; \033[0;92m Evento:', Eventos.__getitem__(y).getEvento(), '; \033[0;92m Data:', Eventos.__getitem__(y).getData())
    else:
      print('\nLista de eventos vazia!')
  time.sleep(2)
  os.system('clear')

#Condicional para o menu principal
while True:
  opcao=menu()
  if opcao == '1':
    os.system('clear')
    inicio()
  if opcao == '2':
    os.system('clear')
    login()
  if opcao == '3':
    os.system('clear')
    infoatualizadas(j)
  if opcao == '4':
    #Efeito visuais
    os.system('clear')
    import turtle 
    pen = turtle.Turtle() 
    pen.speed(0) 

#Biblioteca Gráfica
    def curve(): 
      for i in range(200): 
          pen.right(1) 
          pen.forward(1) 
    def heart():
        pen.fillcolor('red') 
        pen.begin_fill() 
        pen.left(140) 
        pen.forward(113) 
        curve() 
        pen.left(120) 
        curve() 
        pen.forward(112) 
        pen.end_fill() 
    def txt(): 
        pen.up() 
        pen.setpos(-57, 85) 
        pen.down()
        pen.color('white')
        pen.write("Obrigado",font=( "Quicksand", 18, "bold"))
    heart() 
    txt() 
    pen.ht()
    print('\033[0;92m Obrigado(a)!')
    break
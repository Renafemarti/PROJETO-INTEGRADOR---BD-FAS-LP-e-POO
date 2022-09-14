import os

class Usuario:
  global j
  global x
  global k
  Usuarios = []
  Eventos = []
  
  #Construtor
  def __init__(self, nome, data_nascimento, telefone, email, senha, endereco, curso, ie):
    #Atributos da nossa classe
    self.__nome=nome
    self.__data_nascimento=data_nascimento
    self.__telefone=telefone
    self.__email=email
    self.__senha=senha
    self.__endereco=endereco
    self.__curso=curso
    self.__ie=ie

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

  def getEndereco(self):
    return self.__endereco

  def getCurso(self):
    return self.__curso

  def getIe(self):
    return self.__ie

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

  def setEndereco(self, endereco):
    self.__endereco=endereco

  def setCurso(self, curso):
    self.__curso=curso

  def setIe(self, ie):
    self.__ie=ie
    
  def inicio(self):
    print('\033[1;49;34m --- Planner TIGR --- \033[m')
    print('\n\033[1;49;92m CADASTRO \033[m')
    print('\033[0;92m Faça seu cadastro: ')
    nome = input('\n\033[0;92m Nome: ')
    data_nascimento = input('\033[0;92m Idade: ')
    telefone = input('\033[0;92m Telefone: ')
    email = input('\033[0;92m E-mail: ')
    senha = input('\033[0;92m Senha: ')
    endereco = input('\033[0;92m Endereço: ')
    curso = input('\033[0;92m Curso que está cursando: ')
    ie = input('\033[0;92m Instituição de Ensino: ')
    Usuarios.append(Usuario(nome, data_nascimento, telefone, email, senha, endereco, curso, ie))
    exibirinfo(len(Usuarios)-1)
    login()

  def login(self):
    loginemail=input('Digite seu email: ')
    loginsenha=input('Digite sua senha: ')
    if (len(Usuarios) == 0):
      print('\n\033[1;31m Não há nenhum perfil cadastrado!')
      os.system('clear') 
    else:
      for x in range(len(Usuarios)):
        if login_email == Usuarios.__getitem__(x).getEmail():
          break
    while login_email != Usuarios.__getitem__(x).getEmail() or loginsenha !=   Usuarios.__getitem__(x).getSenha():
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
      if login_email == (Usuarios.__getitem__(x).getEmail()) and loginsenha == (Usuarios.__getitem__(x).getSenha()):
        menusecundario()
        
  def redefinirlogin(self):
      rdfl=input('Digite sua SENHA ATUAL: ')
      while rdfln != Usuarios.__getitem__(x).getSenha():
        print('Você digitou sua senha errada ')
        print('Digite sua senha novamente.\n ou Digite (2) para voltar para VOLTAR AO MENU')
        rdfln=input('Digite sua senha ou (2) :  ')

      if rdfl == (Usuarios.__getitem__(x).getSenha()):
        novasenha=input('Digite sua NOVA SENHA : ')
        Usuarios.append(Usuario(novasenha.__getintem__(x).setSenha()))
        print('!!!SENHA ALTERADA COM SUCESSO!!!')
        
  def agendarevento(self):
   os.system('clear')
   nn=input('\n\033[0;92m Você deseja agendar um evento? (S)-Sim ou (N)-Não):  ')
   os.system('clear')
   if nn == 's' or nn == 'S':
     adicionarevento()
  def consultarevento(self):
    
  def excluirevento(self):
    
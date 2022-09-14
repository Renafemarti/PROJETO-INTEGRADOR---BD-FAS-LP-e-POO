import os
class Contato:
  Contatos = []  
  def __init__(self, contato_pessoal, contato_institucional, email_pessoal, email_institucional):
    self.__contato_pessoal = contato_pessoal
    self.__contato_institucional = contato_institucional
    self.__email_pessoal = email_pessoal
    self.__email_institucional = email_institucional
    
    def getContato_p(self):
      return self.__contato_pessoal
      
    def setContato_p(self, contato_pessoal):
      self.__contato_pessoal = contato_pessoal
      
    def getContato_i(self):
      return self.__contato_institucional
      
    def setContato_i(self, contato_institucional):
      self.__contato_institucional = contato_institucional
      
    def getEmail_p(self):
      return self.__email_pessoal
      
    def setEmail_p(self, email_pessoal):
      self.__email_pessoal = email_pessoal
      
    def getEmail_i(self):
      return self.__email_institucional
      
    def setEmail_i(self, email_institucional):
      self.__email_institucional = email_institucional

    def contatos():
      ctt=input('Você deseja adicionar um contato?(S)-Sim e (N)-Não: ')
      if ctt=='S' or ctt=='s':
        qctt=input('Qual tipo de contato você quer adicionar (P)-Pessoa e (I)-Institucional : ')
        if qctt=='P' or qctt=='p':
          cont=input('Digite seu TELEFONE de contato ou EMAIL: ')
          Contatos.append(Contato(qctt))

        if qctt=='i' or qctt=='I':
          conti=input('Digite se EMAIL INSTITUCIONAL: ')
          Contatos.append(Contato(qctt))
      else:
        menusecundario()

    def acessarcontatos():
      
    def adicionarcontatos():
    def editarcontatos():
    def deletarcontatos():
      
class Evento():
  Eventos=[]
  global x
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

  def acessarevento():
    if len(Eventos) != 0:
      for x in range(len(Eventos)):
        if Eventos.__getitem__(x).getIndice() == j:
          print('\n\033[0;92m Posição:', x, '; \033[0;92m Evento:', Eventos.__getitem__(x).getEvento(), '; \033[0;92m Data:', Eventos.__getitem__(x).getData())
  def editardataevento():
    edi=input('\n\033[0;92m Você deseja agendar um evento? (S)-Sim ou (N)-Não):  ')
    if edi == 'S' or edi == 's':
      print('\n\033[0;92m Posição:', x, '; \033[0;92m Evento:', Eventos.__getitem__(x).getEvento(), '; \033[0;92m Data:', Eventos.__getitem__(x).getData())
      edic=input('Digite a posição(número antes do posterior ao evento: ) para a alteração de data:')
      Eventos.pop(d)
      for y in range(len(Eventos)):
        if Eventos.__getitem__(y).getIndice() == j:
          print('\n\033[0;92m Posição:', y, '; \033[0;92m Evento:', Eventos.__getitem__(y).getEvento(), '; \033[0;92m Data:', Eventos.__getitem__(y).getData())
    else:
      menusecundario()

  def editardescricaoevento():
    
  def adicionarevento():

  def deletarevento():
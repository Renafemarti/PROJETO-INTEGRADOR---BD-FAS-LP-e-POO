class Calendario():
  def __init__(self, dia, mes, ano):
    self.__dia = dia
    self.__mes = mes
    self.__ano = ano
    
    def getDia(self):
      return self.__dia
      
    def getMes(self):
      return self.__mes
      
    def getAno(self):
      return self.__ano
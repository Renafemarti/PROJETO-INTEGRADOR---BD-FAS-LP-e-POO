class Atividade:
  def __init__(self, prazo, lembrete, materia, horario_a):
    self.__prazo = prazo
    self.__lembrete = lembrete
    self.__materia = materia
    self.__horario_a = horario_a
    
    def getPrazo(self):
      return self.__prazo
      
    def setPrazo(self, prazo):
      self.__prazo = prazo
      
    def getLembrete(self):
      return self.__lembrete
      
    def getMateria(self):
      return self.__materia
      
    def setMateria(self, materia):
      self.__materia = materia
      
    def getHorario_a(self):
      return self.__horario_a
      
    def setHorario_a(self, horario_a):
      self.__horario_ = horario_a
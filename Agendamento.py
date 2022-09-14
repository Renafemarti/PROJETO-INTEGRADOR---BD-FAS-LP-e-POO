class Agendamento:
  def __init__(self, situacao_ca, situacao_ag):
    self.__situacao_ca = situacao_ca
    self.__situacao_ag = situacao_ag
    
    def getSituacao_ca(self):
      return self.__situacao_ca
      
    def setSituacao_ca(self, situacao_ca):
      self.__situacao_ca = situacao_ca
      
    def getSituacao_ag(self):
      return self.situacao_ag
      
    def setSituacao_ag(self, situacao_ag):
      self.__situcao_ag = situacao_ag


#https://www.hashtagtreinamentos.com/como-trabalhar-com-tempo-no-python?gclid=Cj0KCQjw94WZBhDtARIsAKxWG-_XwGnnlFgmIkAVvRl0BxHsLHpiMdIrZIm_uMeO8HfB3hAsssjUGnEaAqPQEALw_wc
#utilizar no codigo


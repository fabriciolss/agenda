class Times:
  def __init__(self):
    self.times = []
    self.proximo_id = 1

  def visualizar(self):
    return self.times

  def adicionar_lote(self, dados_json) -> bool:
    if not isinstance(dados_json, list):
      return False
    
    adicionados = 0
    for time in dados_json:
      if self.adicionar(time):
        adicionados += 1
    
    return adicionados > 0

  def adicionar(self, dados_json) -> bool:
    if not isinstance(dados_json, dict):
      return False

    if 'clube' in dados_json and 'estadio' in dados_json:
      if any(time['clube'] == dados_json['clube'] for time in self.times):
        return False

      time = {'id': self.proximo_id, 'clube': dados_json['clube'],'estadio': dados_json['estadio']}
      self.times.append(time)
      self.proximo_id += 1
      return True
    return False
  
  def deletar(self, id: int) -> bool:
    for time in self.times:
      if time['id'] == id:
        self.times.remove(time)
        return True
    return False
  
  def atualizar(self, id: int, dados_json) -> bool:
    if not isinstance(dados_json, dict):
      return False

    for time in self.times:
      if time['id'] == id:
        if 'clube' in dados_json:
          time['clube'] = dados_json['clube']
        if 'estadio' in dados_json:
          time['estadio'] = dados_json['estadio']
        return True
    return False

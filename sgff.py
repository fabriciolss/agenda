from abc import ABC, abstractmethod

class Funcionarios(ABC):
  def __init__(self, nome: str, idade: int or str, salario: float or str):
    self.nome = nome
    self.idade = int(idade)
    @property
    def salario(self):
      return self._salario
    
    @salario.setter
    def salario(self, value):
      self._salario = float(value)
    
    self._salario = float(salario)
    
  @abstractmethod
  def pagamento(self):
    pass

  @abstractmethod
  def iniciar_jogo(self):
    pass

class Jogador(Funcionarios):
  def __init__(self, nome, idade, salario):
    super().__init__(nome, idade, salario)
    self.partidas_jogadas = 0
    self.gols_marcados = 0
    self.multa_contratual = 500 * self._salario

  def iniciar_jogo(self):
    print(f"Jogador {self.nome} foi se vestir no vestiário.")

  def pagamento(self):
    return self._salario + self._salario * 0.05 * self.gols_marcados + self.partidas_jogadas * self._salario * 0.02
    
class Treinador(Funcionarios):
  def __init__(self, nome, idade, salario, status: Literal['BAIXO', 'MEDIO', 'ALTO', 'ELITE']):
    super().__init__(nome, idade, salario)
    self.partidas_ganhas = 0
    self.multa_contratual = 300 * salario if status == 'ELITE' else 0 

  def iniciar_jogo(self):
    print(f"Treinador {self.nome} foi montar a preleção técnica.")

  def pagamento(self):
    return self._salario + self._salario * 0.1 * self.partidas_ganhas

class Medico(Funcionarios):
  def __init__(self, nome, idade, salario):
    super().__init__(nome, idade, salario)

  def iniciar_jogo(self):
    print(f"Médico {self.nome} foi montar o kit de primeiros socorros.")

  def pagamento(self):
    return self._salario

class Diretor(Funcionarios):
  def __init__(self, nome, idade, salario):
    super().__init__(nome, idade, salario)
    self.resultado_clube = 0

  def iniciar_jogo(self):
    print(f"Diretor {self.nome} ao camarote receber os investidores e patrocinadores.")

  def pagamento(self):
    return self._salario + self._salario * 0.2 * self.resultado_clube
  
  def verificar_salario(self, Funcionarios):
    return Funcionarios._salario

class JogadorEstrela(Jogador, Diretor):
  def __init__(self, nome, idade, salario):
    super().__init__(**kwargs)
    self.multa_contratual = 500 * self._salario
  
  def iniciar_jogo(self):
    print(f"Jogador Estrela {self.nome} foi se vestir no vestiário.")
  
  def pagamento(self):
    return self._salario + self._salario * 0.05 * self.gols_marcados + self.partidas_jogadas * self._salario * 0.02 + self.partidas_ganhas * self._salario * 0.01
  
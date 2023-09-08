#importanto a biblioteca statistics:
import statistics
#importando a classe de obter os valores:
from Verificacao import Verificacao
#dizendo que a lista é igual ao resultado da verificação:
lista = Verificacao.receberNumeros()

class Moda:
    def calcularModa():
      try:
        moda = statistics.mode(lista)
        return print(f"A media dos números: {lista} é: {moda:.2f}")
      except statistics.StatisticsError:
        return print("Erro: Não há uma moda clara na lista.")

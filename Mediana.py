#para facilitar a escrita do código vamos importar a biblioteca statistics
import statistics
#importando a classe verificação:
from Verificacao import Verificacao
#dizendo que a lista é igual ao resultado da verificação:
lista = Verificacao.receberNumeros()

class Mediana:
  #usamos um bloco try para tentar executar a função e se der errado mostrar uma mensagem de erro
  def calcularMediana():
    try:
      mediana = statistics.median(lista)
      return print(f"A media dos números: {lista} é: {mediana:.2f}")
    except statistics.StatisticsError:
      return print("Erro: A lista está vazia ou contém valores não numéricos.")

Mediana.calcularMediana()
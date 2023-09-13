#para facilitar a escrita do código vamos importar a biblioteca statistics
import statistics
#importando a classe verificação:
from Verificacao import Verificacao

class Mediana:
  #usamos um bloco try para tentar executar a função e se der errado mostrar uma mensagem de erro.
  def calcularMediana():
    #dizendo que a lista é igual ao resultado da verificação:
    try:
      lista = Verificacao.receberNumeros()
      try:
        mediana = statistics.median(lista)
        return print(f"A mediana dos números: {lista} é: {mediana:.2f}")
      except:
        return print("Não conseguimos executar o calculo, por favor verifique os dados inseridos.")
    except:
      return print('Error')
    
    

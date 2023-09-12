#importanto a biblioteca statistics:
import statistics
#importando a classe de obter os valores:
from Verificacao import Verificacao


class Moda:
    #usamos um bloco try para tentar executar a função e se der errado mostrar uma mensagem de erro
    def calcularModa():
      #dizendo que a lista é igual ao resultado da verificação:
      try:
        lista = Verificacao.receberNumeros()
        try:
          moda = statistics.mode(lista)
          return print(f"A moda dos números: {lista} é: {moda:.2f}")
        except:
         return print("Não conseguimos executar o calculo, por favor verifique os dados inseridos.")
      except:
        return print('Erro')

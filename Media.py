#importando a classe de verificação:
from Verificacao import Verificacao
class Media:
  def calcularMedia():
    #usando a funcao de verificacao para receber os dados:
    try:
      lista = Verificacao.receberNumeros()
      #criando uma variavel para receber a soma dos numeros
      soma = 0
      #somando cada numero dos dados inseridos:
      for numero in lista:
        soma += numero
      #pegando a soma e dividindo pelo tamanho da lista
      media = soma / len(lista)
      print(f"A média dos números: {lista} é: {media:.2f}")
    except:
      return print('Não conseguimos executar esse calculo, por favor verifique os dados inseridos')
    
    
    
    
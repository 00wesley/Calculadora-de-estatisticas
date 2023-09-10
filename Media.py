#importando a classe de verificação:
from Verificacao import Verificacao
#usando a funcao de verificacao para receber os dados:
dados = Verificacao.receberNumeros()

class Media:
  def calcularMedia():
    #criando uma variavel para receber a soma dos numeros
    soma = 0
    #somando cada numero dos dados inseridos:
    for numero in dados:
      soma += numero
    #pegando a soma e dividindo pelo tamanho da lista
    media = soma / len(dados)
    print(f"A media dos números: {dados} é: {media:.2f}")
    
    
    
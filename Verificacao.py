#O Objetivo da classe é receber os números e transformá-los em dados do tipo número e também verificar se o usuário inseriu mais de um número

class Verificacao:
  def receberNumeros():
    #usando split para receber todos os números de uma vez:
    entrada = input("Digite os números separados por virgulas: ").split(',')
    if len(entrada) > 1:
      #criando uma lista para receber os números:
      numeros = []
      #verificando se os numeros inseridos são numeros, se for é inserido na lista, se não da erro.
      for item in entrada:
        numero = int(item)
        numeros.append(numero)
      return numeros
    else:
      return print('Para obter as estastisticas deve inserir mais de um número.')
    
        




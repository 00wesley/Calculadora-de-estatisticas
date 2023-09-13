from Media import Media
from Moda import Moda
from Mediana import Mediana

#Aqui temos a interação do usuário:
while True:
  options = input('Escolha uma opção:  \n'
                  '1. Calcular média\n'
                  '2. Calcular moda\n'
                  '3. Calcular mediana\n'
                  '4. Sair\n')
  
  if options == '1':
    Media.calcularMedia()
  elif options == '2':
    Moda.calcularModa()
  elif options == '3':
    Mediana.calcularMediana()
  elif options == '4':
    break
  else:
    print('Desculpe, você digitou uma opção invália.')
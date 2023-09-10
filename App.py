#Aqui temos a interação do usuário

while True:
  options = input('Escolha uma opção:  \n'
                  '1. Calcular media\n'
                  '2. Calcular moda\n'
                  '3. Calcular mediana\n'
                  '4. Sair\n')
  
  if options == '1':
    from Media import Media
    Media.calcularMedia()
  elif options == '2':
    from Moda import Moda
    Moda.calcularModa()
  elif options == '3':
    from Mediana import Mediana
    Mediana.calcularMediana()
  elif options == '4':
    break
  else:
    print('Desculpe, você digitou uma opção invália.')
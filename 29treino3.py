# Pedir para o usuario digitar três números e falar qual é o maior, após isso ordenar os números em ordem crescente


primeiro: int
segundo: int
terceiro: int
maior = int




primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))



if primeiro>segundo and primeiro>terceiro:
  print('primeiro é maior que segundo e terceiro: ')
  print(primeiro)
  print(segundo)
  print(terceiro)
elif segundo>primeiro and segundo>terceiro:
  print('segundo é maior que primeiro e terceiro: ')
  print(primeiro)
  print(segundo)
  print(terceiro)
else:
  print('terceiro é maior que primeiro e segundo: ')
  print(primeiro)
  print(segundo)
  print(terceiro)




#exibir o maior valor entre eles

numero1 = int(input('digite o primeiro numero:'))
numero2 = int(input('digite o segundo numero:'))

if numero1 > numero2:
    print(f"{numero1}' e maior{numero2}")
elif numero2 > numero1:
 print(f"{numero2} e maior que {numero1}")
else:
   print("os numeros são iguais")
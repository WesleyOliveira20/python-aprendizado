'''
if condição:
    # Bloco de código executado se a condição for verdadeira
elif outra_condição:
    # Bloco de código executado se a outra_condição for verdadeira
else:
    # Bloco de código executado se nenhuma das condições for verdadeira
'''           
'''

trabalho_terminado = True 
if trabalho_terminado == False: 
   print('Opa bora dar uma saida!')
else:
  print('Não posso sair agora!')

estou_lirvre = True 
if estou_lirvre == False : 
   print('posso te ajudar sim')
else: 
    print('não poso te ajudar,chama meu irmão!')



numero_atrasos = 0
if numero_atrasos >= 3:
    print(" você esta suspenso ")
elif numero_atrasos == 1:
    print('se atrasar mais duas vezes levara advertencia')
elif numero_atrasos == 2:
    print('caso chegue atrasado mais uma vez tomara suspensão')
elif numero_atrasos == 3:
    print('você foi suspenso')
else:
    print('pode entrar')

    '''

numero1 = int(input('Digite um numero: '))

numero2 = int(input('Digite o segundo numero:  '))

if numero1 > numero2:
    print('numero 1 maior que o numero 2 ')
elif numero2 > numero1:
    print('segundo mumero e maior que o primeiro')

else:
    print('os numeros são iguais')
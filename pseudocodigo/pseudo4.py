# Programa para calcular o fatorial de um número
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

# Pede o número para o usuário
numero = int(input('Digite um número para calcular o fatorial: '))

# Inicializa o fatorial como 1
fatorial = 1

# Calcula o fatorial
for i in range(1, numero + 1):
    fatorial = fatorial * i

# Mostra o resultado
print(f'O fatorial de {numero} é: {fatorial}')
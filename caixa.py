cont1 = 0
cont1 = 0
cont5 = 0
cont10 = 0
cont50 = 0
cont100 = 0

def sacar_notas(valor, valor_nota, cont):
    while valor >= valor_nota:
        valor -= valor_nota
        cont += 1
    return valor, cont

def cabecalho():
    print("*" * 40)
    print("Bem vindo ao Caixa Eletrônico STEM")
    print("*" * 40)

valor = 0
while valor > 600 or valor < 10:
    valor = int(input("Insira o valor do saque (entre 10 e 600): "))

cabecalho()
valor, cont100 = sacar_notas(valor, 100, cont100)
valor, cont50 = sacar_notas(valor, 50, cont50)
valor, cont10 = sacar_notas(valor, 10, cont10)
valor, cont5 = sacar_notas(valor, 5, cont5)
valor, cont1 = sacar_notas(valor, 1, cont1)

print("Quantidade de notas de 100:", cont100)
print("Quantidade de notas de 50:", cont50)
print("Quantidade de notas de 10:", cont10)
print("Quantidade de notas de 5:", cont5)
print("Quantidade de notas de 1:", cont1)

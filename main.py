from random import randint


def descobrir_numero_tentativas(valor):
    qtde = 0
    while valor != 0:
        valor = valor // 2
        qtde += 1
    return qtde


numero_maximo = int(input("Valor máximo possível (inteiro): "))
numero_min = 0

numero_aleatorio = randint(0, numero_maximo)

chute = numero_maximo // 2

chute_maximo = numero_maximo
chute_minimo = 0

tentativa = 0

while True:
    tentativa += 1
    print(f"{chute}")

    if chute < numero_aleatorio:
        print("Maior\n")
        chute_minimo = chute
        chute = (chute + chute_maximo) // 2

    elif chute > numero_aleatorio:
        print("Menor\n")
        chute_maximo = chute
        chute = (chute_maximo + chute_minimo) // 2

    elif chute == numero_aleatorio:
        print(f"Parabéns. O numero era {numero_aleatorio} - levou {tentativa} tentativas e o máximo de tentativas era {descobrir_numero_tentativas(numero_maximo)}")
        break

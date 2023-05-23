from random import randint

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
        print(f"Parabéns. O numero era {numero_aleatorio} - tentativas {tentativa}")
        break
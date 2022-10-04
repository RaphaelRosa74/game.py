import random

def jogar():

    print("Bem vindo ao jogo de Adivinhação!")
    print("=================================")

    numero_secreto = random.randrange(1, 51)
    pontos = 50

    print("Qual dificuldade gostaria de jogar?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nivel: "))

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        tentativa = input("Digite um numero entre 1 e 50: ")
        print("Você digitou", tentativa)
        chute = int(tentativa)

        if (chute < 1 or chute > 50):
            print("Tente um numero entre 1 e 50 :/")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e conseguiu {} pontos :D".format(pontos))
            break
        else:
            if (maior):
                print("Não foi dessa vez, tente chutar mais baixo na proxima :D")
            elif (menor):
                print("Não foi dessa vez, tente chutar mais alto na proxima :D")
            pontos_perdidos = int(abs(numero_secreto - chute))
            pontos = int(pontos - pontos_perdidos)

        print("Jogo encerrado, Obrigado por jogar ;)")

if(__name__ == "__main__"):
    jogar()
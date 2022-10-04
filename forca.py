import random

def jogar():

    menssagem_de_abertura()
    palavra_secreta = carregar_palavra_secreta()
    acertos = inicializa_acertos(palavra_secreta)
    print(acertos)

    enforcou = False
    acertou = False
    tentativas = 0

    while (not acertou and not enforcou):

        chute = chamar_chute()

        if (chute in palavra_secreta):
             marcar_chute(chute, acertos, palavra_secreta)

        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in acertos
        print(acertos)

    if(acertou):
        mensagem_ganhadora()
    else:
        menssagem_perdedora(palavra_secreta)

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_ganhadora():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def menssagem_perdedora(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def marcar_chute(chute, acertos, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            acertos[posicao] = letra
        posicao += 1

def chamar_chute():
    chute = input("Chute uma letra: ")
    chute = chute.strip().upper()
    return chute

def inicializa_acertos(palavra):
    return ["_" for letra in palavra]

def menssagem_de_abertura():
    print("¨¨¨¨Bem vindo ao jogo da Forca!")
    print("===============================")

def carregar_palavra_secreta():
        arquivo = open("palavra.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta

if(__name__ == "__main__"):
    jogar()

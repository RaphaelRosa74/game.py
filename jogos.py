import forca
import adivinhacao

def escolha_jogo():
    print("¨¨¨¨Escolha seu jogo!")
    print("=====================")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Diga qual jogo gostaria de jogar: "))

    if(jogo == 1):
        print("Vamos jogar Forca!")
        forca.jogar()
    elif(jogo == 2):
        print("Vamos jogar Adivinhação!")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()
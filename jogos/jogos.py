import forca
import adivinhacao

def escolhe_jogo():
    print("****************************************")
    print("Escolha qual jogo quer jogar")
    print("****************************************")

    print('(1) - Jogo da Forca (2) - Jogo de adivinhação')

    jogo = int(input("Digite o numero do jogo que quer jogar: "))

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()

if(__name__ == '__main__'):
    escolhe_jogo()
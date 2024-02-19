import random

def jogar():
    print("****************************************")
    print("Bem vindo ao jogo da forca!")
    print("****************************************")

    palavra = input("Digite a palavra: ").lower()
    letra_errada = []
    letra_correta = []
    chances = 5

    while chances > 0:

        letra = input("digite a letra: ").lower()

        if letra in palavra:
            letra_correta.append(letra)
        else:
            letra_errada.append(letra)
            print("letra incorreta")
            chances -= 1
        #
        palavra_atual = ''
        for letra_palavra in palavra:
            if letra_palavra in letra_correta:
                palavra_atual += letra_palavra
            else:
                palavra_atual += "_"

        print(f"Palavra atual: {palavra_atual}")
        print(f"Tentativas restantes: {chances}")
        print(f"Letras incorretas: {', '.join(letra_errada)}")

        if(palavra_atual == palavra):
            print(f"Parabéns. A palavra correta é {palavra}")
            break
        else:
            print(f"Você perdeu o jogo. A palavra correta era {palavra}");
            break
        chances = chances + 1


    print('GAME OVER')

if(__name__ == "__main__"):
    jogar()




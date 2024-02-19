import random

def jogar():
    print("****************************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("****************************************")
    #random.seed(10)
    numero_secreto = random.randrange(1,101) #gera um numero aletorio entre 1 e 100
    pontuacao = 1000


    print(f'Você começa com {pontuacao} pontos')
    print("Escolha o nível que você quer jogar? ")
    print(" Digite: (1) - FÁCIL (2) - MÉDIO (3) - DIFÍCIL")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 3

    for tentativas_atuais in range(1, tentativas + 1): #loop for que irá controlar o numero de tentativas
        print(f'Você tem um total de: {tentativas_atuais} tentativa de {tentativas}')
        print('\n')
        chute = int(input("Digite um numero entre 1 e 100: "))  # conversão de string para int


        if(chute < 1 or chute > 100): #verifica se o numero digitado é menor que 1 ou maior que zero
            print("Você digitou deve digitar um numero entre 1 e 100")
            continue
        if numero_secreto == chute:
            print("Numero correto! Você acertou ein")
            print(f'Você não perdeu nenhum ponto. Sua pontuação é de {pontuacao} pontos.')
            break
        elif chute > numero_secreto:
            print('Errou! O numero digitado é maior que o numero secreto.')
            pontos_perdidos = abs(numero_secreto - chute) #numero_secreto: 40 - chute: 20 = 20
            pontos = pontuacao - pontos_perdidos

        elif chute < numero_secreto:
            print("Errou! Numero digitado é menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)  #numero_secreto: 40 - chute: 20 = 20
            pontos = pontuacao - pontos_perdidos

    print('GAME OVER')
    print(f'O numero secreto é {numero_secreto}')
    print(f'Sua pontuação atual foi de {pontos}')

if(__name__ == "__main__"):
    jogar()
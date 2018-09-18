'''
Exercicio:Faça um programa que jogue PAR OU IMPAR com o computador.O jogo só sera interrompido
quando o jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
'''
import random
win = 0
lose = 0

while True:
    jogador = int(input('Digite um valor qualquer: '))
    pi = str(input('Par ou impar ? [P|I] ')).upper().strip()[0]

    lista_pc = [1,2,3,4,5,6,7,8,9,10]
    #Pc escolhe num 1 - 10
    pc = random.choice(lista_pc)
    #Soma determina se é PAR ou IMPAR
    s = pc + jogador
    if s % 2 == 0 and pi == 'P':
        win +=1
        print('\033[1;34mVocê Venceu!\033[m')
        print(f'Você jogou {v} e o computador jogou {pc}. Total deu {s} Deu Par')
        print('Vamos jogar novamente')

    elif s % 3 == 0 and pi == 'I':
        win +=1
        print('\033[1;34mVocê Venceu!\033[m')
        print(f'Você jogou {v} e o computador jogou {pc}. Total deu {s} Deu IMPAR')
    else:
        lose +=1

        print('\033[1;31mVocê perdeu\033[m')
        print(f'Você jogou {v} e o computador jogou {pc}. Total deu {s}')
        print(f'Derrotas: {lose} ')
        print(f'Vitorias: {win}')
        break

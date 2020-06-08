from classes import jogador, palavras
from functions import forca
import os

jogar = True

nome_jogador = input('Olá, qual o seu nome? ')

player = jogador.Jogador(nome_jogador)
palavra = palavras.Palavra()

palavra.sorteia()

while jogar:
    print(f'Bem vindo {player.nome}, tenha um bom jogo!')
    while True:

        # exibe a forca passando a quantidade de erros

        forca.Forca(player.erros)

        # printa as lacunas referente a palavra sorteada

        for lacuna in palavra.lacunas:
            print(lacuna, end='')

        print(f'\nDica: {palavra.dica}')

        # verifica a quantidade de erros do jogador

        if player.erros >= 6:
            player.registraderrotas()
            jogarNovamente = input('Deseja jogar novamente?(S/N): ').upper()

            if palavra.jogarnovamente(jogarNovamente):
                palavra.sorteia()
                player.erros = 0
                break
            else:
                print(f'Você jogou {player.partidas} partidas obtendo {player.perdeu} derrota(s) e {player.ganhou} vitória(s)')
                jogar = False
                break

        # verifica se o jogador já ganhou preechendo todas as lacunas possíveis

        if palavra.verificaresultado():
            print('Parabéns, você ganhou!!!\n')
            player.registraganho()
            jogarNovamente = input('Deseja jogar novamente?(S/N): ').upper()

            if palavra.jogarnovamente(jogarNovamente):
                palavra.sorteia()
                player.erros = 0
                break
            else:
                print(f'Você jogou {player.partidas} partidas obtendo {player.perdeu} derrota(s) e {player.ganhou} vitória(s)')
                jogar = False
                break

        letraDigitada = input('\nDigite uma letra: ')

        # verifica se a letra digitada faz parte da palavra sorteada

        for ind, letra in enumerate(palavra.letras):
            if letra == letraDigitada:
                palavra.substituilacuna(ind, letra.upper())
                player.acertou = True

        player.contaerros()


from classes import jogador, palavras
from functions import forca

jogar = True

player = jogador.Jogador('Odair')
palavra = palavras.Palavra()

palavra.sorteia()

while jogar:

    while True:

        forca.Forca(player.erros)

        for lacuna in palavra.lacunas:
            print(lacuna, end='')

        print(f'\nDica: {palavra.dica}')

        if player.erros >= 6:
            player.registraderrotas()
            jogarNovamente = input('Deseja jogar novamente?(S/N): ').upper()

            if palavra.jogarnovamente(jogarNovamente):
                palavra.sorteia()
                player.erros = 0
                player.acertou = False
                break
            else:
                jogar = False
                break

        if palavra.verificaresultado() is True:
            print('Parabéns, você ganhou!!!\n')
            player.registraganho()
            jogarNovamente = input('Deseja jogar novamente?(S/N): ').upper()

            if palavra.jogarnovamente(jogarNovamente):
                palavra.sorteia()
                player.erros = 0
                player.acertou  = False
                break
            else:
                jogar = False
                break

        letraDigitada = input('\nDigite uma letra: ')

        for ind, letra in enumerate(palavra.letras):
            if letra == letraDigitada:
                print('Encontrou a letra digitada')
                palavra.substituilacuna(ind, letra)
                player.acertou = True

        player.contaerros()


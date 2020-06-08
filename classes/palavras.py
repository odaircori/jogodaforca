import os
import random
import codecs

# carrega o arquivo de palavras e dicas

arquivo_path = os.path.abspath('arquivos/palavras.txt')

class Palavra(object):
    arquivo_completo = ''
    palavras = []
    palavra = ''
    dica = ''
    letras = ''
    lacunas = ''

    def __init__(self):
        arquivo_palavras = codecs.open(arquivo_path, 'r', encoding='utf-8')
        self.arquivo_completo = [texto for texto in arquivo_palavras]

    # verifica se ainda existe alguma lacuna vazia

    def verificaresultado(self):
        camposrestantes = [x for x in self.lacunas if x == '__ ']

        if len(camposrestantes) > 0:
            return False
        else:
            return True

    def sorteia(self):
        # adiciona somente palavras à lista "palavras" levando em consideração se o índice é par
        for ind, palavra in enumerate(self.arquivo_completo):
            if ind % 2 == 0:
                self.palavras.append(palavra)
        self.palavra = random.sample(self.palavras, len(self.palavras))[0]
        self.letras = [letra for letra in self.palavra.split()[0]]
        self.lacunas = ['__ ' for x in range(len(self.letras))]

        # encontra a dica para a palavra sorteada
        for ind, sorteada in enumerate(self.arquivo_completo):
            if sorteada == self.palavra:
                self.dica = self.arquivo_completo[ind + 1]
                break

    # adiciona a letra digitada à lista de lacunas
    def substituilacuna(self, ind, letra):
        self.lacunas[ind] = letra

    def jogarnovamente(self, jogarnovamente):
        if jogarnovamente == 'S':
            return True
        else:
            return False

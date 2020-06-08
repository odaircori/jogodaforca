import os
import random
import codecs

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

    def verificaresultado(self):
        camposrestantes = [x for x in self.lacunas if x == '__ ']

        if len(camposrestantes) > 0:
            return False
        else:
            return True

    def sorteia(self):
        for ind, palavra in enumerate(self.arquivo_completo):
            if ind % 2 == 0:
                self.palavras.append(palavra)
        self.palavra = random.sample(self.palavras, len(self.palavras))[0]
        self.letras = [letra for letra in self.palavra.split()[0]]
        self.lacunas = ['__ ' for x in range(len(self.letras))]

        #encontra a dica para a palavra sorteada
        for ind, sorteada in enumerate(self.arquivo_completo):
            if sorteada == self.palavra:
                print(f'Palavra sorteada é {sorteada}')
                self.dica = self.arquivo_completo[ind+1]
                break

    def substituilacuna(self, ind, letra):
        self.lacunas[ind] = letra.upper()

    def jogarnovamente(self, jogarnovamente):
        if jogarnovamente == 'S':
            self.acertos = 0
            return True
        else:
            return False

    def __del__(self):
        pass

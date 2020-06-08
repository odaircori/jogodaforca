class Jogador(object):
    def __init__(self, nome,):
        self.nome = nome

    partidas = 0
    ganhou = 0
    perdeu = 0
    erros = 0
    acertou = False

    def contaerros(self):
        if self.acertou:
            pass
        else:
            print('Mais um erro')
            self.erros+=1

    def registraganho(self):
        self.ganhou+=1

    def registraderrotas(self):
        self.perdeu+=1



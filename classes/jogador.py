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
            self.acertou = False
            pass
        else:
            self.acertou = False
            self.erros+=1

    def registraganho(self):
        self.ganhou+=1
        self.partidas+=1
        self.acertou = False

    def registraderrotas(self):
        self.perdeu+=1
        self.partidas+=1
        self.acertou = False



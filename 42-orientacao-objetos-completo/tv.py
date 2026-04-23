class TV:
    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self,novo_canal):
        self.canal = novo_canal
        # O conceito de canal do Lira é muito zoado!


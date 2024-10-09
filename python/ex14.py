class Configuracao:
    _instancia = None  

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Configuracao, cls).__new__(cls)
            
            cls._instancia.configuracoes = {}
        return cls._instancia

    def set_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor

    def get_configuracao(self, chave):
        return self.configuracoes.get(chave, None)


def main():
    
    config1 = Configuracao()
    config2 = Configuracao()

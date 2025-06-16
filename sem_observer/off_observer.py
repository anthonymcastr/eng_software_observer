class Loja:
    def __init__(self):
        self.produto_disponivel = False

    def novo_produto(self):
        self.produto_disponivel = True
        print("Novo produto chegou na CK Informática!")

class Cliente:
    def verificar_loja(self, loja):
        if loja.produto_disponivel:
            print("Cliente: Produto disponível, vou comprar!")
        else:
            print("Cliente: Ainda não chegou.")

loja = Loja()
cliente = Cliente()

cliente.verificar_loja(loja)  # checagem manual do cliente
loja.novo_produto() 
cliente.verificar_loja(loja)

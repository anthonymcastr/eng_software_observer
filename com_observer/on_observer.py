# Observer (interface)
class Observer:
    def update(self, produto):
        pass

# ConcreteObserver
class Cliente(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self, produto):
        print(f"{self.nome} foi notificado: {produto} disponível!")

# Subject (Publisher)
class Loja:
    def __init__(self):
        self.observers = []

    def registrar(self, observer):
        self.observers.append(observer)

    def remover(self, observer): # com o método remover disponível, posteriormente podemos implementar lógica onde caso o usuário não deseja estar mais na lista de avisos automaticos, ele possa ser removido
        self.observers.remove(observer)

    def notificar(self, produto): #funcao de notificação, onde todo cliente recebe a atualização sobre o novo produto disponível
        for observer in self.observers:
            observer.update(produto)

    def novo_produto(self, produto):
        print(f"Loja: {produto} chegou!") # incluimos o produto
        self.notificar(produto) # chama a função de notificação, pós inclusão do produto

# Teste
loja = Loja()
cliente1 = Cliente("Wagner")
cliente2 = Cliente("Anthony")

loja.registrar(cliente1)
loja.registrar(cliente2)

loja.novo_produto("Desktop I5 12400KF + 4060ti")



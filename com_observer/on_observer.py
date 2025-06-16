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

    def remover(self, observer):
        self.observers.remove(observer)

    def notificar(self, produto):
        for observer in self.observers:
            observer.update(produto)

    def novo_produto(self, produto):
        print(f"Loja: {produto} chegou!")
        self.notificar(produto)

# Teste
loja = Loja()
cliente1 = Cliente("Alice")
cliente2 = Cliente("Bob")

loja.registrar(cliente1)
loja.registrar(cliente2)

loja.novo_produto("iPhone 15")



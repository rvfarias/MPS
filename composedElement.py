from interface import GraphElementIF

class ComposedElement(GraphElementIF):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, element: GraphElementIF):
        self.children.append(element)

    def display(self, indent=0):
        #Exibe o nome do elemento com a indentação atual
        print(' ' * indent + f"ComposedElement: {self.name}")
        #Depois itera sobre seus filhos e chama display() recursivamente com indent + 2 para aumentar o recuo
        for child in self.children:
            child.display(indent + 2)


# Subclasses de ComposedElement
class NetNodeCollection(ComposedElement):
    def display(self, indent=0):
        #Mostra o tipo específico
        print(' ' * indent + f"NetNodeCollection: {self.name}")
        #Chama o método da classe mãe para continuar a exibição dos filhos
        super().display(indent + 2)

class Server(ComposedElement):
    def display(self, indent=0):
        #Mostra o tipo específico
        print(' ' * indent + f"Server: {self.name}")
        #Chama o método da classe mãe para continuar a exibição dos filhos
        super().display(indent + 2)

class NetNode(ComposedElement):
    def display(self, indent=0):
        #Mostra o tipo específico
        print(' ' * indent + f"NetNode: {self.name}")
        #Chama o método da classe mãe para continuar a exibição dos filhos
        super().display(indent + 2)

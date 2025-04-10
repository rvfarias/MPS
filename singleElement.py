from MPS.interface import GraphElementIF

class SingleElement(GraphElementIF):
    def __init__(self, name):
        self.name = name
#Exibe o nome do elemento com a indentação atual
    def display(self, indent=0):
        print(' ' * indent + f"SingleElement: {self.name}")


# Subclasses de SingleElement
class Service(SingleElement):
    #Exibe o nome do elemento com a indentação atual
    def display(self, indent=0):
        print(' ' * indent + f"Service: {self.name}")

class Block(SingleElement):
    #Exibe o nome do elemento com a indentação atual
    def display(self, indent=0):
        print(' ' * indent + f"Block: {self.name}")

class Connection(SingleElement):
    #Exibe o nome do elemento com a indentação atual
    def display(self, indent=0):
        print(' ' * indent + f"Connection: {self.name}")


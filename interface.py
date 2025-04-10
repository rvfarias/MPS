from abc import ABC, abstractmethod

#Essa é a interface abstrata, que obriga todas as classes filhas a implementarem o método display.
class GraphElementIF(ABC):
    @abstractmethod
    #Esse método é responsável por exibir a estrutura hierárquica dos elementos da rede 
    #Ele é recursivo e usa o parâmetro indent para controlar a indentação da saída, facilitando a visualização em forma de árvore.
    def display(self, indent=0):
        pass

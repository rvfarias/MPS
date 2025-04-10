from interface import GraphElementIF
from singleElement import *
from composedElement import *

#O método de projeto Composite permite tratar objetos individuais e coleções de objetos da mesma forma. 
#Assim, display() funciona tanto para elementos simples quanto compostos.
#O que permite uma maior facilidade de extensão ou seja,
#novos tipos de elementos podem ser adicionados sem modificar os existentes.
# E também permite o desacoplamento, já que a interface comum permite que o 
# código cliente interaja com elementos sem conhecer detalhes de implementação.

# Arquivo main que realiza a chamada da funação para simulação de uso
if __name__ == "__main__":
    # Elementos simples
    service = Service("DNS")
    block = Block("Firewall")
    connection = Connection("Fiber Link")

    # Elementos compostos
    net_node = NetNode("Node A")
    net_node.add(service)
    net_node.add(block)

    server = Server("Server X")
    server.add(connection)

    # Coleção de nós
    # A coleção imprime seu nome.
    collection = NetNodeCollection("Main Network")
    # Ela tem dois filhos: um NetNode e um Server, que são compostos.
    collection.add(net_node)
    collection.add(server)
    #Cada um deles chama display() novamente, e esse processo continua até chegar nos elementos simples
    collection.display()

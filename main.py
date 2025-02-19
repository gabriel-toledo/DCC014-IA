from Tree import Tree
from Backtracking import Backtracking
from BreadthFirst import BreadthFirst
from DepthFirst import DepthFirst

if __name__ == '__main__':
    print("--------------------------------Problema dos Missionarios e Canibais--------------------------------")
    print("Selecione o Algorigmo de Busca: ")
    print("1 - Backtracking")
    print("2 - Busca em Largura")
    print("3 - Busca em Profundidade")
    print("4 - Sair")
    option = int(input("Opcao: "))
    print("")
    
    while option != 4:
        tree = Tree()
        tree.printRoot()
        if option == 1:
            search = Backtracking()
        elif option == 2:
            search = BreadthFirst()
        elif option == 3:
            search = DepthFirst()
        elif option == 4:
            exit()
        else:
            print("Opção Inválida")
            exit()
    
        search.search()
        print("\nCaminho Solução: ")    
        tree.printTree()
        print("----------------------------------------------------------------------------------------------------\n")
        print("Selecione o Algorigmo de Busca: ")
        print("1 - Backtracking")
        print("2 - Busca em Largura")
        print("3 - Busca em Profundidade")
        print("4 - Sair")
        option = int(input("Opção: "))

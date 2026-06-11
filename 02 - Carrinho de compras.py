#Sistema de Carrinho de Compras

# CLASSE PRODUTO
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# CLASSE CARRINHO
class Carrinho:
    def __init__(self):
        self.itens = [] #TEM DE USAR O "SELF." ANTES DO NOME DA LISTA PORQUE ELA ESTA ASSOCIADA A DEFNIÇAO DO METODO DA CLASSE

    def adicionar_produto(self, nome, preco, quantidade):
        for item in self.itens:
            if item['produto'].nome == nome:
                item['quantidade'] += quantidade
                print(f"{nome} adicionado ao carrinho.")
                return

        produto = Produto(nome, preco)
        self.itens.append({'produto': produto, 'quantidade': quantidade})

        print(f"{nome} adicionado ao carrinho.")

    def remover_produto(self, nome): 
        for item in self.itens:
            if item['produto'].nome == nome:
                self.itens.remove(item)
                print(f"{nome} removido do carrinho.")
                return

        print("Produto não encontrado.")

    def listar_carrinho(self):
        if not self.itens:
            print("Carrinho vazio.")
            return

        print("\n--- Carrinho ---")
        for item in self.itens:
            produto = item['produto']
            quantidade = item['quantidade']
            subtotal = produto.preco * quantidade

            print(f"Produto: {produto.nome}")
            print(f"Preço: R$ {produto.preco:.2f}")
            print(f"Quantidade: {quantidade}")
            print(f"Subtotal: R$ {subtotal:.2f}")
            print("-----------------------")

    def calcular_total(self):
        if not self.itens:
            print("Carrinho vazio.")
            return

        total = 0
        for item in self.itens:
            total += item['produto'].preco * item['quantidade']

        print(f"Total da compra: R$ {total:.2f}")

# MENU
carrinho = Carrinho()

while True:
    print("\n========= MENU =========")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar carrinho")
    print("4 - Calcular total")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        carrinho.adicionar_produto(nome, preco, quantidade)

    elif opcao == "2":
        nome = input("Nome do produto para remover: ")
        carrinho.remover_produto(nome)

    elif opcao == "3":
        carrinho.listar_carrinho()

    elif opcao == "4":
        carrinho.calcular_total()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
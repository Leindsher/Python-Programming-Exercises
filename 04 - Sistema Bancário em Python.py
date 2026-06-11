# Criar um programa simulando um banco
# O número da conta deve ser criado de forma aleatória e não repetida

import random

# Lista global de contas
contas = []

# Classe Conta
class Conta:
    def __init__(self, nome, numero, saldo, limite):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    # Gerar número da conta
    def numero_conta(self):

        while True:
            numero = random.randint(1000, 9999)
            numero_existe = False

            for conta in contas:
                if conta.numero == numero:
                    numero_existe = True
                    break

            if not numero_existe:
                return numero

    # Depositar
    def depositar(self, valor):

        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")

        else:
            print("Valor inválido.")

    # Sacar
    def sacar(self, valor):

        if valor <= 0:
            print("Valor inválido.")

        elif valor > (self.saldo + self.limite):
            print("Saldo insuficiente.")

        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")

    # Extrato
    def extrato(self):

        print("\n===== EXTRATO =====")
        print(f"Nome: {self.nome}")
        print(f"Conta: {self.numero}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print(f"Limite: R$ {self.limite:.2f}")
        print("===================")

# Criar conta
def criar_conta():

    try:
        nome = input("Nome do cliente: ")
        limite = float(input("Limite da conta: "))
        contaa = Conta(nome, 0, 0, limite)
        numero = contaa.numero_conta()       
        nova_conta = Conta(nome, numero, 0, limite)
        contas.append(nova_conta)

        print("Conta criada com sucesso!")
        print(f"Número da conta: {nova_conta.numero}")

    except ValueError:
        print("Erro nos dados informados.")

# Listar contas
def listar_contas():

    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
        return

    print("\n===== CONTAS =====")

    for conta in contas:
        print(f"Nome: {conta.nome}")
        print(f"Conta: {conta.numero}")
        print(f"Saldo: R$ {conta.saldo:.2f}")
        print(f"Limite: R$ {conta.limite:.2f}")
        print("-" * 30)

# Buscar conta
def buscar_conta(numero):

    for conta in contas:
        if conta.numero == numero:
            return conta
    return None

# Programa principal
while True:

    print("\n========= MENU =========")
    print("1 - CRIAR CONTA")
    print("2 - DEPOSITAR")
    print("3 - SACAR")
    print("4 - EXTRATO")
    print("5 - LISTAR CONTAS")
    print("0 - SAIR")

    try:

        opcao = int(input("Escolha: "))

        # Criar conta
        if opcao == 1:
            criar_conta()

        # Depositar
        elif opcao == 2:
            numero = int(input("Número da conta: "))
            conta = buscar_conta(numero)

            if conta:
                valor = float(input("Valor depósito: "))
                conta.depositar(valor)

            else:
                print("Conta não encontrada.")

        # Sacar
        elif opcao == 3:
            numero = int(input("Número da conta: "))
            conta = buscar_conta(numero)

            if conta:
                valor = float(input("Valor saque: "))
                conta.sacar(valor)

            else:
                print("Conta não encontrada.")

        # Extrato
        elif opcao == 4:
            numero = int(input("Número da conta: "))
            conta = buscar_conta(numero)

            if conta:
                conta.extrato()

            else:
                print("Conta não encontrada.")

        # Listar contas
        elif opcao == 5:
            listar_contas()

        # Sair
        elif opcao == 0:
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

    except ValueError:
        print("Entrada inválida.")
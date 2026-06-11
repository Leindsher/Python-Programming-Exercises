#DESAFIO – Sistema Acadêmico com Herança

#classe pai/superclasse
class Pessoa:
    def __init__ (self, nome, endereco, RG, CPF, data_nascimento ):
        self.nome = nome
        self.endereco = endereco
        self.RG = RG
        self.CPF = CPF
        self.data_nascimento = data_nascimento        

    def exibir_dados(self):
        return f'Nome: {self.nome} | Endereço: {self.endereco} | RG: {self.RG} | CPF: {self.CPF} | Data de nascimento {self.data_nascimento}'

#classe filha/subclasse    
class Aluno(Pessoa):
    _contador = 1

    def __init__(self, nome, endereco, RG, CPF, data_nascimento, data_ingresso, curso, semestre, valor_mensalidade):
        super().__init__(nome, endereco, RG, CPF, data_nascimento)

        self.cod_aluno = Aluno._contador
        Aluno._contador += 1

        self.data_ingresso = data_ingresso
        self.curso = curso
        self.semestre = semestre
        self.valor_mensalidade = valor_mensalidade

    def exibir_dados(self):
        base = super().exibir_dados()
        return base + f' | Data de ingresso: {self.data_ingresso} | Cód. do aluno: {self.cod_aluno} | Curso: {self.curso} | Semestre: {self.semestre} | Valor da mensalidade: {self.valor_mensalidade}'


#classe filha/subclasse    
class Professor(Pessoa):
    _contador = 1

    def __init__(self, nome, endereco, RG, CPF, data_nascimento, disciplinas, data_admissao):
        super().__init__(nome, endereco, RG, CPF, data_nascimento)

        self.codigo_funcionario = Professor._contador
        Professor._contador += 1

        self.disciplinas = disciplinas
        self.data_admissao = data_admissao


    def exibir_dados(self):
        base = super().exibir_dados()
        return base + f' | Cód. de funcionário: {self.codigo_funcionario} | Disciplinas: {self.disciplinas} | Data de admissão: {self.data_admissao}'


#classe filha/subclasse    
class Estagiario(Pessoa):
    _contador = 1

    def __init__(self, nome, endereco, RG, CPF, data_nascimento, valor_bolsa, inicio_estagio, cod_aluno):
        super().__init__(nome, endereco, RG, CPF, data_nascimento)

        self.cod_estagiario = Estagiario._contador
        Estagiario._contador += 1

        self.valor_bolsa = valor_bolsa
        self.inicio_estagio = inicio_estagio
        self.cod_aluno = cod_aluno
    
    def exibir_dados(self):
        base = super().exibir_dados()
        return base + f' | Valor da bolsa: {self.valor_bolsa} | Data de início do estágio: {self.inicio_estagio} | Cód. de estagiário: {self.cod_estagiario} | Cód. de aluno: {self.cod_aluno}'

#listas dos cadastros
alunos = []
professores = []
estagiarios = []

#cadastro
def cadastrar_aluno():
    i1 = input('Nome: ')
    i2 = input('Endereço: ')
    i3 = input('RG: ')
    i4 = input('CPF: ')
    i5 = input('Data nascimento: ')
    i6 = input('Data ingresso: ')
    i7 = input('Curso: ')
    i8 = input('Semestre: ')
    i9 = input('Mensalidade: ')

    aluno = Aluno(i1, i2, i3, i4, i5, i6, i7, i8, i9) #aqui os nomes nao precisam ser os mesmos definidos la no método, porem precisam obedecer a mesma ordem, porque eles sao indexados pelo indice do metodo
    alunos.append(aluno)


def cadastrar_professor():
    i1 = input('Nome: ')
    i2 = input('Endereço: ')
    i3 = input('RG: ')
    i4 = input('CPF: ')
    i5 = input('Data nascimento: ')
    i6 = input('Disciplinas: ')
    i7 = input('Data admissão: ')

    professor = Professor(i1, i2, i3, i4, i5, i6, i7) #aqui os nomes nao precisam ser os mesmos definidos la no método, porem precisam obedecer a mesma ordem, porque eles sao indexados pelo indice do metodo
    professores.append(professor)


def cadastrar_estagiario():
    i1 = input('Nome: ')
    i2 = input('Endereço: ')
    i3 = input('RG: ')
    i4 = input('CPF: ')
    i5 = input('Data nascimento: ')
    i6 = input('Valor da bolsa: ')
    i7 = input('Início estágio: ')
    i8 = input('Código do aluno: ')

    estagiario = Estagiario(i1, i2, i3, i4, i5, i6, i7, i8) #aqui os nomes nao precisam ser os mesmos definidos la no método, porem precisam obedecer a mesma ordem, porque eles sao indexados pelo indice do metodo
    estagiarios.append(estagiario)

#listar alunos
def listar_alunos():
    print('\nALUNOS CADASTRADOS: ')
    listar(alunos)

#listar professores
def listar_professores():
    print('\nPROFESSORES CADASTRADOS: ')
    listar(professores)

#listar estagiario
def listar_estagiarios():
    print('\nESTAGIÁRIOS CADASTRADOS: ')
    listar(estagiarios)

#listar todas
def listar_todos():
    print('\n--- TODOS ---')
    print('\nALUNOS CADASTRADOS: ')
    listar(alunos)
    print('\nPROFESSORES CADASTRADOS: ')
    listar(professores)
    print('\nESTAGIÁRIOS CADASTRADOS: ')
    listar(estagiarios)

#se a lista estiver vazia
def listar(lista):
    if not lista:
        print('Nenhum cadastro.')
    for pessoa in lista:
        print(pessoa.exibir_dados())

#menu (sempre é a ultuma coisa)
while True:
    print('\n====SISTEMA DE CADASTROS====')
    print('1 - Cadastrar Aluno')
    print('2 - Cadastrar Professor')
    print('3 - Cadastrar Estagiário')
    print('4 - Listar Alunos')
    print('5 - Listar Professores')
    print('6 - Listar Estagiários')
    print('7 - Listar Todos')
    print('0 - Sair')

    op = input('Escolha: ')

    #cadastrar
    if op == '1':
        cadastrar_aluno()
    elif op == '2':
        cadastrar_professor()
    elif op == '3':
        cadastrar_estagiario()
    elif op == '4':
        listar_alunos()
    elif op == '5':
        listar_professores()
    elif op == '6':
        listar_estagiarios()
    elif op == '7':
        listar_todos()
    elif op == '0':
        break
    else:
        print('Opção inválida!')


def menu(lista):
    print('\n### Menu de Opções ###')
    print('[ 1 ] Cadastrar')
    print('[ 2 ] Excluir')
    print('[ 3 ] Listar')
    print('[ 4 ] Editar')
    print('[ 5 ] Fechar')
    print('###################### \n')

    opção = int(input("Selecione a opção: "))

    if opção == 1:
        cadastrar(lista)
    elif opção == 2:
        excluir(lista)
    elif opção == 3:
        listar(lista)
    elif opção == 4:
        editar(lista)
    elif opção == 5:
        fechar(lista)
    else:
        print('Opção digitada é inválida! Tente novamente.')
        menu(lista)


def editar(lista):
    chave = input('Digite a matrícula do(a) aluno(a) que deseja editar: ')

    for al in lista:
        if al['matricula'] == chave:
            al['nome']      = input('Nome: ')
            al['idade']     = int(input('Idade: '))
            al['cpf']        = input('CPF: ')

    print('Dados do(a) aluno(a) atualizados com sucesso!')

    menu(lista)

def cadastrar(lista):
    print('\n### Cadastrar ###')

    matricula      = input("Matrícula: ")
    nome    = input("Nome: ")
    idade   = int(input("Idade: "))
    cpf      = input("CPF: ")

    save(lista, matricula, nome, idade, cpf)
    print('Aluno(a) cadastrado(a) com sucesso!\n')

    verificacao = int(input("Gostaria de cadastrar um(a) novo(a) aluno(a)? [1-Sim/2-Não]: "))
    if verificacao == 1:
        cadastrar(lista)

    elif verificacao == 2:
        menu(lista)

    else:
        print("Opção selecionada incorreta! Por favor, digite 1 para SIM ou 2 para NÃO.")
        menu(lista)

def excluir(lista):
    matricula = input("Digite a matrícula do(a) aluno(a) a ser excluído(a): ")

    i = 0
    while i < len(lista):
        if lista[i]['matricula'] == matricula:
            del lista[i]
            print('O(a) aluno(a) foi excluído(a) com sucesso!')

        i += 1

    menu(lista)

def listar(lista, verificacao=0):
    print('\n### Alunos Cadastrados ###')

    for al in lista:
        print(al['matricula'] + ', ' + al['nome'] + ', ' + str(al['idade']) + ', ' + al['cpf'])

    if verificacao == 1:
        print('Programa finalizado')
    else:
        menu(lista)

def fechar(lista):
    listar(lista, 1)

def save(lista, matricula, nome, idade, cpf):
    lista.append({
        'matricula'    : matricula,
        'nome'  : nome,
        'idade' : idade,
        'cpf'    : cpf
    })

if __name__ == '__main__':
    lista = []
    menu(lista)
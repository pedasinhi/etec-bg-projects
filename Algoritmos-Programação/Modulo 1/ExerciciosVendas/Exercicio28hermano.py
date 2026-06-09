class Produto: #cria uma classe chamada produto.

    def __init__(self, nome: str, preco: float): # método construtor da classe, será executado toda vez que um objeto for criado, 'self' sendo o proprio objeto, 'nome: str' é um parametro do tipo texto, 'preco: float' sendo um parametro do tipo número decimal.
        self.nome = nome # armazena o nome recebido dentro do objeto.
        self.preco = preco # armazena o preço recebido dentro do objeto.

    def exibir(self, indice: int = None): # método para mostrar os dados do produto, 'indice' sendo opcional, '= none' significa que não pode receber valores, '-> none' indica que a função não retorna nada.
        prefixo = f"[{indice}] " if indice is not None else "    " # cria um prefixo para exibição, se existir indice mostra [0] ou [1], etc, se não existir mostrará apenas espaços (é um operador ternário(if em uma linha)).
        print(f"{prefixo}{self.nome:<25}  R$ {self.preco:>8.2f}") # mostra o produto formatado, '<25' alinha o nome á esquerda ocupando 25 espaços, '>8.2f' alinha o preço à direita

produtos: list[Produto] = [] # lista vazia (por enquanto) na qual produtos serão armazenados

def separador(char: str = "─", largura: int = 45): # função auxiliar que irá imprimir uma linha decorativa, 'char' sendo o caractere usado, 'largura' sendo o que define o tamanho da linha
    print(char * largura) # repetirá o caractere várias vezes 

def titulo(texto: str): # mostra um título formatado
    separador("═") # imprimirá uma linha que será mostrada acima do título
    print(f"  {texto}") # mostrará o texto do título
    separador("═") # imprimirá uma linha que será mostrada abaixo do título

def pausar(): # função que pausará o sistema
    input("\n  Pressione ENTER para continuar...") # espera que o usuário aperte a tecla ENTER

def cadastrar_produto(): # função responável por cadastrar produtos
    titulo("CADASTRAR PRODUTO") # mostrará o título na tela 

    nome = input(" Nome do produto: ").strip() # pede para o usário digitar um nome para o produto, '.strip()' sendo uma função "nativa" que remove espaços em branco
    if not nome: # verifica se o usuário não digitou nada
        print(" Nome não pode ser vazio. ") # mensagem que será mostrada caso nada seja digitado 
        pausar() # pausa e encerra a função
        return # encerra a execução da função imediatamente, voltando ao menu principal sem cadastrar nada

    try: # tenta executar um bloco
        preco = float(input("  Preço (R$): ").replace(",", ".")) # solicita que o usuário digite o preço do produto desejado, '.replace()' sendo uma função "nativa" que substitui o texto e/ou caractere indicado retornando algo novo
        if preco < 0: # caso o valor digitado for menor que 0, o código apontará erro, e será pedido que seja digitado um valor válido, 'raise' permite que seja lançado uma exceção manualmente no código, nesse caso ele está substituindo ',' para '.'
            raise ValueError("Preço não pode ser negativo.") # lança manualmente uma exceção do tipo ValueError com uma mensagem descritiva, interrompendo o bloco try
    except ValueError as erro: # captura qualquer erro do tipo ValueError, seja do float() ou do raise acima, e armazena a mensagem de erro na variável 'erro'
        print(f"   Entrada inválida: {erro}") # exibe a mensagem de erro capturada para informar o usuário do que ocorreu
        pausar() # aguarda o usuário pressionar ENTER antes de continuar
        return # encerra a função sem cadastrar o produto, voltando ao menu principal

    produto = Produto(nome, preco) # cria um novo objeto do tipo Produto passando o nome e preço digitados pelo usuário
    produtos.append(produto) # adiciona o objeto recém-criado ao final da lista global de produtos, '.append()' sendo uma função "nativa" que insere um elemento no fim de uma lista
    print(f"\n  Produto '{nome}' cadastrado com sucesso!") # exibe uma mensagem de confirmação com o nome do produto recém-cadastrado
    pausar() # aguarda o usuário pressionar ENTER para retornar ao menu principal

# Opção 2: Listar produtos
def listar_produtos(): # função responsável por exibir todos os produtos cadastrados na lista
    titulo("PRODUTOS CADASTRADOS") # mostra o título da seção na tela

    if not produtos: # verifica se a lista de produtos está vazia, 'not' invertendo o valor lógico, ou seja, 'True' se a lista estiver vazia
        print(" Nenhum produto cadastrado ainda.") # informa ao usuário que não há produtos para exibir
        pausar() # aguarda o usuário pressionar ENTER antes de continuar
        return # encerra a função sem exibir a tabela, pois não há dados para mostrar

    separador() # imprime uma linha decorativa acima do cabeçalho da tabela
    print(f"  {'Nº':<4}  {'Nome':<25}  {'Preço':>10}") # imprime o cabeçalho da tabela com colunas alinhadas, '<4' alinhando 'Nº' à esquerda em 4 espaços, '<25' alinhando 'Nome' à esquerda em 25 espaços e '>10' alinhando 'Preço' à direita em 10 espaços
    separador() # imprime uma linha decorativa abaixo do cabeçalho, separando-o dos dados
    for i, p in enumerate(produtos): # percorre a lista de produtos, 'enumerate()' retornando tanto o índice 'i' quanto o objeto produto 'p' a cada iteração
        p.exibir(i) # chama o método exibir do produto passando o índice para que seja mostrado o número do item na listagem
    separador() # imprime uma linha decorativa após o último produto, fechando a tabela visualmente
    print(f"  Total de produtos: {len(produtos)}") # exibe a quantidade total de produtos cadastrados, 'len()' sendo uma função "nativa" que retorna o número de elementos de uma lista
    pausar() # aguarda o usuário pressionar ENTER para retornar ao menu principal

# Opção 3: Comprar produto
def comprar_produto(): # função responsável por simular a compra de um produto cadastrado
    titulo("COMPRAR PRODUTO") # mostra o título da seção na tela
 
    if not produtos: # verifica se a lista está vazia antes de tentar exibir produtos para compra
        print("  Nenhum produto disponível. Cadastre produtos primeiro.") # informa ao usuário que é necessário cadastrar produtos antes de comprar
        pausar() # aguarda o usuário pressionar ENTER antes de continuar
        return # encerra a função sem prosseguir, pois não há produtos disponíveis

    # Exibe mini-listagem
    separador() # imprime uma linha decorativa antes de listar os produtos disponíveis
    for i, p in enumerate(produtos): # percorre a lista de produtos gerando o índice 'i' e o objeto 'p' a cada iteração
        p.exibir(i) # exibe cada produto com seu respectivo número de índice para o usuário escolher
    separador() # imprime uma linha decorativa após a listagem de produtos

    try: # tenta executar o bloco de leitura e validação do índice digitado pelo usuário
        indice = int(input("  Número do produto: ")) # lê o número digitado pelo usuário e converte para inteiro, 'int()' sendo uma função "nativa" que transforma texto em número inteiro
        if indice < 0 or indice >= len(produtos): # verifica se o índice está fora do intervalo válido da lista, usando operador lógico 'or' que retorna verdadeiro se qualquer uma das condições for verdadeira
            raise IndexError("Índice fora do intervalo.") # lança manualmente uma exceção do tipo IndexError caso o número digitado não corresponda a nenhum produto
    except ValueError: # captura o erro gerado pelo int() caso o usuário tenha digitado algo que não seja um número inteiro
        print("  Digite um número inteiro válido.") # informa ao usuário que o valor digitado não é um número inteiro válido
        pausar() # aguarda o usuário pressionar ENTER antes de continuar
        return # encerra a função sem prosseguir com a compra
    except IndexError as erro: # captura o IndexError lançado manualmente quando o índice está fora do intervalo, armazenando a mensagem na variável 'erro'
        print(f"  Produto não encontrado: {erro}") # exibe a mensagem de erro informando que o produto não foi encontrado
        pausar() # aguarda o usuário pressionar ENTER antes de continuar
        return # encerra a função sem prosseguir com a compra

    try: # tenta executar o bloco de leitura e validação da quantidade digitada pelo usuário
        quantidade = int(input("  Quantidade: ")) # lê a quantidade digitada pelo usuário e converte para inteiro
        if quantidade <= 0: # verifica se a quantidade é menor ou igual a zero, pois não é possível comprar zero ou menos unidades
            raise ValueError("Quantidade deve ser maior que zero.") # lança manualmente uma exceção caso a quantidade seja inválida
    except ValueError as erro: # captura erros do int() ou do raise acima, armazenando a mensagem na variável 'erro'
        print(f"  Entrada inválida: {erro}") # exibe a mensagem de erro para informar o usuário do problema na quantidade
        pausar() # aguarda o usuário pressionar ENTER antes de continuar
        return # encerra a função sem prosseguir com a compra

    produto_escolhido = produtos[indice] # acessa o produto da lista pelo índice escolhido e armazena na variável para uso a seguir
    total = produto_escolhido.preco * quantidade # calcula o valor total da compra multiplicando o preço unitário pela quantidade desejada

    separador() # imprime uma linha decorativa antes de exibir o resumo da compra
    print(f"  Produto   : {produto_escolhido.nome}") # exibe o nome do produto escolhido no resumo
    print(f"  Quantidade: {quantidade}") # exibe a quantidade informada pelo usuário no resumo
    print(f"  Preço unit: R$ {produto_escolhido.preco:.2f}") # exibe o preço unitário do produto formatado com duas casas decimais, ':.2f' sendo a formatação de número decimal com 2 casas
    separador() # imprime uma linha decorativa separando os detalhes do total
    print(f"  TOTAL  : R$ {total:.2f}") # exibe o valor total da compra formatado com duas casas decimais

    # Expressão relacional e lógica
    if total >= 100: # verifica se o total da compra é maior ou igual a R$ 100,00 para aplicar desconto
        print("  Desconto disponível!") # informa ao usuário que a compra atingiu o valor mínimo para desconto
    else: # caso o total seja menor que R$ 100,00, nenhum desconto é aplicado
        print("  Sem desconto (compras a partir de R$ 100,00).") # informa ao usuário que não há desconto pois o valor mínimo não foi atingido


    separador() # imprime uma linha decorativa ao final do resumo da compra
    pausar() # aguarda o usuário pressionar ENTER para retornar ao menu principal

def exibir_menu(): # função responsável por mostrar as opções do menu principal na tela
    separador() # imprime uma linha decorativa acima do título do menu
    print("      SISTEMA DE CADASTRO E COMPRA") # imprime o título do sistema no topo do menu
    print("  1 - Cadastrar produto") # exibe a opção 1 para o usuário cadastrar um novo produto
    print("  2 - Listar produtos") # exibe a opção 2 para o usuário visualizar todos os produtos cadastrados
    print("  3 - Comprar produto") # exibe a opção 3 para o usuário simular a compra de um produto
    print("  4 - Sair") # exibe a opção 4 para o usuário encerrar o programa
    separador() # imprime uma linha decorativa abaixo das opções do menu

def main(): # função principal que controla o fluxo do programa, sendo o ponto central de execução
    while True: # cria um laço infinito que mantém o menu sendo exibido repetidamente até o usuário escolher sair, 'True' garantindo que o loop nunca pare sozinho
        exibir_menu() # chama a função que imprime as opções do menu na tela a cada iteração do loop

        opcao = input("  Escolha uma opção: ").strip() # lê a opção digitada pelo usuário e remove espaços em branco com '.strip()'

        if opcao == "1": # verifica se o usuário digitou a opção 1
            cadastrar_produto() # chama a função responsável por cadastrar um novo produto
        elif opcao == "2": # verifica se o usuário digitou a opção 2
            listar_produtos() # chama a função responsável por listar todos os produtos cadastrados
        elif opcao == "3": # verifica se o usuário digitou a opção 3
            comprar_produto() # chama a função responsável por simular a compra de um produto
        elif opcao == "4": # verifica se o usuário digitou a opção 4 para encerrar o programa
            separador("═") # imprime uma linha decorativa antes da mensagem de despedida
            print(" Obrigado por usar o sistema. Até logo!") # exibe a mensagem de encerramento para o usuário
            separador("═") # imprime uma linha decorativa após a mensagem de despedida
            break # interrompe o laço 'while True', encerrando o programa
        else: # caso o usuário tenha digitado qualquer valor diferente de 1, 2, 3 ou 4
            print(" Opção inválida. Digite um número entre 1 e 4.") # informa ao usuário que a opção digitada não é válida
            pausar() # aguarda o usuário pressionar ENTER antes de exibir o menu novamente

# Ponto de entrada
if __name__ == "__main__": # verifica se o arquivo está sendo executado diretamente, '__name__' sendo uma variável especial do Python que vale '__main__' quando o arquivo é o principal
    main() # chama a função principal para iniciar o programa
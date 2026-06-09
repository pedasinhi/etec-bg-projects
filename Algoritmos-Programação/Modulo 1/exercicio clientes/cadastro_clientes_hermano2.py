import os                                                 # importa o módulo 'os', que permite interagir com o sistema operacional, como verificar se arquivos existem e montar caminhos de pastas

ARQUIVO_CLIENTES = r'C:\Users\1amod\Desktop\Enzo&Caua&Hermano123\exercicio clientes\clientes.txt' # define o caminho fixo do arquivo .txt na pasta do usuário, 'r' antes das aspas indica uma raw string, fazendo com que as barras '\' sejam tratadas como texto simples e não como caracteres especiais

def separador(char: str = "─", largura: int = 45): # função auxiliar que imprime uma linha decorativa, 'char' sendo o caractere usado com padrão "─", 'largura' definindo o tamanho da linha com padrão 45
    print(char * largura) # repete o caractere 'largura' vezes e imprime na tela

class Cliente: # cria uma classe chamada Cliente, responsável por representar os dados de um cliente

    def __init__(self, nome, idade, email, telefone): # método construtor da classe, executado automaticamente toda vez que um objeto Cliente for criado, 'self' sendo o próprio objeto
        self.__nome = nome # armazena o nome recebido dentro do objeto com encapsulamento, '__' tornando o atributo privado e acessível apenas dentro da própria classe
        self.__idade = idade # armazena a idade recebida dentro do objeto com encapsulamento privado
        self.__email = email # armazena o e-mail recebido dentro do objeto com encapsulamento privado
        self.__telefone = telefone # armazena o telefone recebido dentro do objeto com encapsulamento privado

    def get_nome(self): # método getter responsável por retornar o nome do cliente, permitindo acesso controlado ao atributo privado
        return self.__nome # retorna o valor do atributo privado '__nome'

    def get_idade(self): # método getter responsável por retornar a idade do cliente de forma controlada
        return self.__idade # retorna o valor do atributo privado '__idade'

    def get_email(self): # método getter responsável por retornar o e-mail do cliente de forma controlada
        return self.__email # retorna o valor do atributo privado '__email'

    def get_telefone(self): # método getter responsável por retornar o telefone do cliente de forma controlada
        return self.__telefone # retorna o valor do atributo privado '__telefone'

    def __str__(self): # método especial do Python chamado automaticamente quando o objeto é convertido para texto, como em 'print()' ou 'str()'
        return ( # retorna uma string formatada com todos os dados do cliente separados por ' | '
            f"Nome: {self.__nome} | " # inclui o nome do cliente na string de saída
            f"Idade: {self.__idade} | " # inclui a idade do cliente na string de saída
            f"E-mail: {self.__email} | " # inclui o e-mail do cliente na string de saída
            f"Telefone: {self.__telefone}" # inclui o telefone do cliente na string de saída
        )

class SistemaCadastro: # cria uma classe chamada SistemaCadastro, responsável por todas as operações do sistema como menu, cadastro, listagem e arquivos

    def __init__(self): # método construtor da classe, executado automaticamente ao criar um objeto SistemaCadastro
        self.__clientes = [] # inicializa uma lista vazia e privada que armazenará todos os objetos Cliente cadastrados
        self.__carregar_arquivo() # chama o método que tenta carregar clientes já salvos no arquivo .txt ao iniciar o sistema

    # Validações
    def __validar_nome(self, nome): # método privado responsável por validar o nome digitado, '__' indicando que só pode ser chamado dentro da própria classe
        if not nome.strip(): # verifica se o nome está vazio após remover espaços em branco com '.strip()', 'not' invertendo o valor lógico para True se estiver vazio
            raise ValueError("O nome não pode ser vazio.") # lança manualmente uma exceção do tipo ValueError caso o nome seja vazio, interrompendo a execução
        return nome.strip() # retorna o nome sem espaços nas extremidades caso seja válido

    def __validar_idade(self, idade_str): # método privado responsável por validar a idade digitada, recebendo-a como texto para verificar antes de converter
        try: # tenta executar o bloco de conversão da idade
            idade = int(idade_str) # tenta converter o texto digitado para número inteiro, 'int()' sendo uma função nativa do Python
        except ValueError: # captura o erro gerado pelo 'int()' caso o usuário tenha digitado algo que não seja um número
            raise ValueError("A idade deve ser um número inteiro.") # relança uma exceção mais descritiva informando que a idade precisa ser um número inteiro
        if idade <= 0: # verifica se a idade convertida é menor ou igual a zero, pois idades negativas ou zero não são válidas
            raise ValueError("A idade deve ser maior que zero.") # lança manualmente uma exceção caso a idade seja inválida
        return idade # retorna a idade como número inteiro caso todas as validações sejam aprovadas

    def __validar_email(self, email): # método privado responsável por validar o e-mail digitado
        if "@" not in email: # verifica se o caractere '@' está ausente no e-mail digitado, pois é obrigatório em qualquer endereço de e-mail
            raise ValueError("O e-mail deve conter '@'.") # lança manualmente uma exceção caso o '@' não seja encontrado no e-mail
        return email.strip() # retorna o e-mail sem espaços nas extremidades caso seja válido

    def __validar_telefone(self, telefone): # método privado responsável por validar o telefone digitado
        digits = "".join(filter(str.isdigit, telefone)) # filtra apenas os caracteres numéricos do telefone usando 'filter()' com 'str.isdigit', e os une em uma string com '""join()', deixa apenas numeros exemplo: de (11)91347-0374 para 11913470374
        if len(digits) != len(telefone.strip()): # compara o total de dígitos com o total de caracteres digitados; se forem diferentes, significa que há letras ou símbolos inválidos
            raise ValueError("O telefone deve conter apenas números.") # lança uma exceção informando que apenas números são aceitos no telefone
        if len(digits) < 10: # verifica se o telefone possui menos de 10 dígitos, quantidade mínima para um número válido no Brasil
            raise ValueError("O telefone deve possuir ao menos 10 dígitos.") # lança uma exceção informando que o telefone é curto demais
        return digits # retorna apenas os dígitos do telefone caso todas as validações sejam aprovadas

    # Operações principais
    def cadastrar_cliente(self): # método responsável por coletar, validar e registrar um novo cliente no sistema
        print() # imprime uma linha em branco para separar visualmente o conteúdo anterior
        separador("═") # imprime uma linha decorativa dupla acima do título usando o caractere '═'
        print("       CADASTRO DE CLIENTE") # exibe o título da seção de cadastro
        separador("═") # imprime uma linha decorativa dupla abaixo do título
        try: # tenta executar o bloco de coleta e validação dos dados do cliente
            nome = self.__validar_nome(input("Nome: ")) # solicita o nome ao usuário e passa para o método de validação, armazenando o resultado
            idade = self.__validar_idade(input("Idade: ")) # solicita a idade ao usuário e passa para o método de validação, armazenando o resultado
            email = self.__validar_email(input("E-mail: ")) # solicita o e-mail ao usuário e passa para o método de validação, armazenando o resultado
            telefone = self.__validar_telefone(input("Telefone: ")) # solicita o telefone ao usuário e passa para o método de validação, armazenando o resultado
        except ValueError as e: # captura qualquer exceção do tipo ValueError lançada pelos métodos de validação, armazenando a mensagem em 'e'
            print(f"[ERRO] {e}") # exibe a mensagem de erro descritiva para informar o usuário do que está incorreto
            return # encerra o método sem cadastrar nada, retornando ao menu principal

        cliente = Cliente(nome, idade, email, telefone) # cria um novo objeto do tipo Cliente passando todos os dados validados
        self.__clientes.append(cliente) # adiciona o objeto Cliente recém-criado ao final da lista privada de clientes, '.append()' sendo uma função nativa que insere no fim de uma lista
        self.__salvar_arquivo(cliente) # chama o método responsável por gravar os dados do novo cliente no arquivo .txt
        separador() # imprime uma linha decorativa antes da mensagem de confirmação
        print(" Cliente cadastrado com sucesso!") # exibe a mensagem de sucesso confirmando que o cliente foi cadastrado
        separador() # imprime uma linha decorativa após a mensagem de confirmação

    def listar_clientes(self): # método responsável por exibir todos os clientes cadastrados na lista
        print() # imprime uma linha em branco para separar visualmente o conteúdo anterior
        separador("═") # imprime uma linha decorativa dupla acima do título
        print("        LISTA DE CLIENTES") # exibe o título da seção de listagem
        separador("═") # imprime uma linha decorativa dupla abaixo do título
        if not self.__clientes: # verifica se a lista de clientes está vazia, '
            print("  Nenhum cliente cadastrado.") # informa ao usuário que ainda não há clientes registrados
            separador() # imprime uma linha decorativa encerrando a seção
            return # encerra o método sem exibir dados, retornando ao menu principal
        for i, cliente in enumerate(self.__clientes, start=1): # percorre a lista de clientes, 'enumerate()' retornando o índice 'i' e o objeto 'cliente' a cada iteração, 'start=1' iniciando a contagem em 1
            print(f"  {i}. {cliente}") # exibe o número sequencial e os dados formatados do cliente, chamando automaticamente o método '__str__' do objeto
            separador() # imprime uma linha decorativa após cada cliente para separar visualmente os registros

    def __reescrever_arquivo(self): #metodo de reescrever dados do cliente do sistema de cadastro 
        try:
            with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as arquivo: # Ele abre o arquivo no formato escrita (Write), encoding="utf-8"' garantindo suporte a acentos e caracteres especiais
                for cliente in self.__clientes: # Percorre o cliente dentro da classe de encapsulamento atributo clientes (Classe privada)
                    arquivo.write(str(cliente)) + "\n"
        except IOError as e: #captura erro de entrada/saida que podem ocorrer ao usuario tentar reescrever o arquivo e ele armazena isso em 'e'
                print(f"[ERRO ao atualizar o arquivo {e}]") #exibe a mensagem de erro descritiva para informar o usuaro do que está incorreto 

    def excluir_dados(self): #metodo de excluir dados do cliente do sistema de cadastro
        print() #Linha em branco para separar
        separador("=")# linha decorativa dupla acima do título 
        print("       EXCLUIR CLIENTE")# exibe o titulo da seção de listagem 
        separador("=")# linha decorativa dupla acima do título

        if not self.__clientes:# verifica se o cliente está cadastrado
            print("Nenhum cliente cadastrado.")# Se o cliente não estiver cadastrado ele informa que ainda não há clientes cadastrados
            separador() # linha decorativa após verificação de cliente cadastro 
            return # encerra o método sem exebir dados e retorna ao menu principal
         
        
        self.listar_clientes

        try:
            indice= int(input("Digite o numero do cliente que deseja excluir: ")) -1

            if indice <0 or indice >=len(self.__clientes):
                print("[ERRO] Cliente não encontrado")
                return
            
            cliente_removido = self.__clientes.pop(indice)

            self.__reescrever_arquivo()

            print()
            print(f"Cliente '{cliente_removido.get_nome()}' removido com sucesso.")

        except ValueError:
            print("[ERRO] Digite um numero valido.")

    def __salvar_arquivo(self, cliente): # método privado responsável por gravar os dados de um cliente no arquivo .txt
        try: # tenta executar o bloco de escrita no arquivo
            with open(ARQUIVO_CLIENTES, "a", encoding="utf-8") as arquivo: # abre o arquivo no modo 'a' (append) para adicionar sem apagar o conteúdo existente, 'encoding="utf-8"' garantindo suporte a acentos e caracteres especiais
                arquivo.write(str(cliente) + "\n") # converte o objeto cliente para texto com 'str()' e escreve uma linha no arquivo, '\n' pulando para a próxima linha
            print(f"[INFO] Dados salvos em: {ARQUIVO_CLIENTES}") # exibe o caminho completo do arquivo onde os dados foram salvos
        except IOError as e: # captura erros de entrada/saída que podem ocorrer ao tentar escrever no arquivo, armazenando a mensagem em 'e'
            print(f"[ERRO ao salvar arquivo] {e}") # exibe a mensagem de erro informando que não foi possível salvar os dados

    def __carregar_arquivo(self): # método privado responsável por ler o arquivo .txt e recarregar os clientes na lista ao iniciar o sistema
        if not os.path.exists(ARQUIVO_CLIENTES): # verifica se o arquivo ainda não existe usando 'os.path.exists()', 'not' invertendo para True caso não exista
            return # encerra o método sem fazer nada, pois não há arquivo para carregar
        try: # tenta executar o bloco de leitura do arquivo
            with open(ARQUIVO_CLIENTES, "r", encoding="utf-8") as arquivo: # abre o arquivo no modo 'r' (leitura) com suporte a caracteres especiais
                for linha in arquivo: # percorre cada linha do arquivo uma por uma
                    linha = linha.strip() # remove espaços em branco e quebras de linha das extremidades com '.strip()'
                    if not linha: # verifica se a linha está vazia após remover os espaços
                        continue # pula para a próxima iteração ignorando linhas em branco, 'continue' sendo uma instrução nativa que avança o loop
                    try: # tenta executar o bloco de reconstrução do objeto Cliente a partir do texto da linha
                        partes = dict( # cria um dicionário a partir dos pares "chave: valor" encontrados na linha. O código lê uma linha do arquivo, separa os campos pelo " | ", divide cada campo em chave e valor usando ": ", e transforma tudo em um dicionário para reconstruir o objeto Cliente.
                            item.split(": ", 1) # divide cada segmento no primeiro ': ' encontrado, separando a chave do valor
                            for item in linha.split(" | ") # divide a linha nos separadores ' | ' gerando os segmentos individuais de cada campo
                        )
                        cliente = Cliente( # cria um novo objeto Cliente com os dados extraídos do dicionário
                            partes["Nome"], # acessa o valor da chave "Nome" no dicionário
                            int(partes["Idade"]), # acessa e converte a idade para inteiro com 'int()'
                            partes["E-mail"], # acessa o valor da chave "E-mail" no dicionário
                            partes["Telefone"], # acessa o valor da chave "Telefone" no dicionário
                        )
                        self.__clientes.append(cliente) # adiciona o objeto Cliente reconstruído à lista privada de clientes
                    except (KeyError, ValueError): # captura erros de chave inexistente no dicionário ou de conversão de tipo inválida
                        pass # ignora silenciosamente a linha mal formatada e continua para a próxima, 'pass' sendo uma instrução que não faz nada
        except IOError as e: # captura erros de entrada/saída ao tentar abrir ou ler o arquivo
            print(f"[ERRO ao carregar arquivo] {e}") # exibe a mensagem de erro informando que não foi possível carregar os dados

    # Menu
    def exibir_menu(self): # método responsável por exibir o menu principal e controlar o fluxo de navegação do sistema
        while True: # cria um laço infinito que mantém o menu sendo exibido repetidamente até o usuário escolher sair, 'True' garantindo que o loop nunca pare sozinho
            print() # imprime uma linha em branco para separar visualmente cada exibição do menu
            separador("═") # imprime uma linha decorativa dupla acima do título do menu
            print("        MENU PRINCIPAL") # exibe o título do menu principal
            separador("═") # imprime uma linha decorativa dupla abaixo do título
            print("  1 - Cadastrar cliente") # exibe a opção 1 para cadastrar um novo cliente
            print("  2 - Listar clientes") # exibe a opção 2 para listar todos os clientes cadastrados
            print("  3 - Sair") # exibe a opção 3 para encerrar o programa
            separador() # imprime uma linha decorativa abaixo das opções antes do campo de entrada

            opcao = input("  Escolha uma opção: ").strip() # lê a opção digitada pelo usuário e remove espaços em branco com '.strip()'
            separador() # imprime uma linha decorativa após a entrada do usuário, antes de executar a opção

            if opcao == "1": # verifica se o usuário digitou a opção 1
                self.cadastrar_cliente() # chama o método responsável por cadastrar um novo cliente
            elif opcao == "2": # verifica se o usuário digitou a opção 2
                self.listar_clientes() # chama o método responsável por listar todos os clientes cadastrados
            elif opcao == "3": # verifica se o usuário digitou a opção 3 para encerrar o programa
                separador("═") # imprime uma linha decorativa dupla antes da mensagem de encerramento
                print("  Encerrando o sistema. Até logo!") # exibe a mensagem de despedida ao usuário
                separador("═") # imprime uma linha decorativa dupla após a mensagem de encerramento
                break # interrompe o laço 'while True', encerrando o programa
            else: # caso o usuário tenha digitado qualquer valor diferente de 1, 2 ou 3
                print("  [AVISO] Opção inválida. Digite 1, 2 ou 3.") # informa ao usuário que a opção digitada não é válida

# Ponto de entrada
if __name__ == "__main__": # verifica se o arquivo está sendo executado diretamente, '__name__' sendo uma variável especial do Python que vale '__main__' quando o arquivo é o principal
    sistema = SistemaCadastro() # cria um objeto da classe SistemaCadastro, disparando o construtor que inicializa a lista e carrega o arquivo
    sistema.exibir_menu() # chama o método que inicia o loop do menu principal, dando início à execução do sistema
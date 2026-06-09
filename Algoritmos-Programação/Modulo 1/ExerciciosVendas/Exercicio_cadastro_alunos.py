def classificar_aluno(nota):
    # determina se o aluno é aprovado, recuperação ou reprovado
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def calcular_media(alunos):
    # calcula a média da turma sem usar sum()
    total = 0

    for aluno in alunos:
        total = total + aluno["nota"]

    media = total / len(alunos)
    return media


alunos = []  # lista onde os alunos serão armazenados

while True:
    print()

    nome = input("Digite o nome do aluno: ")

    # tratamento da idade
    while True:
        try:
            idade = int(input("Digite a idade: "))

            if idade <= 0:
                print("Erro: A idade deve ser maior que 0.")
            else:
                break

        except ValueError:
            print("Erro: Digite um número inteiro.")

    # tratamento da nota
    while True:
        try:
            nota = float(input("Digite a nota: "))

            if nota < 0 or nota > 10:
                print("Erro: A nota deve estar entre 0 e 10.")
            else:
                break

        except ValueError:
            print("Erro: Digite um número válido.")

    # cria o dicionário do aluno
    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota,
        "situacao": classificar_aluno(nota)
    }

    # adiciona o aluno na lista
    alunos.append(aluno)

    # pergunta se deseja continuar
    while True:
        continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower().strip()

        if continuar == "s" or continuar == "n":
            break
        else:
            print("Erro: Digite apenas 's' ou 'n'.")

    if continuar == "n":
        break


# mostra os alunos cadastrados
print()
print("----- RESULTADO -----")

for aluno in alunos:
    print(
        f"Aluno: {aluno['nome']} | "
        f"Idade: {aluno['idade']} | "
        f"Nota: {aluno['nota']} | "
        f"Situação: {aluno['situacao']}"
    )

# calcula média
media = calcular_media(alunos)

# contadores
aprovados = 0
recuperacao = 0
reprovados = 0

# variáveis para maior e menor nota
maior = alunos[0]
menor = alunos[0]

# percorre a lista
for aluno in alunos:

    # conta situações
    if aluno["situacao"] == "Aprovado":
        aprovados = aprovados + 1

    elif aluno["situacao"] == "Recuperação":
        recuperacao = recuperacao + 1

    else:
        reprovados = reprovados + 1

    # verifica maior nota
    if aluno["nota"] > maior["nota"]:
        maior = aluno

    # verifica menor nota
    if aluno["nota"] < menor["nota"]:
        menor = aluno


# mostra resultados finais
print()
print(f"Média da turma: {media:.2f}")

print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")

print()
print(f"Aluno com maior nota: {maior['nome']} - {maior['nota']}")
print(f"Aluno com menor nota: {menor['nome']} - {menor['nota']}")
Idade = int(input("Digite sua idade: "))

def IdadeLegal(num):
    return(f"{'Maior de idade' if num >= 18 else 'Menor de idade'}")

print(IdadeLegal(Idade))
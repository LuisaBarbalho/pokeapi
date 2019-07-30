# Tratamento de Exceção

nome = input("Digite seu nome: ")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Idade inválida, tente novamente.")

print(f"Seu nome é {nome} e sua idade é {idade}.")
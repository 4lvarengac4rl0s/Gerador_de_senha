import random

print (f"Bem vindo ao seu gerador de senhas!")

letras_minusculas = "abcdefghijlmnopqrstuvxzkw"
letras_maiusculas = "ABCDEFGHIJLMNOPQRSTUVXZKW"
numeros = "1234567890"
especiais = "!@#$%&"
caracteres = letras_maiusculas + letras_minusculas + numeros + especiais

numero_de_senhas = int(input(f"\nQuantas senhas deseja criar? "))
tamanho_da_senha = int(input(f"\nQuantos caracteres deve ter senha? "))

for pwd in range(numero_de_senhas):
    senha = ""
    
    for c in range(tamanho_da_senha):
        senha += random.choice(caracteres)

    if(numero_de_senhas == 1):
        print(f"\nA senha gerada foi: {senha}")
    else: 
        print(f"\nAs senhas geradas foram: {senha}")

input("\nTecle Enter para fechar o programa...")
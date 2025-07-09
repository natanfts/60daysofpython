entrada = input("Coloque o numero: ")

try: #tente rodar
    numero = int(entrada)
    if numero % 2 == 0:
        print("Numero é par")
    else:
        print("Numero impar")
except ValueError:
    print("Você não passou um numero inteiro")
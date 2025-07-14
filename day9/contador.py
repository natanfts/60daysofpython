
def contador_personalizado():
    try:
        limite = int(input("Digite o valor máximo do contador: "))
        #função range cria uma lista de numero a partir do 0
        #até o valor definido pelo usuário
        limite = limite + 1
        for i in range(limite):
            print(i) 
            if i == limite:
                print("Contador atingiu o limite")
                break
    except ValueError:
        print("Entrada invalida. Por favor insira um numero inteiro.")
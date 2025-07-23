"""
primeiro passo, pegar as notas
segundo passo, somar as quatro notas
terceiro passo, dividir as notas
verificar se a nota tá dentro da média
mostrar resultado aprovado/reprovado
"""
def media_nota():
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        print("A nota deve estar entre 0 e 10.")
        nota1 = float(input("Digite a primeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        print("A nota deve estar entre 0 e 10.")
        nota2 = float(input("Digite a segunda nota: "))

    nota3 = float(input("Digite a terceira nota: "))
    while nota3 < 0 or nota3 > 10:
        print("A nota deve estar entre 0 e 10.")
        nota3 = float(input("Digite a terceira nota: "))

    nota4 = float(input("Digite a quarta nota: "))
    while nota4 < 0 or nota4 > 10:
        print("A nota deve estar entre 0 e 10.")
        nota4 = float(input("Digite a quarta nota: "))

    
    media = (nota1 + nota2 + nota3 + nota4) / 4
    #limitar a nota de zero a dez

    if media >= 7:
        print(f"Sua média foi {media} aprovada.")
    else:
        print(f"Sua média foi {media} reprovada.")    
        

media_nota()

"""
passo1, altura e peso
passo2, calcular o IMC(peso / altura ** 2)
passo3, retornar o calculo
"""

#def massa_corporal():
    

    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    

    imc = peso / (altura ** 2) 
    print(imc)
    if imc < 18.5:
        print("Está abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Peso normal")
    elif 25 <= imc < 30:
        print("acima do peso")
    elif 30 <= imc < 35:
        print("Obesidade grau 1")
    elif 35 <= imc < 40:
        print("Obesidade grau 2")
    else:
        print("Obesidade grau 3")
        
    
    
massa_corporal()   
   
    
    

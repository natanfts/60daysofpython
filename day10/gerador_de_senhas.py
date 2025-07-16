import random 
import string

#string forcene um conjunto de caracteres prontos
#random fornece funções para gerar numeros aleatorios
#como letras maisculas, numeros e simbolos



def gerador_de_senhas(tamanho):
    comprimento = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    
    while  len(senha) < comprimento:
        senha += random.choice(caracteres)
        
    print(f"Sua senha ficou assim: {senha}")   
gerador_de_senhas(30)

# não repetir o print para evitar o erro "none"
        
        
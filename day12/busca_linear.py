def busca_linear(lista, numero_procurado):
    """
    procurar um numero dentro de uma lista utilizando busca linear
    
    :paramêtro lista: lista de numeros
    :paramêtro numero_procurado: o numero que iremos procurar
    """
    
    for i, numero in enumerate(lista): #função nativa do python enumerate
    #enumerate passa por cada item dentro de uma lista, enquanto contabiliza
 
         if numero == numero_procurado:
             return i
    return -1
    
lista = [1,2,3,4,5,6,7,8,11]
numero_procurado = 7
    
buscando_o_numero = busca_linear(lista, numero_procurado)
#print(buscando_o_numero)

if buscando_o_numero != -1:
    print(f"o numero se encontra no indice: {buscando_o_numero}")
else:
    print("numero não encontrado")    
     
     
         
      
    
    
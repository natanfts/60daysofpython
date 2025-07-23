def fatorial(n):
    
    
    
    if n <0:
        raise ValueError("O numero deve ser positivo")
    if n == 0 or n == 1:
        return 1
    
    return n * fatorial (n -1)


try:
    print(f"fatorial igual a {fatorial(5)}")
except ValueError as e:
    print(e)


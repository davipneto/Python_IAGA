def tabuada(n: int):
    print(f"Tabuada do {n}:")
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")

def somarNumeros(n: int):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

tabuada(5)
print(somarNumeros(10))
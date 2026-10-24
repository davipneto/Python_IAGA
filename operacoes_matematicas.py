from math import sqrt

n = int(input("Digite um número: "))

dobro = n * 2
triplo = n * 3
quadrado = n ** 2
cubo = n ** 3
raiz = sqrt(n)

print()
print(f"Sendo n = {n}, temos:")
print(f"O dobro de {n} é {dobro}")
print(f"O triplo de {n} é {triplo}")
print(f"O quadrado de {n} é {quadrado}")
print(f"O cubo de {n} é {cubo}")
print(f"A raiz quadrada de {n} é {raiz:.4f}")
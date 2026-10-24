paciente = input("Digite o nome do paciente: ")
peso = float(input("Digite o peso do paciente (em kg): "))
altura = float(input("Digite a altura do paciente (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print()
print(f"Nome do Paciente: {paciente}")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
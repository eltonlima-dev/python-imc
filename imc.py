nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite o nome da sua cidade: ")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc > 18.5 and imc <25:
  print("Peso ideal")
else:
  print("Fora do peso ideal")

print(f"Bem vindo {nome}")

continuar = "s"

while continuar == "s":
    peso = float(input("Digite seu peso (KG): "))
    altura = float(input("Digite sua altura (M): "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade grau 1"
    elif imc < 40:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3"

    print("\n===== RESULTADO =====")
    print(f" Seu IMC: {imc:.2f}")
    print(f" Classificacao: {classificacao}")
    print("====================")

    continuar = input("\nDeseja calcular novamente? (s/n): ").lower()
print("insira sua altura")
altura= input()
print("insira seu peso")
peso=input()
try:
    altura=float(altura)
    peso=float(peso)

    resultado = altura *altura
    imc = peso/resultado

    if imc >=40:
        print("seu corpo pede socorro")
    elif imc >=39.9:
        print("obesidade grau 2")
    elif imc>=34.9:
        print("obesidade garu 1")
    elif imc>=29.9:
        print("sobre peso")
    elif imc>=24.9:
        print("peso normal")
    elif imc>=18.5:
        print("precisa comer")
    else:
        print("magro")
except:
    print("numero desconhecido")
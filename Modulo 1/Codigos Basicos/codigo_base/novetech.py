def soma (n1,n2):
   
    return n1 + n2

def subtrair(n1,n2):

    return n1 - n2

def multiplicar(n1,n2):
    
    return n1 * n2

def dividir(n1,n2):
   
    return n1 / n2
try:

    numero1= int(input("digite o primeiro numero: "))
    numero2= int(input("digite o segundo numero: "))

    opção = input("digite a opção que deseja:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n")
    if opção == "1":
        print(f"a soma dos numeros é: {soma(numero1,numero2)}")
    elif opção == "2":
        print(f"a subtração dos numero é:{subtrair(numero1,numero2)}")
    elif opção == "3":
        print(f"a multiplicação dos numero é:{multiplicar(numero1,numero2)}")
    elif opção == "4":
        print(f"a divisão dos numeros é:{dividir(numero1,numero2)}")
    else:
        print("numero invalido")
except:
    print("numero desconhecido")
finally:
    print("numero nao existente")
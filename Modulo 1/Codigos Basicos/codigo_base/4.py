def soma():
    n1 = float(input("digite o primeiro numero:"))
    n2 = float(input("digite o segundo numero :"))
    print(n1 + n2)

def subtraçao(n1,n2):
    
    print(n1-n2)

while True:
    opçao = input("1 - opçao1\n2 - opçao 2\n0 - sair\n")
    if opçao == "0":
        print("sair")
        break 
    elif opçao == "1":
        soma()
    elif opçao == "2":
        n1 = float(input("digite o primeiro numero:"))
        n2 = float(input("digite o segundo numero :"))
        subtraçao(n1,n2)
    else:
        print("opçao invalida")


nome=input("qual e o seu nome?")
idade=int(input("qual sua idade"))
possui_carteira = input("possui carteira de motorista? \n (1-sim/2-nao)")
 
if idade >= 18:
    if possui_carteira== "sim":
        print("pode dirigir")
    else:
        print("nao pode dirigir")
else:
   print("menor de idade")
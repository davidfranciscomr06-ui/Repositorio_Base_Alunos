print("digite sua idade")
try:
    idade=int(input())
    if idade <18:
        print("menor de idade")
    else:
        print("maior de idade")
finally:
    print("idade desconhecida")
    

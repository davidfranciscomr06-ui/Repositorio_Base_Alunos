try:
    temperatura = float(input("digite a temperatura em celsius:"))

    if temperatura >=30:

        print("esta quente!")
    if temperatura >=20:
        print("esta agradavel!")
    if temperatura >=10:
        print("esta frio!")
    else:
        print ("esta muito frio!")
except:
    print("numero desconhecido")
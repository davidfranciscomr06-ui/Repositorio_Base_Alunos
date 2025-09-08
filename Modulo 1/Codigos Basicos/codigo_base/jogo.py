nome=input("digite o nome")
email = input("digite o e-mail:")

with open("pessoa.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"{nome} | {email}\n")

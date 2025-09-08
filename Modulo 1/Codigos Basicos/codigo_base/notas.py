print("digite seu nome")
nome=input()
print("digite sua primera nota")
nota1=input()

print("digite a segunda nota")
nota2=input()

print("digite a terceira nota")
nota3=input()

nota1=float(nota1)
nota2=float(nota2)
nota3=float(nota3)
 
resultado=nota1 + nota2 + nota3
media = resultado/ 3
 
if media >= 5:
    print("aprovado")
elif media > 4:
    print("recuperaçao")
else:
    print("reprovado")
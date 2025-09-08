i = 1
while i <= 3:
    
    nome=input("insira seu nome")
    nota1=float(input("digite sua nota"))
    nota2=float(input("digite sua nota"))
    nota3=float(input("digite sua nota"))

    resultado = nota1 + nota2 + nota3
    media = resultado/3 
    i=i+1
    print (f"aluno: {nome}, media: {media:.1f}")
  
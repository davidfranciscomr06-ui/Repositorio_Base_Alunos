try:
    print("digite primeiro numero") #print aonde mostra para escrever como exemplo
    variavel =int(input()) # e começa por exemplo aonde o usuario escreve,int converte para inteiro e o input pega informaçao 
    for i in range(1,11): # e aqui e feito uma lista e repetiçao atraves dos comandos 
        print(variavel * i)#print printa e mostra aonde escrever na execulçao da maquina 
except:
    print("numero desconhecido")
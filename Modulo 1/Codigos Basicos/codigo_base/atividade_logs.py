#abrir o arquivo de log no phyton,colar os dois arquivos em uma pasta e visualizar a ordem e gerar um comando
#que leia as linhas de cima a baixo e identifique qual linha esta com erro ou algo faltandocamio
caminho_arquivo = "C:\\Users\\Aluno_Programador\\Desktop\\aula\\atv_logs\logs.txt"
palavra_chave = "WARNING"

with open(caminho_arquivo, "r",encoding="utf-8") as logs:
    for linha in logs:
        if palavra_chave in linha:
         print(linha.strip())

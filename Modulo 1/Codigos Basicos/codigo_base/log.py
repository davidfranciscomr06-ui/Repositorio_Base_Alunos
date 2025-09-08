#variaveis
nome_arquivo = "exemplo_logs.txt"
palavra_chave = "erro"
lista_linhas = ["2025-07-27 INFO: Tudo funcionando bem.","2025-07-27 10:00:05 DEBUG: Processando requisição ID: 123.","2025-07-27 10:00:10 ERRO: Falha ao conectar ao banco de dados."]
quantidade_erros = 0

for linha in lista_linhas:
    if palavra_chave in linha:
        print(linha)




#previsao_tempo = "previsão do tempo : chuva"

#EXEMPLO AVULSO
#if "chuva" in previsao_tempo :
  #####for fruta in frutas:
    #print(f"eu gosto de {fruta}")
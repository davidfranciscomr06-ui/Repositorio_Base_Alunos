nome_produto = ("digite o nome do produto")
preço= float(input("digite o preço do produto:"))
desconto = float (input("digite o percentual de desconto:"))
valor_desconto = preço * desconto /100
preço_final = preço - valor_desconto
print(f"produto:{nome_produto} - preço final:R$ {preço - valor_desconto}")

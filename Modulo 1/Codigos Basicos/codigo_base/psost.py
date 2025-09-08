import requests
dados = {'titulo':'meu post',
'conteudo': 'este e o conteudo do meu post.','usuariold':1}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json = dados)

print(response.status_code)
print(response.json())
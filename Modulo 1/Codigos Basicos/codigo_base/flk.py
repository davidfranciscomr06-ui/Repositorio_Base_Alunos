from flask import Flask,jsonify
app = Flask (__name__)


usuario = {
    "nome":"Ana",
    "frase": "cliente 00001 falha na diretriz",
    "idade":17,
    "hobbies": ["justin biber","rocket league","fotografia"],
    "ativo":True 
}


@app.route('/api',methods= ['get'])
def hello_api ():
    return jsonify(usuario)


app.run(host= "0.0.0.0",debug = True)
from flask import Flask, jsonify,request

app = Flask(__name__)

playlist = [
    {"id": 1, "titulo": " Everybody ", "artista": "Backstreet Boys ","link": "https://youtu.be/e-syzbglE6g?si=zWAV7p7LKp09_NSx"},
    {"id": 2, "titulo": "beat it", "artista": "michael jackson","link":"https://youtu.be/8fO8jVZ3T9g?si=l_-4axlB4wweUSeS"},

    
]
@app.route('/musicas', methods= ['get'])
def get_musicas():

    return jsonify({"playlist": playlist, "total": len(playlist)})

@app.route("/musicas/<int:id>",methods = ['get'])
def get_musica(id):
    for musica in playlist:
        if musica["id"] == id :
            return jsonify(musica),200
    return "", 204

@app.route("/musicas",methods = ['POST'])
def add_musica():
    nova_musica = request.json


    nova_musica["id"] = len (playlist) + 1
    

    playlist.append (nova_musica)
    return jsonify({"mensagem": "musica aducionados!", "musica":nova_musica}), 201
app.run()


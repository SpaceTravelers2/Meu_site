from flask import Flask, jsonify, request

app = Flask(__name__)

playlist = [
    {"id":1,"titulo":"Bohemian Rhapsody","artista":"Queen"},
    {"id":2,"titulo":"Shape of You","artista":"Ed Sheeran"}
]
@app.route('/musicas', methods=['GET'])
def get_musicas():
    return jsonify({"playlist": playlist, "total": len(playlist)})

@app.route('/musicas', methods=['POST'])
def add_musica():
    nova_musica = request.json
    nova_musica["id"] = len(playlist) + 1
    playlist.append(nova_musica)
    return jsonify({"mensagem":"Música adicionada!","musica":nova_musica}), 201

@app.route('/musicas/<int:id>')
def musica_id(id):
    for musica in playlist:
        if musica["id"] == id:
            return jsonify(musica)
    return {"mensagem":"Musica não encontrada"}

app.run(host="0.0.0.0",debug=True)
from flask import Flask ,jsonify
from funcoes import *

json_file = 'json_data.json'
dados = abrirArquivo(json_file)

app = Flask(__name__)

@app.route("/")
def index():
    versao = {"versao":"0.0.1"}
    return jsonify(versao),200

@app.get("/instituicoes")
def getInstituicoesResource():
    return jsonify(dados),200

@app.get("/instituicoes/<int:id>")
def getInstituicoesByIdResource(id):
    if(acharItemByIdBinarySearch( dados, id, 'CO_ENTIDADE') == -1):
       return jsonify({"erro": "Entidade não encontrada"}),404
    else: 
        instituicao = dados[acharItemByIdBinarySearch( dados, id, 'CO_ENTIDADE')]
        return jsonify(instituicao),200

# @app.delete("/instituicoes/<int:id>")
# def deleteInstituicoesByIdResource(id):
#     instituicao = acharItemByIdLinearSearch(dados, id,'CO_ENTIDADE')
#     deletarItem(json_file,dados,instituicao )
#     return jsonify(instituicao),200

@app.delete("/instituicoes/<int:id>")
def deleteInstituicoesByIdResource(id):
    if(acharItemByIdBinarySearch( dados, id, 'CO_ENTIDADE') == -1):
       return jsonify({"erro": "Entidade não encontrada"}),404
    else: 
        instituicao = dados[acharItemByIdBinarySearch( dados, id, 'CO_ENTIDADE')]
        deletarItem(json_file,dados,instituicao )
        return jsonify(instituicao),200
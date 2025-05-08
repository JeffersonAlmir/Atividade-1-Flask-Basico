from flask import Flask,request ,jsonify
import sqlite3

from models.InstituicaoEnsino import InstituicaoEnsino


app = Flask(__name__)

@app.route("/")
def index():
    versao = {"versao":"0.0.1"}
    return jsonify(versao),200

@app.get("/instituicoes")
def getInstituicoesResource():
    try:
        page = request.args.get("page",1, type = int)
        limit = request.args.get("limit",1, type = int)
        offset = (page -1) * limit

        conn = sqlite3.connect('entidades.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM entidades LIMIT ? OFFSET ?',(limit,offset))
        resultSet = cursor.fetchall()
        instituicoesEnsino = [InstituicaoEnsino(*row).toDict()  for row in resultSet]

    except sqlite3.Error as e:
         return jsonify({"mensagem": "Problema com o banco de dados."}), 500
    finally:
        conn.close()

    return jsonify(instituicoesEnsino),200



@app.get("/instituicoes/<int:id>")
def getInstituicoesByIdResource(id):
    try:
        conn = sqlite3.connect('entidades.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM entidades WHERE CO_ENTIDADE = ?",(id,))
        row = cursor.fetchone()

        if not row:
             return jsonify({"mensagem":"Instituição de ensino não encontrada."}), 404
        
        instituicaoEnsino = InstituicaoEnsino(*row)
        

    except sqlite3.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados."}), 500
    
    finally:
        conn.close()

    return jsonify(instituicaoEnsino.toDict()),200



@app.delete("/instituicoes/<int:id>")
def deleteInstituicaoResource(id):
    try:
        conn = sqlite3.connect('entidades.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM entidades WHERE CO_ENTIDADE = ?",(id,))
        conn.commit()

    except sqlite3.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados."}), 500
    
    finally:
        conn.close()

    return "", 200


@app.post("/instituicoes")
def createInstituicaoResource():

    try:
        instituicaoJson = request.get_json()
       
        keysList = ["co_entidade", "co_regiao", "no_regiao", "no_uf", "sg_uf", "no_municipio",
                "no_mesorregiao", "no_microrregiao", "no_entidade", "qt_mat_bas",
                "qt_mat_inf", "qt_mat_fund", "qt_mat_med", "qt_mat_med_ct",
                "qt_mat_med_nm", "qt_mat_prof", "qt_mat_prof_tec", "qt_mat_eja", "qt_mat_esp"]
        
        instituicao = tuple(instituicaoJson[key] for key in keysList)

        conn = sqlite3.connect('entidades.db')
        cursor = conn.cursor()
        cursor.execute("""
                    INSERT INTO entidades
                        (CO_ENTIDADE, CO_REGIAO, NO_REGIAO, NO_UF, SG_UF, NO_MUNICIPIO, 
                        NO_MESORREGIAO, NO_MICRORREGIAO, NO_ENTIDADE, QT_MAT_BAS, QT_MAT_INF, 
                        QT_MAT_FUND, QT_MAT_MED, QT_MAT_MED_CT, QT_MAT_MED_NM, QT_MAT_PROF, QT_MAT_PROF_TEC,
                        QT_MAT_EJA, QT_MAT_ESP)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",instituicao)
        
        instituicaoEnsino = InstituicaoEnsino(*instituicao)
        
        conn.commit()

    except sqlite3.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados."}), 500
    
    finally:
        conn.close()

    return jsonify(instituicaoEnsino.toDict()),201


@app.put("/instituicoes/<int:id>")
def updateInstituicaoResource(id):
    try:
        instituicaoJson = request.get_json()
        keysList = ["co_entidade", "co_regiao", "no_regiao", "no_uf", "sg_uf", "no_municipio",
                "no_mesorregiao", "no_microrregiao", "no_entidade", "qt_mat_bas",
                "qt_mat_inf", "qt_mat_fund", "qt_mat_med", "qt_mat_med_ct",
                "qt_mat_med_nm", "qt_mat_prof", "qt_mat_prof_tec", "qt_mat_eja", "qt_mat_esp"]
        
        instituicao = tuple(instituicaoJson[key] for key in keysList)

        conn = sqlite3.connect('entidades.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM entidades WHERE CO_ENTIDADE = ?',(id,))
        existe = cursor.fetchone()
        
        if not existe:
            return jsonify({"mensagem":"Instituição de ensino não encontrada."}), 404
        
        cursor.execute(""" 
                UPDATE entidades
                SET CO_REGIAO = ?, NO_REGIAO = ?, NO_UF = ?, SG_UF = ?, NO_MUNICIPIO = ?, 
                    NO_MESORREGIAO = ?, NO_MICRORREGIAO = ?, NO_ENTIDADE = ?, QT_MAT_BAS = ?, 
                    QT_MAT_INF = ?, QT_MAT_FUND = ?, QT_MAT_MED = ?, QT_MAT_MED_CT = ?, 
                    QT_MAT_MED_NM = ?, QT_MAT_PROF = ?, QT_MAT_PROF_TEC = ?, QT_MAT_EJA = ?, QT_MAT_ESP = ?
                WHERE CO_ENTIDADE = ?;""", instituicao[1:] + (id,))
        
        instituicaoEnsino = InstituicaoEnsino(*instituicao)
        
        conn.commit()

    except sqlite3.Error as e:
        return jsonify({"mensagem": "Problema com o banco de dados."}), 500
    
    finally:
        conn.close()

    return jsonify(instituicaoEnsino.toDict()),201

    
from flask import Flask, jsonify, request



app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})  

@app.route('/usuarios/<string:nombre>')
def usuario(nombre): 
    return jsonify({"name": nombre})

@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({"id": id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return nombre

#GET todos los 'recursos'
@app.route('/recurso', methods = ['GET'])
def get_recursos():
    return jsonify({"data": "lista de todos los items del recurso"})

#POST nuevo 'recurso'
@app.route('/recurso', methods = ['POST'])
def post_recursos():
    print (request.get_json())
    body = request.get_json()
    name= body["name"]
    modelo= body["modelo"]
    #insertar en la BD
    return jsonify({ "recurso":{
        "name" : name,
        "modelo" : modelo
    }})

#GET un 'recurso' a traves de su id 
@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id):
    #buscar en la BD un registro con ese id
    return jsonify({"recurso":{ 
        "name": "nombre correspondiente a ese id", 
        "modelo": "modelo correspondiente a ese id"
        }})


if __name__ == '__main__':
    app.run(debug=True, port = 5000)

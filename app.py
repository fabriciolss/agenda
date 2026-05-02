from flask import Flask, jsonify, request
import api_times as api

app = Flask(__name__)

time = api.Times()

@app.route('/', methods=['GET'])
def read():
  return jsonify(time.visualizar())

@app.route('/cadastro', methods=['POST'])
def create():
  data = request.get_json(silent=True)
  if not data:
    return jsonify({"message": "JSON inválido ou vazio"}), 400
    
  cadastro_suc = time.adicionar(data)
  
  if cadastro_suc:
    return jsonify({"message": "Cadastro realizado com sucesso!"}), 201
  return jsonify({"message": "Inválido. Revise a documentação"}), 404

@app.route('/cadastro/lote', methods=['POST'])
def create_all():
  data = request.get_json(silent=True)
  if not data:
    return jsonify({"message": "JSON inválido ou vazio"}), 400

  cadastro_suc = time.adicionar_lote(data)
  
  if cadastro_suc:
    return jsonify({"message": "Cadastro realizado com sucesso!"}), 201
  return jsonify({"message": "Inválido. Revise a documentação"}), 404

@app.route('/deletar/<int:id>', methods=['DELETE'])
def delete(id):
  delete_suc = time.deletar(int(id))

  if delete_suc:
    return jsonify(), 204
  return jsonify({"message": "Não localizado. Verifique se o ID está correto."}), 404

@app.route('/atualizar/<int:id>', methods=['PUT'])
def update(id):
  data = request.get_json(silent=True) 
  if not data:
    return jsonify({"message": "JSON inválido ou vazio"}), 400

  update_suc = time.atualizar(id, data)

  if update_suc:
    return jsonify({"message": "Cadastro atualizado com sucesso!"}), 200
  return jsonify({"message": "Inválido. Revise a documentação"}), 404

if __name__ == '__main__':
  app.run(debug=True)
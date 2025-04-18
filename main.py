from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__, static_folder='frontend', template_folder='frontend')
CORS(app)

DADOS_PATH = 'dados.json'

# Rota da página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para arquivos estáticos (CSS, JS, etc.)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('frontend', filename)

# Rota para agendar consulta
@app.route('/api/agendar', methods=['POST'])
def agendar():
    dados = request.get_json()
    try:
        with open(DADOS_PATH, 'r') as f:
            agendamentos = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        agendamentos = []

    agendamentos.append(dados)

    with open(DADOS_PATH, 'w') as f:
        json.dump(agendamentos, f, indent=4)

    return jsonify({"mensagem": "Agendamento realizado com sucesso!"})

# Rota para consultar agendamentos por CPF
@app.route('/api/consultar/<cpf>', methods=['GET'])
def consultar(cpf):
    try:
        with open(DADOS_PATH, 'r') as f:
            agendamentos = json.load(f)
        filtrados = [a for a in agendamentos if a.get('cpf') == cpf]
        return jsonify(filtrados)
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify([])

# Rota para cancelar agendamento por CPF
@app.route('/api/cancelar/<cpf>', methods=['DELETE'])
def cancelar(cpf):
    try:
        with open(DADOS_PATH, 'r') as f:
            agendamentos = json.load(f)
        agendamentos = [a for a in agendamentos if a.get('cpf') != cpf]
        with open(DADOS_PATH, 'w') as f:
            json.dump(agendamentos, f, indent=4)
        return jsonify({"mensagem": "Agendamento cancelado com sucesso!"})
    except (FileNotFoundError, json.JSONDecodeError):
        return jsonify({"erro": "Erro ao processar cancelamento"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

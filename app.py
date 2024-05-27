from flask import Flask, request, jsonify
import datetime



app = Flask(__name__)

# Lista fictícia para armazenar as missões
missoes = []

@app.route('/api/v1/missoes', methods=['POST'])
def create_missao():
    # Extrair dados da requisição
    missao_data = request.json
    
    # Adicionar nova missão à lista
    missoes.append(missao_data)
    
    return jsonify(missao_data), 201

@app.route('/api/v1/missoes', methods=['GET'])
def read_missions():
    # Ordenar missões por data de lançamento em ordem decrescente
    classificacao_missao = sorted(missoes, key=lambda x: x['Data de lançamento'], reverse=True)
    
    return jsonify(classificacao_missao)

@app.route('/api/v1/missoes/<int:missao_id>', methods=['GET'])
def get_mission_details(missao_id):
    # Encontrar missão pelo ID
    missao = next((missao for missao in missoes if missao['id'] == missao_id), None)
    
    if missao:
        return jsonify(missao)
    else:
        return jsonify({'error': 'Missão não encontrada'}), 404

@app.route('/api/v1/missoes/<int:missao_id>', methods=['PUT'])
def update_missao(missao_id):
    # Extrair dados da requisição
    missao_data = request.json
    
    # Atualizar missão existente
    for i, missao in enumerate(missoes):
        if missao['id'] == missao_id:
            missoes[i] = missao_data
            break
    
    return jsonify(missao_data), 200

@app.route('/api/v1/missoes/<int:missao_id>', methods=['DELETE'])
def delete_missao(missao_id):
    # Encontre a missão a ser excluída
    mission_index = next(i for i, missao in enumerate(missoes) if missao['id'] == missao_id)
    
    if mission_index is not None:
        # Retire a missao da lista
        del missoes[mission_index]
        
        return jsonify({'message': 'Missão deletada'}), 200
    else:
        return jsonify({'error': 'Missão não encontrada'}), 404


if __name__ == '__main__':
    app.run(debug=True)

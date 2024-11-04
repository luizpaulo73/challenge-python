from flask import Flask, jsonify, request
import oracledb

app = Flask(__name__)

# Função para obter a conexão com o banco de dados Oracle
def get_connection():
    print("Tentando conectar ao banco de dados...")
    try:
        connection = oracledb.connect('RM555497/240805@oracle.fiap.com.br:1521/orcl')
        print("Conexão com o banco de dados foi estabelecida com sucesso!")
        return connection
    except oracledb.DatabaseError as e:
        error, = e.args
        print("Erro ao conectar ao banco de dados:", error.message)
        raise e

# Função para adicionar um veículo ao banco de dados
def adicionar_veiculo_db(marca, modelo, tipo_transmissao, ano, placa, cpf):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
            INSERT INTO tbl_veiculo_challenge (marca, modelo, tipo_transmissao, ano, placa, cpf)
            VALUES (:marca, :modelo, :tipo_transmissao, :ano, :placa, :cpf)
        ''', {'marca': marca, 'modelo': modelo, 'tipo_transmissao': tipo_transmissao, 'ano': ano, 'placa': placa, 'cpf': cpf})
    connection.commit()
    cursor.close()
    connection.close()

# # Função para listar todos os veículos do banco de dados
# def listar_veiculos_db():

#     return veiculos


# Função para atualizar um veículo no banco de dados
def atualizar_veiculo_db(id_veiculo, marca, modelo, tipo_transmissao, ano, placa, cpf):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute('''
            UPDATE tbl_veiculo_challenge
            SET marca = :marca, modelo = :modelo, tipo_transmissao = :tipo_transmissao,
                ano = :ano, placa = :placa, cpf = :cpf
            WHERE id_veiculo = :id_veiculo
        ''', {'marca': marca, 'modelo': modelo, 'tipo_transmissao': tipo_transmissao, 'ano': ano, 'placa': placa, 'cpf': cpf, 'id_veiculo': id_veiculo})
        connection.commit()
        return cursor.rowcount > 0  # Retorna True se algum registro foi atualizado
    except oracledb.DatabaseError as e:
        error, = e.args
        print("Erro ao atualizar veículo:", error.message)
        raise
    finally:
        cursor.close()
        connection.close()

# Função para deletar um veículo no banco de dados
def deletar_veiculo_db(id_veiculo):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM tbl_veiculo_challenge WHERE id_veiculo = :id_veiculo", {'id_veiculo': id_veiculo})
        connection.commit()
        return cursor.rowcount > 0  # Retorna True se algum registro foi deletado
    except oracledb.DatabaseError as e:
        error, = e.args
        print("Erro ao deletar veículo:", error.message)
        raise
    finally:
        cursor.close()
        connection.close()

# Endpoint para adicionar um veículo
@app.route('/veiculos/<string:cpf>', methods=['POST'])
def adicionar_veiculo(cpf):
    data = request.json
    marca = data.get('marca')
    modelo = data.get('modelo')
    tipo_transmissao = data.get('tipo_transmissao')
    ano = data.get('ano')
    placa = data.get('placa')

    if not all([marca, modelo, tipo_transmissao, ano, placa, cpf]):
        return jsonify({'message': 'Dados incompletos para adicionar o veículo'}), 400

    try:
        adicionar_veiculo_db(marca, modelo, tipo_transmissao, ano, placa, cpf)
        return jsonify({"message": "Veículo adicionado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"message": "Erro ao adicionar veículo: " + str(e)}), 500

# Endpoint para listar todos os veículos
@app.route('/veiculos/<string:cpf>', methods=['GET'])
def listar_veiculos(cpf):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = f"SELECT * FROM tbl_veiculo_challenge WHERE cpf = {cpf}"
        cursor.execute(sql)
        tabela = cursor.fetchall()
        lista = []
        for item in tabela:
            veiculo = {
                "id" : item[0],
                "marca" : item[1],
                "modelo": item[2],
                "tipo_transmissao": item[3],
                "ano": item[4],
                "placa": item[5],
                "cpf": item[6]
            }
            lista.append(veiculo)
        print(lista)
        cursor.close()
        connection.close()
        return jsonify(lista), 200
    except Exception as e:
        return jsonify({"message": "Erro ao listar veículos: " + str(e)}), 500

# Endpoint para atualizar um veículo
@app.route('/veiculos/<string:cpf>/<int:id_veiculo>', methods=['PUT'])
def atualizar_veiculo(cpf, id_veiculo):
    data = request.json
    marca = data.get('marca')
    modelo = data.get('modelo')
    tipo_transmissao = data.get('tipo_transmissao')
    ano = data.get('ano')
    placa = data.get('placa')

    if not all([marca, modelo, tipo_transmissao, ano, placa, cpf]):
        return jsonify({'message': 'Dados incompletos para atualizar o veículo'}), 400

    try:
        atualizado = atualizar_veiculo_db(id_veiculo, marca, modelo, tipo_transmissao, ano, placa, cpf)
        if not atualizado:
            return jsonify({"message": "Veículo não encontrado"}), 404
        return jsonify({"message": "Veículo atualizado com sucesso"}), 200
    except Exception as e:
        return jsonify({"message": "Erro ao atualizar veículo: " + str(e)}), 500

# Endpoint para deletar um veículo
@app.route('/veiculos/<string:cpf>/<int:id_veiculo>', methods=['DELETE'])
def deletar_veiculo(cpf, id_veiculo):
    try:
        deletado = deletar_veiculo_db(id_veiculo)
        if not deletado:
            return jsonify({"message": "Veículo não encontrado"}), 404
        return jsonify({"message": "Veículo deletado com sucesso"}), 200
    except Exception as e:
        return jsonify({"message": "Erro ao deletar veículo: " + str(e)}), 500

# Endpoint de teste para verificar se o Flask está rodando
@app.route('/test', methods=['GET'])
def test_endpoint():
    return jsonify({"message": "Aplicativo Flask está rodando"}), 200

if __name__ == "__main__":
    app.run(debug=True)
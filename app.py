from flask import Flask, jsonify, request
from sudoku import run

app = Flask(__name__)

@app.route('/api/result', methods=['GET'])
def get_result():
    result = {
        'status': 'success',
        'data': 'This is the result'
    }
    return jsonify(result)

@app.route('/api/solve', methods=['POST'])
def submit_data():
    data = request.json
    if(data and data['grid']):
        response = run(data['grid'])
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
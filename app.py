from flask import Flask, jsonify, request, render_template
from block import Blockchain
from storage import save_chain, load_chain

app = Flask(__name__)

blockchain = load_chain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blocks', methods=['GET'])
def get_blocks():
    return jsonify(blockchain.to_dict())

@app.route('/add', methods=['POST'])
def add_block():
    data = request.get_json()
    if not data or 'data' not in data:
        return jsonify({"error": "Missing data"}), 400
    new_block = blockchain.add_block(data['data'])
    save_chain(blockchain)
    return jsonify(new_block.to_dict()), 201

@app.route('/check', methods=['GET'])
def check_integrity():
    valid, message = blockchain.is_valid()
    return jsonify({"valid": valid, "message": message})

if __name__ == '__main__':
    app.run(debug=True)

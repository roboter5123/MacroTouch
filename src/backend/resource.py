from flask import Flask, request, jsonify
from flask_cors import CORS
from keyCombinationService import KeyCombinationService


app = Flask(__name__)
CORS(app)

key_combo_service: KeyCombinationService = KeyCombinationService()

@app.route('/keycombination', methods=['POST'])
def keycombination():
    key_combination_ = request.json["keyCombination"]
    key_combo_service.executekeycombo(key_combination_)

if __name__ == "__main__":
    app.run(debug=True)

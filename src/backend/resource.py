from flask import Flask, request, jsonify
from flask_cors import CORS
import keyCombinationService


app = Flask(__name__)
CORS(app)

key_combo_service:  = KeyCombinationService()

@app.route('/keycombination', methods=['POST'])
def executekeycombination() -> None:
    key_combination = request.json["keyCombination"]
    keyCombinationService.executekeycombo(key_combination)

if __name__ == "__main__":
    app.run(debug=True)

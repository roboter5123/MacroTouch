from flask import Flask, request
from flask_cors import CORS

import keyCombinationService

app = Flask(__name__)
CORS(app)


@app.route('/keycombination', methods=['POST'])
def execute_key_combination() -> None:
    key_combination = request.json["keyCombination"]
    keyCombinationService.execute_key_combination(key_combination)


if __name__ == "__main__":
    app.run(debug=True)

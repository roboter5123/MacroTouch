from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/keycombo', methods=['POST'])
def keycombo():
    print(request.json["keyCombo"])
    print(jsonify(request.json))
    return request.json


if __name__ == "__main__":
    app.run(debug=True)

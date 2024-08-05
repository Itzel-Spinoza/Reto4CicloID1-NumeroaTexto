from flask import Flask, request, jsonify, send_from_directory
from num2words import num2words
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory(os.path.abspath(os.path.dirname(__file__)), 'index.html')

@app.route('/convert', methods=['GET'])
def convert():
    numero = request.args.get('numero')
    if not numero:
        return jsonify({"error": "Por favor, proporciona un número."}), 400

    try:
        numero = int(numero)
    except ValueError:
        return jsonify({"error": "Por favor, proporciona un número válido."}), 400

    palabras = num2words(numero, lang='es')
    return jsonify({"numero": numero, "palabras": palabras})

if __name__ == '__main__':
    app.run(debug=True)

# main.py (modificado)
from flask import Flask, request, jsonify, render_template
from num2words import num2words

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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

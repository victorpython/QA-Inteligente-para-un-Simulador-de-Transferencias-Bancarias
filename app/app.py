from flask import Flask, render_template, request, jsonify
from model_sim import interpretar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    data = request.json
    mensaje = data.get('mensaje', '')
    respuesta = interpretar(mensaje)
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True)
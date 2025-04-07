# Código principal del backend

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Renombrador BLIP funcionando', 200
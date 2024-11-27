from flask import Flask, jsonify
from flask_cors import CORS
from app import create_app, db

app = create_app()
CORS(app)  # Habilitar CORS

# Crear la base de datos si no existe
with app.app_context():
    db.create_all()

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hola desde Flask, React puede consumir este mensaje"})

if __name__ == '__main__':
    app.run(debug=True)

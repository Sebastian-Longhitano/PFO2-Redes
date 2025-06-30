from flask import Flask, request, jsonify, render_template_string
from bd import init_db
from auth import registrar_usuario, verificar_credenciales

app = Flask(__name__)

init_db()

@app.route('/registro', methods=['POST'])
def registro():
    data = request.json
    usuario = data.get("usuario")
    contrasena = data.get("contraseña")
    if not usuario or not contrasena:
        return jsonify({"error": "Datos incompletos"}), 400
    return registrar_usuario(usuario, contrasena)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = data.get("usuario")
    contrasena = data.get("contraseña")
    if not usuario or not contrasena:
        return jsonify({"error": "Datos incompletos"}), 400
    return verificar_credenciales(usuario, contrasena)

@app.route('/tareas', methods=['GET'])
def ver_tareas():
    return render_template_string("<h1>Bienvenido al Gestor de Tareas</h1>")

if __name__ == '__main__':
    app.run(debug=True)

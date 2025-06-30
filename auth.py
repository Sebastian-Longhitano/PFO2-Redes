from werkzeug.security import generate_password_hash, check_password_hash
from bd import get_connection

def registrar_usuario(usuario, contrasena):
    hash_pw = generate_password_hash(contrasena)
    try:
        conn = get_connection()
        conn.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, hash_pw))
        conn.commit()
        conn.close()
        return {"mensaje": "Usuario registrado exitosamente"}, 201
    except Exception as e:
        return {"error": "Usuario ya existe o error en la base de datos"}, 409

def verificar_credenciales(usuario, contrasena):
    conn = get_connection()
    user = conn.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,)).fetchone()
    conn.close()
    if user and check_password_hash(user["contrasena"], contrasena):
        return {"mensaje": "Login exitoso", "usuario_id": user["id"]}, 200
    return {"error": "Credenciales inválidas"}, 401
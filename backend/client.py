from flask import Flask, jsonify
from flask_cors import CORS
import socket
import json

app = Flask(__name__)
CORS(app)

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001

@app.route("/quiz/<game_id>")
def quiz(game_id):
    try:
        # Connect to server.py via socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_HOST, SERVER_PORT))
        s.sendall(game_id.encode())

        data = s.recv(4096).decode()
        s.close()

        return jsonify(json.loads(data))
    except Exception as e:
        return jsonify({"error": f"Failed to fetch from server: {e}"})

if __name__ == "__main__":
    print("[*] Client proxy running at http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000)

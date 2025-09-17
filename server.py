import socket
import json

HOST = "127.0.0.1"
PORT = 7000

# Store multiple quiz datasets
games = {
    "1": {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1. Mars", "2. Venus"],
        "answer": "1"
    },
    "2": {
        "question": "Which is the largest ocean on Earth?",
        "options": ["1. Atlantic Ocean", "2. Pacific Ocean"],
        "answer": "2"
    }
}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print(f"[*] Server running on {HOST}:{PORT}, waiting for requests...")

while True:
    conn, addr = s.accept()
    print("[*] Client connected:", addr)

    # Receive gameID
    game_id = conn.recv(1024).decode().strip()
    print(f"[*] Requested gameID: {game_id}")

    # Fetch data if available
    data = games.get(game_id, {"error": "Invalid gameID"})
    conn.sendall(json.dumps(data).encode())

    conn.close()

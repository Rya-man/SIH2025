import socket
import json

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 7000

LOCAL_HOST = "127.0.0.1"
LOCAL_PORT = 6000

# Local proxy for game.py
local_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_sock.bind((LOCAL_HOST, LOCAL_PORT))
local_sock.listen(5)
print(f"[*] Local proxy running on {LOCAL_HOST}:{LOCAL_PORT}")

while True:
    conn, addr = local_sock.accept()
    print("[*] Game connected:", addr)

    # Receive gameID from game.py
    game_id = conn.recv(1024).decode().strip()
    print(f"[*] Got gameID from game.py: {game_id}")

    # Connect to server and forward gameID
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.connect((SERVER_HOST, SERVER_PORT))
    server_sock.sendall(game_id.encode())

    # Get quiz data from server
    data = server_sock.recv(1024).decode()
    server_sock.close()

    # Send data back to game.py
    conn.sendall(data.encode())
    conn.close()
    print("[*] Sent quiz data to game.py")

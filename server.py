import socket

HOST = "0.0.0.0"   # listen on all interfaces
PORT = 5000        # any free port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print(f"[*] Server listening on {HOST}:{PORT}")
conn, addr = s.accept()
print("[*] Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Client says:", data.decode())
    conn.sendall(b"Hello from Android!")

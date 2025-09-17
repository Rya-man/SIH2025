import socket

HOST = "10.130.40.223"  # your Android hotspot IP (gateway)
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(b"Hello from Laptop!")
print("Server replied:", s.recv(1024).decode())

s.close()

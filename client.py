import socket
""" So now we will be assigning the host ip after a device connects to it, as of now it is static.
    later on we can make it dynamic, in this case the host ip is the ip address of the device suppling the hotspot.
    the connected devices can talk to the host device only
    """
HOST = "10.130.40.223"  # your Android hotspot IP (gateway)
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(b"Hello from Laptop!")
print("Server replied:", s.recv(1024).decode())

s.close()

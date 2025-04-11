import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("127.0.0.1", 13234))
while True:
    msg = input("Tu (cliente): ")
    socket.sendall(str.encode(msg))
    data = socket.recv(1024)

    print(f"Mensagem recebida: {data}")

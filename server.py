import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 13234))
server.listen()
print("[*] Aguardando conexao.")
con, addr = server.accept()
print(f"[*] Cliente conectado em {con}")

while True:
    data = con.recv(1024)
    if not data or data == "sair":
        break
    print(f"Cliente: {data}")
    resposta = input("Tu (servidor): ")
    con.send(str.encode(resposta))






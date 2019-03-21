import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 443
s.bind((host, port))
s.listen(10)  
c, addr = s.accept()
c.sendall(bytes("Merhaba!".encode("utf-8")))
print('{} bağlandı.'.format(addr))
while True:
    data = str(c.recv(1024))[1:]
    if data:
        print("İstemci: {}".format(data))
        respond = input("Sunucu: ").encode("utf-8")
        if respond == b"q":
            exit()
        else:
            c.sendall(bytes(respond))

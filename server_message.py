import socket

socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_conn.bind(('127.0.0.1', 12800))
socket_conn.listen(5)
client_conn, client_addr = socket_conn.accept()
print('Connected by', client_addr)
message_conn_to_client = "La connexion avec le serveur a bien été établie"
bytes_to_send = client_conn.send(message_conn_to_client.encode("utf-8"))
print(bytes_to_send)

message_recv = ""
while message_recv != "close":
	message_recv = client_conn.recv(1024)
	message_recv = message_recv.decode()
	print(message_recv)

client_conn.close()
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.17.1.71', 6666))

data = 'Hello' + '你好'
data = data.encode()
client_socket.send(data)

recv_data = client_socket.recv(1024)
print('未解码::', recv_data)

recv_data = recv_data.decode()
print('解码后::', recv_data)

client_socket.close()

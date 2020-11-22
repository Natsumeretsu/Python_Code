import socket

# 创建套接字对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 目前服务器是一次性的,若马上重启服务器,会出现一个错误,原因是此时地址和端口没有被释放
# 如果想马上释放,需要设置一下socke选项
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 绑定ip和端口
# 为空则默认绑定本机ip地址
server_socket.bind(('', 7777))

# 设置监听,设置为被动,不能主动连接,只能等待客户端去链接服务器
server_socket.listen(128)

# 等待客户端链接
# 链接成功会返回带有 客户端socket的对象 和 客户端地址信息(包含ip地址和端口号)
client_socket, ip_port = server_socket.accept()

print(f'[客户端] {ip_port[0]} 使用端口 {ip_port[1]} 连接成功...')

# 接收客户端的数据
data = client_socket.recv(1024)
if len(data) != 0:
    data = data.decode()
    print(f'[客户端] {ip_port[0]} 发送的数据是\n{data}')
else:
    print(f'[客户端] {ip_port[0]} 关闭了链接...')
# 给客户端发送数据
data = '我是服务端'.encode()
client_socket.send(data)


# 关闭客户端
client_socket.close()
# 关闭服务端
server_socket.close()

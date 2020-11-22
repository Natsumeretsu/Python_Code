'''
返回固定数据的静态web服务器
'''

# 1.导入模块
import socket

# 2.创建socket对象
static_web_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 端口复用
static_web_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定ip和端口
static_web_socket_server.bind(('', 8080))
# 设置监听
static_web_socket_server.listen(128)
# 3.接收请求
while True:
    # 返回两个,前者是客户端的socket对象,后者是ip地址和端口组成的一个元组
    # 这一瞬间就执行了三次握手
    client, ip_port = static_web_socket_server.accept()
    print(f'客户端{ip_port[0]}使用{ip_port[1]}端口链接成功....')
    # 3.1 接受客户端的请求信息
    request_info = client.recv(1024).decode()
    print(request_info)
    # 4.读取资源内容
    with open('static/index.html', 'rb') as file:
        file_centent = file.read()
    # 5.拼接响应报文
    #     a.响应行
    respense_line = 'HTTP/1.1 200 OK\r\n'
    #     b.响应头
    respense_header = 'Server:PSWS1.0\r\n'
    #     c.拼接响应报文
    # 因为响应行和头都是文本,所以要进行编码,响应体的文件内容都是直接使用二进制读取出来的,所以不需要转换
    respense_data =(respense_line+respense_header+'\r\n').encode()+file_centent

    # 6.发送响应报文
    client.send(respense_data)

    # 7.关闭连接
    client.close()

static_web_socket_server.close()

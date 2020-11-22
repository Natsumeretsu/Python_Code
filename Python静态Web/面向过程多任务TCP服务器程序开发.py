import threading
import socket

def client_task(client_socket, ip_port):
    print(ip_port,'链接上来了..')

    # 实现一个循环,可以持续接收客户端的消息
    while True:
        data = client_socket.recv(1024).decode()
        if len(data)!= 0:
            print(f'客户端{ip_port[0]}发来的消息是: {data}')
        else:
            print(f'客户端{ip_port[0]}已断开连接,下次再见..')
            break
        # 服务端回复的消息
        send_data = ('Hello --' + data).encode()
        client_socket.send(send_data)



# 程序入口
if __name__ == '__main__':
    # 创建服务器对象
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 端口复用
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 绑定ip
    server_socket.bind(('',6666))
    # 测试监听
    server_socket.listen(128)
    # 循环接收客户端链接
    while True:
        client_socket , ip_port = server_socket.accept()

        # 下面实现多任务
        t_client = threading.Thread(target=client_task,args=(client_socket,ip_port))
        # 设置守护线程
        t_client.setDaemon(True)
        #启动多任务
        t_client.start()

    # 关闭服务器的链接
    serve_socket.close()
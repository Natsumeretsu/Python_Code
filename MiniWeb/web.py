'''
使用进程实现多任务面向对象返回指定数据的静态web服务器
'''
import socket
import multiprocessing
# from FrameWork import application
from FrameWork_V1利用模板实现首页显示 import application


class MiniWebServer(object):

    def __init__(self, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建一个基于TCP方式的字节流的socket对象
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)  # 端口复用
        self.server.bind(('', port))
        self.server.listen(128)  # 监听,最大等待数128

    def start(self):
        while True:
            client, ip_port = self.server.accept()  # 接收到后返回两个东西
            # 一个是 客户端的socket对象,另一个是 客户端的ip地址和端口号
            print(f'客户端 {ip_port[0]} 使用 {ip_port[1]} 端口连接成功....')

            # 实现多任务
            # 通过多进程实现多任务
            p = multiprocessing.Process(target=self.task, args=(client,))  # 将客户端的socket对象传入了子进程task任务
            p.start()  # 启动子进程
            client.close()  # 将主进程里的client客户端对象结束(本来是主进程执行任务,
            # 但是此时已将client对象传给了子进程,让子进程去执行任务,所以将主进程里的client对象结束即client.close()

        # 因为是死循环,所以执行不到
        self.server.close()

    # 每一个子进程执行任务时都要执行task任务
    def task(self, client):
        # 接受一下客户端发送的数据(请求数据)
        request_data = client.recv(1024).decode()
        # 判断一下接收数据(请求数据)的长度,如果长度为0,直接关闭掉这次请求
        if len(request_data) == 0:
            client.close()

        else:

            # 分割请求报文,拿到请求地址,第二项就是我们要的请求地址
            request_path = request_data.split(' ')[1]
            print('请求地址是:', request_path)

            # 判断是否是 /
            if request_path == '/':
                request_path = '/index.html'

            # 当确定好请求地址后,来通过请求地址的后缀来确定请求的是静态的数据还是动态的数据
            if request_path.endswith('.html'):
                # 处理动态数据

                # 通过 框架里实现的Application函数来得到请求的数据
                # 该函数接收两个参数
                # 参数一是一个字典,用来传入 请求相关的信息,比如:请求地址
                # 参数二是一个函数引用,通过这个引用可以将响应的状态的响应头信息数据返回
                env = {"PATH": request_path}
                # 服务端将客户请求的数据通过框架发送给客户端
                response_body = application(env, self.start_response)
                # 准备拼接响应报文
                response_line = 'HTTP/1.1 %s\r\n' % self.__status
                response_head = ''
                for t in self.__headers:
                    response_head += '%s:%s\r\n' % t
                response_data = (response_line + response_head + '\r\n' + response_body).encode('GBK')
                client.send(response_data)
                client.close()

            else:
                # 处理静态数据

                # 读取文件,但有可能指定的文件不存在
                try:
                    with open('static' + request_path, 'rb') as file:
                        file_content = file.read()

                except Exception as e:
                    # 文件找不到,拼接404的异常报文
                    # 响应行
                    response_line = 'HTTP/1.1 404 NOT FOUND\r\n'
                    # 响应头
                    response_head = 'Server: PSWS1.1\r\n'
                    # 响应体
                    # 因为 error.html 是纯文本,所以可以使用r模式读取
                    with open('templates/error.html', 'r') as f:
                        error_data = f.read()

                    # 拼接响应报文
                    response_data = (response_line + response_head + '\r\n' + error_data).encode()

                    # 发送给客户端
                    client.send(response_data)

                else:
                    # 找到文件后的报文
                    # 响应行
                    response_line = 'HTTP/1.1 200 OK\r\n'
                    # 响应头
                    response_head = 'Server: PSWS1.1\r\n'
                    # 响应体
                    # 因为 error.html 是纯文本,所以可以使用r模式读取
                    with open('static' + request_path, 'rb') as f:
                        response_body = f.read()

                    # 拼接响应报文
                    response_data = (response_line + response_head + '\r\n').encode() + response_body

                    # 发送给客户端
                    client.send(response_data)

                finally:
                    # 关闭客户连接
                    client.close()

    # 定义一个回调函数
    def start_response(self, status, headers):
        # 在这里,可以直接拼接响应报文中的一部分数据,也可以先保存,后拼接
        self.__status = status
        self.__headers = headers


if __name__ == '__main__':
    # 创建一个服务器对象并启动
    MiniWebServer(9999).start()

"""
使用进程实现多任务面向对象返回指定数据的静态web服务器
"""
import socket
import multiprocessing


class StaticWebSever(object):
    def __init__(self, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server.bind(('', port))
        self.server.listen(128)

    def start(self):
        while True:
            client, ip_port = self.server.accept()
            print(f'客户端{ip_port[0]}使用{ip_port[1]}端口链接成功....')

            # 实现多任务
            p = multiprocessing.Process(target=self.task, args=(client,))
            p.start()
        # 因为是死循环,所以执行不到下面这句话
        self.server.close()


    def task(self,client):
        request_data = client.recv(1024).decode()
        # 判断一下接收数据的长度,如果长度为0,直接关闭掉这次请求
        if len(request_data) == 0:
            client.close()
        else:
            # 分割请求报文,拿到请求地址,第二项即为我们要的请求地址
            request_path = request_data.split(' ', maxsplit=2)[1]
            print('请求地址是', request_path)

            # 判断是否是根 /

            if request_path == '/':
                request_path = '/index2.html'
            # 读取文件,当可能指定的文件不存在
            try:
                with open('static' + request_path, 'rb') as file:
                    file_centent = file.read()
            except Exception as e:
                # 文件找不到,拼接404的报文
                # 响应行
                response_line = 'HTTP/1.1 404 Not Found \r\n'
                # 响应头
                response_header = 'Server:PSWS1.1\r\n'
                # 响应体
                # 因为error.html是纯文本,所以可以使用r模式读取
                with open('static/error.html', 'rb') as f:
                    response_body = f.read()
                # 拼接响应报文
                response_body = (response_line + response_header + '\r\n').encode() + response_body

                # 发送给客户端
                client.send(response_body)
            else:

                # 找到文件后的报文
                # 响应行
                response_line = 'HTTP/1.1 200 OK \r\n'
                # 响应头
                response_header = 'Server:PSWS1.1\r\n'
                # 响应体
                # 因为error.html是纯文本,所以可以使用r模式读取
                with open('static' + request_path, 'rb') as f:
                    response_body = f.read()
                # 拼接响应报文
                response_data = (response_line + response_header + '\r\n').encode() + response_body

                # 发送给客户端
                client.send(response_data)
            finally:
                # 关闭客户端链接
                client.close()


if __name__ == '__main__':
    # 创建一个服务器对象并启动
    StaticWebSever(8888).start()

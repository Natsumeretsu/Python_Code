# WSGI 接口方法,应该实现在框架程序中
def application(environ, start_response):
    # 通过传入的字典,将客户端请求的地址拿到
    request_url = environ['PATH']
    # 准备一个响应状态
    status = '200 OK'
    if request_url == '/index.html':
        data = index()
    elif request_url == '/center.html':
        data = center()
    else:
        # 当请求的页面地址不存在时返回的数据
        data = other()
        # 因为没有找到数据,所以改变状态为404
    # 执行回调函数,将响应状态和响应头返回
    start_response(status, [('Server', 'PMiniWebServer1.0'), ('Content-type', 'text/html')])
    # 返回响应数据
    return '<h1>Hello,web!</h1>'


# 首页的数据函数
def index():
    return "<h1>Index Page Run ...</h1>"


# 中心的数据函数
def center():
    return "<h1>Center Page Run ...</h1>"


# 其他的数据函数
def other():
    return "<h1>Page Not Found ...</h1>"

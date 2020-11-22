"""
路由: 通过一个路径,可以去找到一个资源的地址



"""
router_table = {}


# 定义一个用来进行自动维护路由的装饰器,(带参)
def router(url):
    def wrapper(func):
        def inner():
            print('inner - ', func)
            func()

        # 在这里来维护路由表
        router_table[url] = inner
        print(router_table)
        return inner

    return wrapper


@router('index.html')
def index():
    print('首页内容')


@router('center.html')
def center():
    print('个人中心')


@router('mail.html')
def mail():
    print('邮箱页面')


@router('login.html')
def login():
    print('登陆页面')


def error():
    print('访问页面不存在')


# 定义一个路由表字典
# router_table = {'index.html':index, 'center.html': center }

def request_url(url):
    # if url == 'index.html':
    #     index()
    # elif url == 'center.html':
    #     center()
    # else:
    #     error()

    # 先定义一个函数引用,指向错误页面
    func = error

    # 判断 请求的 url 是否在字典里,如果在字典里,那么使用 url 做为key,取出对应的函数引用.
    if url in router_table:
        func = router_table[url]

    # 执行函数
    func()


request_url('index.html')
request_url('center.html')
request_url('mail.html')
request_url('login.html')

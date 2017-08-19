import socket
from concurrent import futures


def blocking_way():
    sock = socket.socket()
    sock.connect(('example.com', 80))
    request = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    return response


def blocking_way_4():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('example.com', 80))
    except IOError:
        pass
    request = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
    data = request.encode('ascii')
    while True:
        try:
            sock.send(data)
            break
        except OSError:
            pass
    response = b''
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass
    return response


# 同步阻塞
def sync_way():
    res = []
    for i in range(10):
        res.append(blocking_way())
    return len(res)


# 多进程
def sync_way_2():
    workers = 10
    with futures.ProcessPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])


# 多线程
def sync_way_3():
    workers = 10
    with futures.ThreadPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])


# 非阻塞
def sync_way_4():
    res = []
    for i in range(10):
        res.append(blocking_way_4())
    return len(res)


# 同步阻塞
# sync_way()

# 多进程
# sync_way_2()

# 多线程
# sync_way_3()

# 非阻塞
# sync_way_4()

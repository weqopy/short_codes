info_struct = {"addr": 10000, "content": ""}


class Server:
    content = ""

    def recv(self, info):
        pass

    def send(self, info):
        pass

    def show(self):
        pass


class InfoServer(Server):
    def recv(self, info):
        self.content = info
        print("recv OK")

    def show(self):
        self.content = self.content if self.content else None
        print("SHOW: {}".format(self.content))


class ServerProxy:
    pass


class InfoServerProxy(ServerProxy):
    server = ""

    def __init__(self, server):
        self.server = server

    def recv(self, info):
        return self.server.recv(info)

    def show(self):
        self.server.show()


class WhiteInfoServerProxy(InfoServerProxy):
    white_list = []

    def recv(self, info):
        try:
            assert type(info) == dict
        except:
            return "info struct is not correct"
        addr = info.get("addr", 0)
        if addr not in self.white_list:
            return "address is not in white list"
        else:
            content = info.get("content", "")
            return self.server.recv(content)

    def add_white(self, addr):
        self.white_list.append(addr)

    def rem_white(self, addr):
        self.white_list.remove(addr)

    def clear_white(self):
        self.white_list = []


if __name__ == "__main__":
    info_struct = dict()
    info_struct["addr"] = 10010
    info_struct["content"] = "Hello world!"
    info_server = InfoServer()
    info_server_proxy = WhiteInfoServerProxy(info_server)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()
    info_server_proxy.add_white(10010)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()

class bol(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return "<b>{}</b>".format(self.func())


class ita(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return "<i>{}</i>".format(self.func())


class der:
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, func):
        def wrapper():
            return "<{tag}>{f}</{tag}>".format(tag=self.tag, f=func())
        return wrapper


class der_2:
    def __init__(self, *args):
        self.args = args

    def __call__(self, func):
        def wrapper():
            n = len(self.args)
            return "{0}{1}{2}".format(('<{}>' * n).format(*self.args), func(), ('</{}>' * n).format(*reversed(self.args)))
        return wrapper


class der_3:
    def __init__(self, *args):
        self.args = args

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            n = len(self.args)
            return "{0}{1}{2}".format(('<{}>' * n).format(*self.args), func(*args, **kwargs), ('</{}>' * n).format(*reversed(self.args)))
        return wrapper


@der('b')
@der('i')
def sayhi():
    return 'hi'


@der_2('b', 'i')
def sayhi_2():
    return 'hi'


@der_3('b', 'i')
def sayhi_3(word='hi'):
    return word


print(sayhi())
print(sayhi_2())
print(sayhi_3())
print(sayhi_3('hello'))

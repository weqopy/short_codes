class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __repr__(self):
        return "Singleton module"


def test_Singleton():
    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(dir(s1))
    print(s1 == s2)
    print(id(s1), id(s2))


if __name__ == "__main__":
    test_Singleton()

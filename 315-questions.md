# 315-questions

[TOC]

## ** 第一部分 Python 基础篇（80 题）**

### 1、为什么学习 Python？

### 2、通过什么途径学习的 Python？

### 3、Python 和 Java、PHP、C、C#、C++ 等其他语言的对比？

### 4、简述解释型和编译型编程语言？

把高级语言翻译成机器语言，计算机才能运行高级语言所编写的程序。
用编译型语言写的程序执行之前，需要一个专门的编译过程，通过编译系统把高级语言翻译成机器语言，把源高级程序编译成为机器语言文件，翻译只做了一次，运行时不需要翻译。
解释型语言编写的程序不需要编译，解释型语言在运行的时候才翻译。

### 5、Python 解释器种类以及特点？

CPython 官方解释器
IPython 基于 CPython，增强交互
PyPy 动态编译，提高速度
JPython Java 平台
IronPython 微软. Net 平台

### 6、位和字节的关系？

一个字节由八个二进制位构成

### 7、b、B、KB、MB、GB 的关系？

1024

### 8、请至少列举 5 个 PEP8 规范（越多越好）。

导入：每行一个导入，标准库、第三方库、应用程序指定导入
缩进：4 个空格
空格：避免不必要处空格，空格应在各种符号后添加
行长度：79 字符，换行可以使用反斜杠，最好使用圆括号。换行点要在操作符的后边敲回车。
空行：类和 top-level 函数定义之间空两行；类中的方法定义之间空一行；函数内逻辑无关段落之间空一行；其他地方尽量不要再空行。

### 9、通过代码实现如下转换：

> 二进制转换成十进制：v = “0b1111011”
> 十进制转换成二进制：v = 18
> 八进制转换成十进制：v = “011”
> 十进制转换成八进制：v = 30
> 十六进制转换成十进制：v = “0x12”
> 十进制转换成十六进制：v = 87


N -> 10: int(v, N)

10 -> 2: bin(v)

10 -> 8: oct(v)

10 -> 16: hex(v)

### 10、请编写一个函数实现将 IP 地址转换成一个整数。

> 如 10.3.9.12 转换规则为：
>
> 10           00001010
>
> 3            00000011
>
> 9            00001001
>
> 12           00001100

再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？

```python
# ip_sr = input('input the ip:')

ip_sr = '10.3.9.12'

def convert(ip):
	list_ip = ip_sr.split('.')
	bin_rt = []
	for i in list_ip:
		bin_i = bin(int(i)).replace('0b', '')
		eight_bin_i = '0' * (8 - len(bin_i)) + bin_i
		bin_rt.append(eight_bin_i)
	return int(''.join(bin_rt), 2)

print(convert(ip_sr))  # 167971084
```

### 11、python 递归的最大层数？

### 12、求结果：

>v1 = 1 or 3 # 1
>
>v2 = 1 and 3 # 3
>
>v3 = 0 and 2 and 1 # 0
>
>v4 = 0 and 2 or 1 # 1
>
>v5 = 0 and 2 or 1 or 4 # 1
>
>v6 = 0 or False and 1 # False

```
全为 and，如果都为真，则返回最后一个变量值；如果为假，则返回第一个假值

全为 or，如果都为假则返回最后一个值；如果为真，则返回第一个真值

（a and b ） or c ：如果 a and b 为真则结果为 b，若 a and b 为假，结果为 c

or 有短路现象，如果为真，后面的不执行
```

### 13、ascii、unicode、utf-8、gbk 区别？

> 1.ANSI 即为 ASCII 编码，为一个字节，只用到 0~127 号字符。
>
> 2.Unicode 编码为万国码，包含几乎世界上的所有字符，一般情况下为两个字节。
>
> 3.GBK 编码为中国特有编码，但也是在 ANSI 基础上演变出来的，包含两个字节，其中中文编码与 Unicode 的中文编码不一样。
>
> 4.UTF-8 为 Unicode 的一种实现编码，Unicode 编码可以通过一定的规则进行转变。

### 14、字节码和机器码的区别？

机器码 ** 是电脑的 CPU 可直接解读的数据 **

字节码（Bytecode）是一种包含执行程序、由一序列 op 代码 / 数据对 组成的 ** 二进制文件 **。** 字节码是一种中间码 **，它比机器码更抽象，需要直译器转译后才能成为机器码的中间代码。

### 15、三元运算规则以及应用场景？

`and` 有假则假，全真则真

`or` 有真则真，全假则假

`not` 非真则假，非假则真

### 16、列举 Python2 和 Python3 的区别？

> 1. print，语句；函数
> 2. `xrange` /`range` ；range
> 3. 2 默认旧式类，3 默认新式类；新式类是采用广度优先搜索，旧式类采用深度优先搜索；新式类对象可以直接通过 `__class__` 属性获取自身类型: type

### 17、用一行代码实现数值交换：

> a = 1
>
> b = 2

```python
a, b = b, a
```

### 18、Python3 和 Python2 中 int 和 long 的区别？

python3 统一为 int，支持高精度整数运算

### 19、xrange 和 range 的区别？

xrange 返回迭代器对象，range 返回列表

### 20、文件操作时：xreadlines 和 readlines 的区别？

readlines 返回列表
xreadlines 返回迭代器

### 21、列举布尔值为 False 的常见值？

0 [] None False ''"" {} ()

### 22、字符串、列表、元组、字典每个常用的 5 个方法？

```python
# string
len(string)
string.format()
string.index(obj)
string.join(sql)
string.replace(str1, str2, num)
string.split(str="", num=string.count(str))
# list
len(list)
list.append('a')
list.pop()
max(list) min(list)
list.index(obj)
list.insert(index, obj)
list.sort()
# tuple
len max min
tuple(seq)
tuple.index(obj)
# dict
len(dict)
dict.get(key, default=None)
dict.has_key(key)
dict.keys()
dict.items()
```



### 23、lambda 表达式格式以及应用场景？

`lambda x: x ** 2`

部分只需快速返回数据处

### 24、pass 的作用？

空语句，一般作占位符用

### 25、*arg 和 **kwarg 作用

不定数量参数，元组、字典

### 26、is 和 == 的区别

is 对比对象 ID

== 对比对象 值

当对象占用空间较小时，is 返回 == 相同值，数字范围 -5:256

### 27、简述 Python 的深浅拷贝以及应用场景？

### 28、Python 垃圾回收机制？

### 29、Python 的可变类型和不可变类型？

可变类型：字典、列表
不可变类型：数字、字符串、元组

### 30、求结果：

```python
v = dict.fromkeys(['k1','k2'],[])
v[‘k1’].append(666)
print(v)  # {'k1': [666], 'k2': [666]}
v[‘k1’] = 777
print(v)  # {'k1': 777, 'k2': [666]}
```

### 31、求结果：

```python
def num():
    return [lambda x: i * x for i in range(4)]
print([m(2) for m in num()])  # [6, 6, 6]
```

[[Python 之 for 循环中的 lambda](https://www.cnblogs.com/liuq/p/6073855.html)]

### 32、列举常见的内置函数？

```
len list tuple split join max min map reduce filter
```

### 33、filter、map、reduce 的作用？

> filter 筛选元素
> map 依次对数组中元素应用函数
> reduce 依次将数组中元素前后应用函数

### 34、一行代码实现 9*9 乘法表

```python
lt = [[f'{x} * {y} =' + str(x * y) for y in range(1, 10)] for x in range(1, 10)]
print(lt)
```

### 35、如何安装第三方模块？以及用过哪些第三方模块？

`pip install ***`
> flask django request beautifulsoup

### 36、至少列举 8 个常用模块都有那些？

> os sys math collections functools request beautifulsoup

### 37、re 的 match 和 search 区别？

> match 从字符串首部匹配，成功返回 Match object，失败返回 None，只匹配一个
> search 在整个字符串中进行匹配，成功返回 Match object, 失败返回 None, 只匹配一个

### 38、什么是正则的贪婪匹配？

> 总是尝试匹配尽可能多的字符。
> 加入 `?` 后为非贪婪匹配。

### 39、求结果： a. [i % 2 for i in range(10) ] b. ( i % 2 for i in range(10) )

`[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]`
`<generator object <genexpr> at 0x105f9abf8>`

### 40、求结果： a. 1 or 2 b. 1 and 2 c. 1 <(2==2) d. 1 < 2 == 2

1
2
False
True

### 41、def func(a,b=[]) 这种写法有什么坑？

b 为可变类型，会产生带入参数的情况。
可改为：
```python
def func(a, b=None):
    if b is None:
        b = []
```

### 42、如何实现 “1,2,3” 变成 [‘1’,’2’,’3’] ?

`[str(x) for x in '1, 2, 3'.split(',')]`

### 43、如何实现 [‘1’,’2’,’3’] 变成[1,2,3] ?

`[int(x) for x in ['1', '2', '3']]`

### 44、比较： a = [1, 2, 3] 和 b = [(1), (2), (3)] 以及 c = [(1, ), (2, ), (3, )] 的区别？

`a == b`
`a != c`
> 单个元素的元组，需要在元素后加逗号，否则圆括号会被识别为数学符号中的‘小括号’，
> 作用于数字本身，仍然等于原数字

### 45、如何用一行代码生成 [1,4,9,16,25,36,49,64,81,100] ?

`[i ** 2 for i in range(1, 11)]`

### 46、一行代码实现删除列表中重复的值 ?

`list(set(seq))`

### 47、如何在函数中设置一个全局变量 ?

> 使用 global 关键字

### 48、logging 模块的作用？以及应用场景？

> 可以进行标准的日志记录。
> 开发过程中的信息反馈记录、错误提示等。
```python
import logging
import logging.handlers
import datetime


logger = logging.getLogger('log_test')
logger.setLevel(logging.DEBUG)


rf_handler = logging.handlers.TimedRotatingFileHandler(
    'all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s'))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
```

### 49、请用代码简答实现 stack 。

### 50、常用字符串格式化哪几种？

```python
% format f
'%s world' %('hello')
'{} world'.format('hello')
h = 'hello'
f'{h} world'
```

### 51、简述 生成器、迭代器、可迭代对象 以及应用场景？

> 迭代器：带状态的对象，在调用`next()`方法时返回容器中的下一个值。任何实现了`__iter__` `__next__`方法的对象都是迭代器。
> 生成器：一种特殊的迭代器，仅需要`yield`关键字
> 可迭代对象：实现了`__iter__`方法，返回一个迭代器对象。

### 52、用 Python 实现一个二分查找的函数。

```python
def func(target, seq):
    start = 0
    end = len(seq)
    while start < end:
        mid = (start + end) // 2
        if target <seq[mid]:
            end = mid
        elif target > seq[mid]:
            start = mid
        else:
            return mid
    return mid
```

### 53、谈谈你对闭包的理解？

> 装饰器的原理

### 54、os 和 sys 模块的作用？

> os 系统中文件及目录
> sys 请求解释器行为的接口

### 55、如何生成一个随机数？

> 使用 random 模块
```python
import random

print(random.randint(1, 10))  # 产生 1 到 10 的一个整数型随机数
print(random.random())  # 产生 0 到 1 之间的随机浮点数
print(random.uniform(1.1, 5.4))  # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
print(random.randrange(1, 100, 2))  # 生成从 1 到 100 的间隔为 2 的随机整数
a = [1, 3, 5, 6, 7]  # 将序列 a 中的元素顺序打乱
random.shuffle(a)
print(a)
```

### 56、如何使用 python 删除一个文件？

```python
# 使用 os.remove()
import os

os.remove('file_name')
```

### 57、谈谈你对面向对象的理解？

> 对象是一个独立个体，可以有相应行为、操作
> 以对象为单位进行目标设计

### 58、Python 面向对象中的继承有什么特点？

> 1：在继承中基类的构造（`__init__`()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
> 2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别在于类中调用普通函数时并不需要带上self参数
> 3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。

### 59、面向对象深度优先和广度优先是什么？

> 深度优先，优先纵向进行，到底部后返回原点开始第二条路径纵向进行
> 广度优先，优先横向进行，一条路径可途径所有节点

### 60、面向对象中 super 的作用？

```python
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
```

> 在 inst 的 MRO 列表上搜索 cls 的下一个类

### 61、是否使用过 functools 中的函数？其作用是什么？

### 62、列举面向对象中带双下划线的特殊方法，如：`__new__`、`__init__`

> `__del__`, `__eq__`, `__get__`, `__set__`

### 63、如何判断是函数还是方法？

> 一个可调用对象是方法和函数，和这个对象无关，仅和这个对象是否与类或实例绑定有关（bound method）。
> 实例方法，在类中未和类绑定，是函数；在实例中，此实例方法与实例绑定，即变成方法。

### 64、静态方法和类方法区别？

> @staticmethod; @classmethod
> 静态方法，无参数要求；类方法第一个参数必须默认传类，一般习惯用 cls
> 函数；方法

### 65、列举面向对象中的特殊成员以及应用场景

> `__doc__` 表示类的描述信息
> `__module__` 表示操作对象所在模块
> `__class__` 表示操作对象所属的类
> `__init__` 构造方法，通过类创建对象时自动运行
> `__del__` 析构方法，当对象在内存中被释放时自动触发
> `__call__` 对象后面加括号，触发执行。 # 构造方法的执行是由创建对象触发的，即：对象 = 类名() ；而对于 `__call__` 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
> `__dict__` 类或对象中的所有成员
> `__str__` 如果一个类中定义了`__str__`方法，那么在打印 对象 时，默认输出该方法的返回值。
> `__getitem__`、`__setitem__`、`__delitem__` 用于索引操作，如字典。以上分别表示获取、设置、删除数据
> `__getslice__`、`__setslice__`、`__delslice__` 该三个方法用于分片操作，如：列表
> `__iter__` 用于迭代器，之所以列表、字典、元组可以进行for循环，是因为类型内部定义了 `__iter__`
> `__new__` 和 `__metaclass__` 元类，类的创建

### 66、1、2、3、4、5 能组成多少个互不相同且无重复的三位数

> 5 ** 3
> 125

### 67、什么是反射？以及应用场景？

> 反射就是通过字符串的形式，导入模块；通过字符串的形式，去模块寻找指定函数，并执行。利用字符串的形式去对象（模块）中操作（查找/获取/删除/添加）成员，一种基于字符串的事件驱动。

### 68、metaclass 作用？以及应用场景？

> 创建类。
> 主要用途是创建 API

> 为什么要使用 metaclass 类而不是函数？
> 1.意图更加清晰
> 2.可以使用 OOP 编程
> 3.可以更好地组织代码
> 4.可以使用`__new__`, `__init__`, `__call__`等特殊方法

### 69、用尽量多的方法实现单例模式。

1. 使用模块。将相关函数和数据定义在一个模块中，就可以获得一个单例对象。
2. 使用特殊方法`__new__`。
```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Myclass(Singleton):
    a = 1


one = Myclass()
two = Myclass()

print(one == two, one is two, id(one), id(two))
```
3. 装饰器
```python
from functools import wraps


def singleton(cls):
    instance = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getinstance


@singleton
class MyClass:
    a = 1
```
4. 元类
```python
class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class MyClass(metaclass=Singleton):
    pass

```

### 70、装饰器的写法以及应用场景。

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```

> 应用场景
> 1. 注入参数（提供默认参数，生成参数）
> 2. 记录函数行为（日志、缓存、计时等）
> 3. 预处理／后处理（配置上下文等）
> 4. 修改调用时的上下文（线程异步或者并行，类方法）

### 71、异常处理写法以及如何主动跑出异常（应用场景）

### 72、什么是面向对象的 mro

### 73、isinstance 作用以及应用场景？

### 74、写代码并实现：

> Given an array of integers, return indices of the two numbers such that they add up to a specific target.You may assume that each input would have exactly one solution, and you may not use the same element twice.
>
> Example:
>
>          Given nums = [2, 7, 11, 15], target = 9,
>
> Because nums[0] + nums[1] = 2 + 7 = 9,
>
>           return [0, 1]

```python
class Solution:
    def twoSum(self, target, nums):
        tmp_dict = {}
        for i in range(len(nums)):
            if nums[i] not in tmp_dict:
                tmp_dict[target - nums[i]] = i
            else:
                return [tmp_dict[nums[i]], i]
        return None
```

### 75、json 序列化时，可以处理的数据类型有哪些？如何定制支持 datetime 类型？

> 序列化，把变量从内存中变成可存储或传输的过程

```json
dict: object,
list, tuple: array,
str: string,
int, float: number,
True: true,
False: false,
None: null
```

```python
# 定制类以支持 json 序列化 datetime 类型
import json
from datetime import datetime


class Custom_Datetime(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def main():
    now = datetime.now()
    print(json.dumps({'now': now}, cls=Custom_Datetime))


if __name__ == '__main__':
    main()

```

### 76、json 序列化时，默认遇到中文会转换成 unicode，如果想要保留中文怎么办？

### 77、什么是断言？应用场景？

### 78、有用过 with statement 吗？它的好处是什么？

### 79、使用代码实现查看列举目录下的所有文件。

### 80、简述 yield 和 yield from 关键字。

## ** 第二部分 网络编程和并发（34 题）**


### 1、简述 OSI 七层协议。

### 2、什么是 C/S 和 B/S 架构？

### 3、简述 三次握手、四次挥手的流程。

### 4、什么是 arp 协议？

### 5、TCP 和 UDP 的区别？

### 6、什么是局域网和广域网？

### 7、为何基于 tcp 协议的通信比基于 udp 协议的通信更可靠？

### 8、什么是 socket？简述基于 tcp 协议的套接字通信流程。

### 9、什么是粘包？ socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？

### 10、IO 多路复用的作用？

### 11、什么是防火墙以及作用？

### 12、select、poll、epoll 模型的区别？

### 13、简述 进程、线程、协程的区别 以及应用场景？

### 14、GIL 锁是什么鬼？

### 15、Python 中如何使用线程池和进程池？

### 16、threading.local 的作用？

### 17、进程之间如何进行通信？

### 18、什么是并发和并行？

### 19、进程锁和线程锁的作用？

### 20、解释什么是异步非阻塞？

### 21、路由器和交换机的区别？

### 22、什么是域名解析？

### 23、如何修改本地 hosts 文件？

### 24、生产者消费者模型应用场景及优势？

### 25、什么是 cdn？

### 26、LVS 是什么及作用？

### 27、Nginx 是什么及作用？

### 28、keepalived 是什么及作用?

### 29、haproxy 是什么以及作用？

### 30、什么是负载均衡？

### 31、什么是 rpc 及应用场景？

### 32、简述 asynio 模块的作用和应用场景。

### 33、简述 gevent 模块的作用和应用场景。

### 34、twisted 框架的使用和应用？

## ** 第三部分 数据库和缓存（46 题）**


### 1、列举常见的关系型数据库和非关系型都有那些？

### 2、MySQL 常见数据库引擎及比较？

### 3、简述数据三大范式？

### 4、什么是事务？MySQL 如何支持事务？

### 5、简述数据库设计中一对多和多对多的应用场景？

### 6、如何基于数据库实现商城商品计数器？

### 7、常见 SQL（必备）

> 详见武沛齐博客：https://www.cnblogs.com/wupeiqi/articles/5729934.html


### 8、简述触发器、函数、视图、存储过程？

### 9、MySQL 索引种类

### 10、索引在什么情况下遵循最左前缀的规则？

### 11、主键和外键的区别？

### 12、MySQL 常见的函数？

### 13、列举 创建索引但是无法命中索引的 8 种情况。

### 14、如何开启慢日志查询？

### 15、数据库导入导出命令（结构 + 数据）？

### 16、数据库优化方案？

### 17、char 和 varchar 的区别？

### 18、简述 MySQL 的执行计划？

### 19、在对 name 做了唯一索引前提下，简述以下区别：

```sql
select * from tb wherename = ‘Oldboy-Wupeiqi’
select * from tb wherename = ‘Oldboy-Wupeiqi’ limit1
```

### 20、1000w 条数据，使用 limit offset 分页时，为什么越往后翻越慢？如何解决？

### 21、什么是索引合并？

### 22、什么是覆盖索引？

### 23、简述数据库读写分离？

### 24、简述数据库分库分表？（水平、垂直）

### 25、redis 和 memcached 比较？

### 26、redis 中数据库默认是多少个 db 及作用？

### 27、python 操作 redis 的模块？

### 28、如果 redis 中的某个列表中的数据量非常大，如果实现循环显示每一个值？

### 29、redis 如何实现主从复制？以及数据同步机制？

### 30、redis 中的 sentinel 的作用？

### 31、如何实现 redis 集群？

### 32、redis 中默认有多少个哈希槽？

### 33、简述 redis 的有哪几种持久化策略及比较？

### 34、列举 redis 支持的过期策略。

### 35、MySQL 里有 2000w 数据，redis 中只存 20w 的数据，如何保证 redis 中都是热点数据？

### 36、写代码，基于 redis 的列表实现 先进先出、后进先出队列、优先级队列。

### 37、如何基于 redis 实现消息队列？

### 38、如何基于 redis 实现发布和订阅？以及发布订阅和消息队列的区别？

### 39、什么是 codis 及作用？

### 40、什么是 twemproxy 及作用？

### 41、写代码实现 redis 事务操作。

### 42、redis 中的 watch 的命令的作用？

### 43、基于 redis 如何实现商城商品数量计数器？

### 44、简述 redis 分布式锁和 redlock 的实现机制。

### 45、什么是一致性哈希？Python 中是否有相应模块？



### 46、如何高效的找到 redis 中所有以 oldboy 开头的 key？


## ** 第四部分 前端、框架和其他（155 题）**


### 1、谈谈你对 http 协议的认识。

### 2、谈谈你对 websocket 协议的认识。

### 3、什么是 magic string ？

### 4、如何创建响应式布局？

### 5、你曾经使用过哪些前端框架？

### 6、什么是 ajax 请求？并使用 jQuery 和 XMLHttpRequest 对象实现一个 ajax 请求。

### 7、如何在前端实现轮训？

### 8、如何在前端实现长轮训？

### 9、vuex 的作用？

### 10、vue 中的路由的拦截器的作用？

### 11、axios 的作用？

### 12、列举 vue 的常见指令。

### 13、简述 jsonp 及实现原理？

### 14、是什么 cors ？

### 15、列举 Http 请求中常见的请求方式？

### 16、列举 Http 请求中的状态码？

### 17、列举 Http 请求中常见的请求头？

### 24、django、flask、tornado 框架的比较？

### 25、什么是 wsgi？

### 26、django 请求的生命周期？

### 27、列举 django 的内置组件？

### 28、列举 django 中间件的 5 个方法？以及 django 中间件的应用场景？

### 29、简述什么是 FBV 和 CBV？

### 30、django 的 request 对象是在什么时候创建的？

### 31、如何给 CBV 的程序添加装饰器？

### 32、列举 django orm 中所有的方法（QuerySet 对象的所有方法）

### 33、only 和 defer 的区别？

### 34、select_related 和 prefetch_related 的区别？

### 35、filter 和 exclude 的区别？

### 36、列举 django orm 中三种能写 sql 语句的方法。

### 37、django orm 中如何设置读写分离？

### 38、F 和 Q 的作用?

### 39、values 和 values_list 的区别？

### 40、如何使用 django orm 批量创建数据？

### 41、django 的 Form 和 ModeForm 的作用？

### 42、django 的 Form 组件中，如果字段中包含 choices 参数，请使用两种方式实现数据源实时更新。

### 43、django 的 Model 中的 ForeignKey 字段中的 on_delete 参数有什么作用？

### 44、django 中 csrf 的实现机制？

### 45、django 如何实现 websocket？

### 46、基于 django 使用 ajax 发送 post 请求时，都可以使用哪种方法携带 csrf token？

### 47、django 中如何实现 orm 表中添加数据时创建一条日志记录。

### 48、django 缓存如何设置？

### 49、django 的缓存能使用 redis 吗？如果可以的话，如何配置？

### 50、django 路由系统中 name 的作用？

### 51、django 的模板中 filter 和 simple_tag 的区别？

### 52、django-debug-toolbar 的作用？

### 53、django 中如何实现单元测试？

### 54、解释 orm 中 db first 和 code first 的含义？

### 55、django 中如何根据数据库表生成 model 中的类？

### 56、使用 orm 和原生 sql 的优缺点？

### 57、简述 MVC 和 MTV

### 58、django 的 contenttype 组件的作用？

### 59、谈谈你对 restfull 规范的认识？

### 60、接口的幂等性是什么意思？

### 61、什么是 RPC？

### 62、Http 和 Https 的区别？

### 63、为什么要使用 django rest framework 框架？

### 64、django rest framework 框架中都有那些组件？

### 65、django rest framework 框架中的视图都可以继承哪些类？

### 66、简述 django rest framework 框架的认证流程。

### 67、django rest framework 如何实现的用户访问频率控制？

### 68、Flask 框架的优势？

### 69、Flask 框架依赖组件？

### 70、Flask 蓝图的作用？

### 71、列举使用过的 Flask 第三方组件？

### 72、简述 Flask 上下文管理流程?

### 73、Flask 中的 g 的作用？

### 74、Flask 中上下文管理主要涉及到了那些相关的类？并描述类主要作用？

### 75、为什么要 Flask 把 Local 对象中的的值 stack 维护成一个列表？

### 76、Flask 中多 app 应用是怎么完成？

### 77、在 Flask 中实现 WebSocket 需要什么组件？

### 78、wtforms 组件的作用？

### 79、Flask 框架默认 session 处理机制？

### 80、解释 Flask 框架中的 Local 对象和 threading.local 对象的区别？

### 81、Flask 中 blinker 是什么？

### 82、SQLAlchemy 中的 session 和 scoped_session 的区别？

### 83、SQLAlchemy 如何执行原生 SQL？

### 84、ORM 的实现原理？

### 85、DBUtils 模块的作用？

### 86、以下 SQLAlchemy 的字段是否正确？如果不正确请更正：

```sql
from datetime import datetime
from sqlalchemy.ext.declarative
import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
Base = declarative_base()
classUserInfo(Base):
__tablename__ = 'userinfo'
id = Column(Integer, primary_key=True, autoincrement=True)
name = Column(String(64), unique=True)
ctime = Column(DateTime, default=datetime.now())
```

### 87、SQLAchemy 中如何为表设置引擎和字符编码？

### 88、SQLAchemy 中如何设置联合唯一索引？

### 89、简述 Tornado 框架的特点。

### 90、简述 Tornado 框架中 Future 对象的作用？

### 91、Tornado 框架中如何编写 WebSocket 程序？

### 92、Tornado 中静态文件是如何处理的？如： <link href="{{static_url("commons.css")}}" rel="stylesheet" />

### 93、Tornado 操作 MySQL 使用的模块？

### 94、Tornado 操作 redis 使用的模块？

### 95、简述 Tornado 框架的适用场景？

### 96、git 常见命令作用：

### 97、简述以下 git 中 stash 命令作用以及相关其他命令。

### 98、git 中 merge 和 rebase 命令 的区别。

### 99、公司如何基于 git 做的协同开发？

### 100、如何基于 git 实现代码 review？

### 101、git 如何实现 v1.0 、v2.0 等版本的管理？

### 102、什么是 gitlab？

### 103、github 和 gitlab 的区别？

### 104、如何为 github 上牛逼的开源项目贡献代码？

### 105、git 中 .gitignore 文件的作用?

### 106、什么是敏捷开发？

### 107、简述 jenkins 工具的作用?

### 108、公司如何实现代码发布？

### 109、简述 RabbitMQ、Kafka、ZeroMQ 的区别？

### 110、RabbitMQ 如何在消费者获取任务后未处理完前就挂掉时，保证数据不丢失？

### 111、RabbitMQ 如何对消息做持久化？

### 112、RabbitMQ 如何控制消息被消费的顺序？

### 113、以下 RabbitMQ 的 exchange type 分别代表什么意思？如：fanout、direct、topic。

### 114、简述 celery 是什么以及应用场景？

### 115、简述 celery 运行机制。

### 116、celery 如何实现定时任务？

### 117、简述 celery 多任务结构目录？

### 118、celery 中装饰器 @app.task 和 @shared_task 的区别？

### 119、简述 requests 模块的作用及基本使用？

### 120、简述 beautifulsoup 模块的作用及基本使用？

### 121、简述 seleninu 模块的作用及基本使用?

### 122、scrapy 框架中各组件的工作流程？

### 123、在 scrapy 框架中如何设置代理（两种方法）？

### 124、scrapy 框架中如何实现大文件的下载？

### 125、scrapy 中如何实现限速？

### 126、scrapy 中如何实现暂定爬虫？

### 127、scrapy 中如何进行自定制命令？

### 128、scrapy 中如何实现的记录爬虫的深度？

### 129、scrapy 中的 pipelines 工作原理？

### 130、scrapy 的 pipelines 如何丢弃一个 item 对象？

### 131、简述 scrapy 中爬虫中间件和下载中间件的作用？

### 132、scrapy-redis 组件的作用？

### 133、scrapy-redis 组件中如何实现的任务的去重？

### 134、scrapy-redis 的调度器如何实现任务的深度优先和广度优先？

### 135、简述 vitualenv 及应用场景?

### 136、简述 pipreqs 及应用场景？

### 137、在 Python 中使用过什么代码检查工具？

### 138、简述 saltstack、ansible、fabric、puppet 工具的作用？

### 139、B Tree 和 B+ Tree 的区别？

### 140、请列举常见排序并通过代码实现任意三种。

### 141、请列举常见查找并通过代码实现任意三种。

### 142、请列举你熟悉的设计模式？

### 143、有没有刷过 leetcode？

### 144、列举熟悉的的 Linux 命令。

### 145、公司线上服务器是什么系统？

### 146、解释 PV、UV 的含义？

### 147、解释 QPS 的含义？

### 148、uwsgi 和 wsgi 的区别？

### 149、supervisor 的作用？

### 150、什么是反向代理？

### 151、简述 SSH 的整个过程。

### 152、有问题都去那些找解决方案？

### 153、是否有关注什么技术类的公众号？

### 154、最近在研究什么新技术？

### 155、是否了解过领域驱动模型？

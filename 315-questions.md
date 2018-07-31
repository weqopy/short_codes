# 315-questions

[TOC]

## 第一部分 Python 基础篇（80 题）

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

导入：每行一个导入，标准库、第三方库、应用、程序指定导入

缩进：4 个空格

空格：避免不必要处空格，空格应在各种符号后添加

行长度：79 字符，换行可以使用反斜杠，最好使用圆括号。换行点要在操作符的后边敲回车。

空行：类和 top - level 函数定义之间空两行；类中的方法定义之间空一行；函数内逻辑无关段落之间空一行；其他地方尽量不要再空行。

### 9、通过代码实现如下转换：

> 二进制转换成十进制：v = “0b1111011”
>
> 十进制转换成二进制：v = 18
>
> 八进制转换成十进制：v = “011”
>
> 十进制转换成八进制：v = 30
>
> 十六进制转换成十进制：v = “0x12”
>
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
### ip_sr = input('input the ip:')

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

>v1 = 1 or 3  # 1
>
>v2 = 1 and 3  # 3
>
>v3 = 0 and 2 and 1  # 0
>
>v4 = 0 and 2 or 1  # 1
>
>v5 = 0 and 2 or 1 or 4  # 1
>
>v6 = 0 or False and 1  # False

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
> 4.UTF - 8 为 Unicode 的一种实现编码，Unicode 编码可以通过一定的规则进行转变。

### 14、字节码和机器码的区别？

机器码 ** 是电脑的 CPU 可直接解读的数据 **

字节码（Bytecode）是一种包含执行程序、由一序列 op 代码 / 数据对 组成的 ** 二进制文件 **。** 字节码是一种中间码 **，它比机器码更抽象，需要直译器转译后才能成为机器码的中间代码。

### 15、三元运算规则以及应用场景？

`and` 有假则假，全真则真

`or` 有真则真，全假则假

`not` 非真则假，非假则真

### 16、列举 Python2 和 Python3 的区别？

> 1. print，语句；函数
> 2. `xrange` / `range` ；range
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

0 [] None False ''"" {}()

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

当对象占用空间较小时，is 返回 == 相同值，数字范围 -5: 256

### 27、简述 Python 的深浅拷贝以及应用场景？

### 28、Python 垃圾回收机制？

### 29、Python 的可变类型和不可变类型？

可变类型：字典、列表
不可变类型：数字、字符串、元组

### 30、求结果：

```python
v = dict.fromkeys(['k1', 'k2'], [])
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

[[Python 之 for 循环中的 lambda](https: // www.cnblogs.com / liuq / p / 6073855.html)]

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

`pip install ** *`
> flask django request beautifulsoup

### 36、至少列举 8 个常用模块都有那些？

> os sys math collections functools request beautifulsoup

### 37、re 的 match 和 search 区别？

> match 从字符串首部匹配，成功返回 Match object，失败返回 None，只匹配一个
>
> search 在整个字符串中进行匹配，成功返回 Match object, 失败返回 None, 只匹配一个

### 38、什么是正则的贪婪匹配？

> 总是尝试匹配尽可能多的字符。
>
> 加入 `?` 后为非贪婪匹配。

### 39、求结果： a. [i % 2 for i in range(10) ] b. ( i % 2 for i in range(10) )

`[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]`
` <generator object < genexpr> at 0x105f9abf8 > `

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

### 43、如何实现 [‘1’,’2’,’3’] 变成 [1,2,3] ?

`[int(x) for x in ['1', '2', '3']]`

### 44、比较： a = [1, 2, 3] 和 b = [(1), (2), (3)] 以及 c = [(1, ), (2, ), (3, )] 的区别？

`a == b`
`a != c`
> 单个元素的元组，需要在元素后加逗号，否则圆括号会被识别为数学符号中的‘小括号’，
>
> 作用于数字本身，仍然等于原数字

### 45、如何用一行代码生成 [1,4,9,16,25,36,49,64,81,100] ?

`[i ** 2 for i in range(1, 11)]`

### 46、一行代码实现删除列表中重复的值 ?

`list(set(seq))`

### 47、如何在函数中设置一个全局变量 ?

> 使用 global 关键字

### 48、logging 模块的作用？以及应用场景？

> 可以进行标准的日志记录。
>
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

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            raise LookupError('stack is empty!')

    def is_empty(self):
        return bool(self.stack)

    def top(self):
        return self.stack[-1]
```

### 50、常用字符串格式化哪几种？

```python
% format f
'%s world' % ('hello')
'{} world'.format('hello')
h = 'hello'
f'{h} world'
```

### 51、简述 生成器、迭代器、可迭代对象 以及应用场景？

> 迭代器：带状态的对象，在调用 `next()` 方法时返回容器中的下一个值。任何实现了 `__iter__` `__next__` 方法的对象都是迭代器。
>
> 生成器：一种特殊的迭代器，仅需要 `yield` 关键字
>
> 可迭代对象：实现了 `__iter__` 方法，返回一个迭代器对象。

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
>
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
### 使用 os.remove()
import os

os.remove('file_name')
```

### 57、谈谈你对面向对象的理解？

> 对象是一个独立个体，可以有相应行为、操作
>
> 以对象为单位进行目标设计

### 58、Python 面向对象中的继承有什么特点？

> 1：在继承中基类的构造（`__init__`() 方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
>
> 2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
>
> 3：Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。

### 59、面向对象深度优先和广度优先是什么？

> 深度优先，优先纵向进行，到底部后返回原点开始第二条路径纵向进行
>
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
>
> 实例方法，在类中未和类绑定，是函数；在实例中，此实例方法与实例绑定，即变成方法。

### 64、静态方法和类方法区别？

> @staticmethod; @classmethod
>
> 静态方法，无参数要求；类方法第一个参数必须默认传类，一般习惯用 cls
> 函数；方法

### 65、列举面向对象中的特殊成员以及应用场景

> `__doc__` 表示类的描述信息
>
> `__module__` 表示操作对象所在模块
>
> `__class__` 表示操作对象所属的类
>
> `__init__` 构造方法，通过类创建对象时自动运行
>
> `__del__` 析构方法，当对象在内存中被释放时自动触发
>
>构造方法的执行是由创建对象触发的，即：对象 = 类名 () ；而对于 `__call__` 方法的执行是由对象后加括号触发的，即：对象 () 或者 类 ()()
>
> `__call__` 对象后面加括号，触发执行。
>
> `__dict__` 类或对象中的所有成员
>
> `__str__` 如果一个类中定义了 `__str__` 方法，那么在打印 对象 时，默认输出该方法的返回值。
>
> `__getitem__`、`__setitem__`、`__delitem__` 用于索引操作，如字典。以上分别表示获取、设置、删除数据
>
> `__getslice__`、`__setslice__`、`__delslice__` 该三个方法用于分片操作，如：列表
>
> `__iter__` 用于迭代器，之所以列表、字典、元组可以进行 for 循环，是因为类型内部定义了 `__iter__`
>
> `__new__` 和 `__metaclass__` 元类，类的创建

### 66、1、2、3、4、5 能组成多少个互不相同且无重复的三位数

> 5 ** 3
>
> 125

### 67、什么是反射？以及应用场景？

> 反射就是通过字符串的形式，导入模块；通过字符串的形式，去模块寻找指定函数，并执行。利用字符串的形式去对象（模块）中操作（查找 / 获取 / 删除 / 添加）成员，一种基于字符串的事件驱动。

### 68、metaclass 作用？以及应用场景？

> 创建类。
>
> 主要用途是创建 API

> 为什么要使用 metaclass 类而不是函数？
> 1. 意图更加清晰
> 2. 可以使用 OOP 编程
> 3. 可以更好地组织代码
> 4. 可以使用 `__new__`, `__init__`, `__call__` 等特殊方法

### 69、用尽量多的方法实现单例模式。

1. 使用模块。将相关函数和数据定义在一个模块中，就可以获得一个单例对象。
2. 使用特殊方法 `__new__`。
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

> Python 支持面向对象编程，支持多重继承
>
> 在方法调用时需要对当前类及基类搜索，以确定方法所在的位置
>
> 搜索顺序，即是‘方法解析顺序’（*Method Resolution Order*, MRO）
>
> Python2.3 之后采用一种称为 **C3** 的方式计算 *MRO*

```
      <- B <- D <-
O <- A            F
      <- C <- E <-
mro(A) = [A,O]
mro(B) = [B,A,O]
mro(C) = [C,A,O]
mro(D) = [D,B,A,O]
mro(E) = [E,C,A,O]
mro(F) = [F] + merge( mro(D) , mro(E) , [D,E] )

使用下面的规则来化简上面类 F 的 mro：
1. 在 merge 列表中，如果第一个 mro 的第一个类出现在其它序列，并且也是第一个，或者不在其它序列中出现，那么这个类就会从这些序列中删除，合并到访问顺序列表中.
2. 若第一个 mro 无法继续找到符合规则 1 的类，则从下一个 mro 中继续按照规则 1 搜索.
3. 重复直到列表为空或者无法输出，若列表为空则此时访问顺序列表生成完毕；否则，说明无法构建继承关系.

mro(F) = [F] + merge( [D,B,A,O] , [E,C,A,O] , [D,E] )
       = [F,D] + merge( [B,A,O] , [E,C,A,O] , [E] )
       = [F,D,B] + merge( [A,O] , [E,C,A,O] , [E] )
       = ....
       = [F,D,B,E,C,A,O]
```

### 73、isinstance 作用以及应用场景？

> 判断对象是否是已知类型

### 74、写代码并实现：

> Given an array of integers, return indices of the two numbers such that they add up to a specific target.You may assume that each input would have exactly one solution, and you may not use the same element twice.
>
> Example:
>
>          Given nums = [2, 7, 11, 15], target = 9,
>
> Because nums[0] + nums[1] = 2 + 7 = 9,
>
> return [0, 1]

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
# json.dumps 将 Python 数据结构转换为 JSON， json.loads 将一个 JSON 编码的字符串转换回一个 Python 数据结构
# 如果要处理的是文件而不是字符串，可以使用 json.dump() 和 json.load() 来编码和解码 JSON 数据。
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

> 使用参数 `ensure_ascii=False`

### 77、什么是断言？应用场景？

> 检查一个条件，如为真则继续；如为假则抛出 AssertError 并且包含错误信息

*使用场景*
- 防御型的编程
- 运行时检查程序逻辑
- 检查约定
- 程序常量
- 检查文档
- 测试代码

### 78、有用过 with statement 吗？它的好处是什么？

> 处理文件时使用
>
> 文件调用结束后自动关闭，

### 79、使用代码实现查看列举目录下的所有文件。

```python
import pathlib

cwd = pathlib.Path.cwd()
all_files = pathlib.Path.iterdir(cwd)

for i in all_files:
    print(i)
```

### 80、简述 yield 和 yield from 关键字。

> `yield` 是定义生成器的一种方式，包含 `yield` 语句的函数就是一个生成器对象
>
> 调用一个生成器函数，返回的是一个迭代器对象，迭代器控制生成器的执行，当函数运行到第一个 `yield` 语句时暂停，将 `yield` 表达式后的值返回给调用者；当生成器函数被再次调用时，直接从上次暂停的 `yield` 表达式处继续运行。
>
> 函数重新运行时， `yield` 会先接收一个值作为结果，然后继续运行。如果调用者使用 `next` 函数或者 `__next__()` 方法，则默认返回给 `yield` 表达式 `None` 值；使用 `send()` 方法则传递一个值作为 `yield` 表达式的结果。

```python
def wine():
    print('first yield...')
    # 直接 yield 返回值
    yield 1
    print('second yield...')
    yield 2

ww = wine()
print(next(ww))

# ** 输出：**
first yield...
1

print(next(ww))

# ** 输出：**
second yield...
2


def wine():
    print('first yield...')
    x = yield 1
    print(x)
    print('second yield...')
    yield 2

ww = wine()
print(next(ww))

# ** 输出：**
first yield...
1

print(ww.send('the result of first yield...'))

# ** 输出：**
the result of first yield...
second yield...
2
```

## 第二部分 网络编程和并发（34 题）

### 1、简述 OSI 七层协议。

![OSI](https://ws3.sinaimg.cn/large/006tNc79ly1ftbzur75xwg30v4183431.gif)

### 2、什么是 C/S 和 B/S 架构？

C/S：客户端/服务端，重客户端
- 客户端优点：直接连接，更加快速、安全；可以处理逻辑事务；操作界面，方便、个性化
- 客户端缺点：客户端，功能单一、网速要求高、部署困难、需按系统分别开发
- 服务端：对服务器要求高
- 用户：必须通过客户端访问
- 成本：专业、费用高
- 后期：维护、升级需要持续跟进；业务变更或扩展时，客户端需要调整

B/S：浏览器/服务端，重服务端
- 浏览器-Web 服务器-数据库服务器
- 浏览器：适用范围广、负担小、更新可以同步、开发简单、扩展方便、与平台、系统无关
- 服务器：数据集中存放，安全、一致；可远程操作；服务器负载增加时可以平滑升级
- 用户：网速要求小；适用对象广大
- 成本：重用性强，开发简单，成本小
- 缺点：页面通用化，页面需动态加载，用户多、网速慢时较耗时
- 用户数量大时，服务器响应慢；功能较轻；服务器的数据负荷重要。

### 3、简述三次握手、四次挥手的流程。

三次握手：
- 客户端向服务器发送信号
- 服务器收到信号，并向客户端发送信号
- 客户端确认收到信号，开始数据传输

### 4、什么是 arp 协议？

ARP (Address Resolution Protocol) ，地址解析协议。是根据 IP 地址获取物理地址（MAC）的一个 TCP/IP 协议.

### 5、TCP 和 UDP 的区别？

1. 基于连接与无连接； 
2. 对系统资源的要求（TCP较多，UDP少）； 
3. UDP程序结构较简单； 
4. 流模式与数据包模式 ；
5. TCP保证数据正确性，UDP可能丢包，TCP保证数据顺序，UDP不保证。

### 6、什么是局域网和广域网？

广域网（WAN），就是我们通常所说的Internet，它是一个遍及全世界的网络。

局域网（LAN），相对于广域网（WAN）而言，主要是指在小范围内的计算机互联网络。这个“小范围”可以是一个家庭，一所学校，一家公司，或者是一个政府部门。 BT中常常提到的公网、外网，即广域网（WAN）；BT中常常提到私网、内网，即局域网（LAN）。

### 7、为何基于 tcp 协议的通信比基于 udp 协议的通信更可靠？

1. TCP（Transmission Control Protocol，传输控制协议）是面向连接的协议，也就是说，在收发数据前，必须和对方建立可靠的连接。一个TCP连接必须要经过三次“对话”才能建立起来。
2. TCP有专门的序列号SN字段，可提供数据re-order
3. 窗口和计时器的使用。TCP窗口中会指明双方能够发送接收的最大数据量
4. TCP的拥塞控制由4个核心算法组成。“慢启动”（Slow Start），“拥塞避免”（Congestion avoidance），“快速重传 ”（Fast Retransmit），“快速恢复”（Fast Recovery）

### 8、什么是 socket？简述基于 tcp 协议的套接字通信流程。

多个 TCP 与 UDP 同时为多个应用程序提供并发服务时，可能需要通过同一个 TCP 协议端口传输数据，未来区别不同的应用程序及连接，计算机系统为此提供称为套接字(Socket）的接口。

1. 服务器先用 socket 函数来建立一个套接字，用这个套接字完成通信的监听。 
2. 用 bind 函数来绑定一个端口号和 IP 地址
3. 服务器调用 listen 函数，使这个端口和 IP 处于监听状态,等待连接。 
4. 客户端用 socket 函数建立一个套接字，设定远程 IP 和端口。 
5. 客户端调用 connect 函数连接远程计算机指定的端口。 
6. 服务器用 accept 函数来接受远程计算机的连接，建立起与客户端之间的通信。 
7. 建立连接以后，客户端与服务器都可以使用 write 或 read 函数向 socket 中写入数据，或读取对方发送过来的数据
8. 完成通信以后，用 close 函数关闭 socket 连接。 

### 9、什么是粘包？ socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？

TCP 流数据传输，如果因为某种原因导致多个包被合并传输的情况，被称为粘包。

1. TCP 基于字节流，没有维护消息之间的边界，发送的字节流存在 MSS(最大报文端长度)
2. 缓冲区一条消息的字节大小超过发送缓冲区的大小
3. 数据链路层发送的数据有 MTU(最大传输单元)的限制
4. 流量控制、拥塞控制
5. TCP 的延迟发送问题

### 10、IO 多路复用的作用？

避免多个 socket 的请求阻塞，可以在同一个线程内同时处理多个 IO 请求。

### 11、什么是防火墙以及作用？

数据通常在使用互联网时在网络空间中的计算机与服务器和路由器之间进行交换，防火墙的目的是监视此数据（以数据包的形式发送）并检查是否安全。防火墙通过确定数据包是否符合已经建立的规则来做到这一点。根据这些规则，数据包被拒绝或接受。

1. 网络安全的屏障
2. 强化网络安全策略
3. 网络存取和访问进行监控审计
4. 防止内部信息的外泄

### 12、select、poll、epoll 模型的区别？

都是 IO 多路复用的机制，但它们本身的读写过程是阻塞的。

poll的实现和select非常相似，只是描述fd集合的方式不同，poll使用pollfd结构而不是select的fd_set结构，其他的都差不多。

select和poll都只提供了一个函数——select或者poll函数。而epoll提供了三个函数，epoll_create,epoll_ctl和epoll_wait，epoll_create是创建一个epoll句柄；epoll_ctl是注册要监听的事件类型；epoll_wait则是等待事件的产生。

都需要自己不断轮询所有fd集合，直到设备就绪，期间可能要睡眠和唤醒多次交替，但是select和poll在“醒着”的时候要遍历整个fd集合，而epoll在“醒着”的时候只要判断一下就绪链表是否为空就行了，这节省了大量的CPU时间。这就是回调机制带来的性能提升。

select，poll每次调用都要把fd集合从用户态往内核态拷贝一次，并且要把current往设备等待队列中挂一次，而epoll只要一次拷贝，而且把current往等待队列上挂也只挂一次

### 13、简述进程、线程、协程的区别以及应用场景？

[进程和线程、协程的区别](http://www.cnblogs.com/lxmhhy/p/6041001.html)
```
一、概念
　　1、进程
进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调度的一个独立单位。每个进程都有自己的独立内存空间，不同进程通过进程间通信来通信。由于进程比较重量，占据独立的内存，所以上下文进程间的切换开销（栈、寄存器、虚拟内存、文件句柄等）比较大，但相对比较稳定安全。
　　2、线程
线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源。线程间通信主要通过共享内存，上下文切换很快，资源开销较少，但相比进程不够稳定容易丢失数据。
　　3、协程
协程是一种用户态的轻量级线程，协程的调度完全由用户控制。协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈，直接操作栈则基本没有内核切换的开销，可以不加锁的访问全局变量，所以上下文的切换非常快。

二、区别：
　　1、进程多与线程比较
线程是指进程内的一个执行单元,也是进程内的可调度实体。线程与进程的区别:
1) 地址空间:线程是进程内的一个执行单元，进程内至少有一个线程，它们共享进程的地址空间，而进程有自己独立的地址空间
2) 资源拥有:进程是资源分配和拥有的单位,同一个进程内的线程共享进程的资源
3) 线程是处理器调度的基本单位,但进程不是
4) 二者均可并发执行
5) 每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口，但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制
　　2、协程多与线程进行比较
1) 一个线程可以多个协程，一个进程也可以单独拥有多个协程，这样python中则能使用多核CPU。
2) 线程进程都是同步机制，而协程则是异步
3) 协程能保留上一次调用时的状态，每次过程重入时，就相当于进入上一次调用的状态
```

### 14、GIL 锁是什么？

全称 Global Interpreter Lock，python设计之初的考虑，为了数据安全所做的决定。同一时刻只允许一个线程运行。

### 15、Python 中如何使用线程池和进程池？

标准库提供了concurrent.futures 模块，它提供了 ThreadPoolExecutor 和 ProcessPoolExecutor 两个类，为编写线程池/进程池提供了直接的支持。

```python
# example1.py
from concurrent.futures import ThreadPoolExecutor
import time
def return_future_result(message):
    time.sleep(2)
    return message
pool = ThreadPoolExecutor(max_workers=2)  # 创建一个最大可容纳2个task的线程池
future1 = pool.submit(return_future_result, ("hello"))  # 往线程池里面加入一个task
future2 = pool.submit(return_future_result, ("world"))  # 往线程池里面加入一个task
print(future1.done())  # 判断task1是否结束
time.sleep(3)
print(future2.done())  # 判断task2是否结束
print(future1.result())  # 查看task1返回的结果
print(future2.result())  # 查看task2返回的结果
```

```python
# example2.py
from concurrent.futures import ProcessPoolExecutor
import time
def return_future_result(message):
    time.sleep(2)
    return message
pool = ProcessPoolExecutor(max_workers=2)
future1 = pool.submit(return_future_result, ("hello"))
future2 = pool.submit(return_future_result, ("world"))
print(future1.done())
time.sleep(3)
print(future2.done())
print(future1.result())
print(future2.result())
```

### 16、threading.local 的作用？

用来保存一个全局变量，但是这个全局变量只有在当前线程才能访问，在不同的线程里面赋值不会覆盖之前的值，因为每个线程里面都有一个单独的空间来保存这个数据，而且这个数据是隔离的，其他线程无法访问

### 17、进程之间如何进行通信？

每个进程各自有不同的用户地址空间，不同进程的全局变量在其他进程中无法查看。进程间交换数据需要通过内核，在内核中开辟缓冲区，不同进程通过缓冲区传输数据，这种机制称为进程间通信(IPC)。

方式：管道，有名管道，信号，消息队列，共享内存，信号量，套接字

### 18、什么是并发和并行？

并发：不同进程同时存在，交替进行

并行：不同进程同时进行

并行是并发的子集。

### 19、进程锁和线程锁的作用？

线程锁：主要用来给方法、代码块加锁。当某个方法或者代码块使用锁时，那么在同一时刻至多仅有有一个线程在执行该段代码。当有多个线程访问同一对象的加锁方法/代码块时，同一时间只有一个线程在执行，其余线程必须要等待当前线程执行完之后才能执行该代码段。但是，其余线程是可以访问该对象中的非加锁代码块的。

进程锁：也是为了控制同一操作系统中多个进程访问一个共享资源，只是因为程序的独立性，各个进程是无法控制其他进程对资源的访问的，但是可以使用本地系统的信号量控制

### 20、解释什么是异步非阻塞？

1. 同步与异步是关于指令执行顺序的。
2. 阻塞非阻塞是关于线程与进程的。
3. 两者本身并没有必然的关联系。

```
同步是指代码调用IO操作时，必须等待IO操作完成才返回的调用方式。
异步是指代码调用IO操作时，不必等IO操作完成就返回的调用方式。

同步是最原始的调用方式。
异步则需要多线程，多CPU或者非阻塞IO的支持。

阻塞是指调用线程或者进程被操作系统挂起。
非阻塞是指调用线程或者进程不会被操作系统挂起。
```

### 21、路由器和交换机的区别？

```
普通用户用途：
交换机用来将一根网线变为多根，如果网络需要登录大家各自分别登录。
路由器用来将一条网络变为多条，分出的多条网络共享主线的网络带宽。

交换机工作于数据链路层，用来隔离冲突域，连接的所有设备同属于一个广播域（子网），负责子网内部通信。

路由器工作于网络层，用来隔离广播域（子网），连接的设备分属不同子网，工作范围是多个子网之间，负责网络与网络之间通信。
```

### 22、什么是域名解析？

域名解析是把域名指向网站空间IP，让人们通过注册的域名可以方便地访问到网站的一种服务。IP地址是网络上标识站点的数字地址，为了方便记忆，采用域名来代替IP地址标识站点地址。域名解析就是域名到IP地址的转换过程。域名的解析工作由DNS服务器完成。

### 23、如何修改本地 hosts 文件？

将文件复制到其他位置，记事本/文本编辑方式打开、修改；命令行进入目录，vim 方式打开、修改。

### 24、生产者消费者模型应用场景及优势？

数据的产生与消耗并非严格一一对应，有缓冲区作为数据缓冲使用，比较适用于生产者消费者模型。

优势：解耦，支持并发，支持忙闲不均

### 25、什么是 cdn？

CDN的全称是Content Delivery Network，即内容分发网络。其基本思路是尽可能避开互联网上有可能影响数据传输速度和稳定性的瓶颈和环节，使内容传输的更快、更稳定。通过在网络各处放置节点服务器所构成的在现有的互联网基础之上的一层智能虚拟网络，CDN系统能够实时地根据网络流量和各节点的连接、负载状况以及到用户的距离和响应时间等综合信息将用户的请求重新导向离用户最近的服务节点上。其目的是使用户可就近取得所需内容，解决 Internet网络拥挤的状况，提高用户访问网站的响应速度。

### 26、LVS 是什么及作用？

LVS 的英文全称是 Linux Virtual Server，即Linux虚拟服务器。

LVS 主要用于多服务器的负载均衡。它工作在网络层，可以实现高性能，高可用的服务器集群技术。它廉价，可把许多低性能的服务器组合在一起形成一个超级服务器。它易用，配置非常简单，且有多种负载均衡的方法。它稳定可靠，即使在集群的服务器中某台服务器无法正常工作，也不影响整体效果。另外可扩展性也非常好。

### 27、Nginx 是什么及作用？

Nginx 是一款高性能的 HTTP 和反向代理服务器。也是一个IMAP/POP3/SMTP代理服务器。

Nginx本身就可以托管网站，进行HTTP服务处理，也可以作为反向代理服务器使用。

### 28、keepalived 是什么及作用?

keepalived是一个类似于layer3, 4 & 5交换机制的软件，也就是我们平时说的第3层、第4层和第5层交换。Keepalived是自动完成，不需人工干涉。

Keepalived的作用是检测服务器的状态，如果有一台web服务器宕机，或工作出现故障，Keepalived将检测到，并将有故障的服务器从系统中剔除，同时使用其他服务器代替该服务器的工作，当服务器工作正常后Keepalived自动将服务器加入到服务器群中，这些工作全部自动完成，不需要人工干涉，需要人工做的只是修复故障的服务器。

### 29、haproxy 是什么以及作用？

HAProxy是免费、极速且可靠的用于为TCP和基于HTTP应用程序提供高可用、负载均衡和代理服务的解决方案，尤其适用于高负载且需要持久连接或7层处理机制的web站点。

### 30、什么是负载均衡？

负载平衡（Load balancing）是一种计算机技术，用来在多个计算机（计算机集群）、网络连接、CPU、磁盘驱动器或其他资源中分配负载，以达到最优化资源使用、最大化吞吐率、最小化响应时间、同时避免过载的目的。 

### 31、什么是 rpc 及应用场景？

RPC (Remote Procedure Call)是一个计算机通信协议，该协议允许运行于一台计算机的程序调用另一台计算机的子程序，而程序员无需额外地为这个交互作用编程。

RPC是一个分布式计算的CS模式，总是由Client向Server发出一个执行若干过程请求，Server接受请求，使用客户端提供的参数，计算完成之后将结果返回给客户端。

### 32、简述 asyncio 模块的作用和应用场景。

asyncio是Python 3.4 试验性引入的异步I/O框架（PEP 3156），提供了基于协程做异步I/O编写单线程并发代码的基础设施。其核心组件有事件循环（Event Loop）、协程(Coroutine）、任务(Task)、未来对象(Future)以及其他一些扩充和辅助性质的模块。

### 33、简述 gevent 模块的作用和应用场景。

gevent是一个使用完全同步编程模型的可扩展的异步I/O框架。

### 34、twisted 框架的使用和应用？

Twisted是用Python实现的基于事件驱动的网络引擎框架。

## 第三部分 数据库和缓存（46 题）


### 1、列举常见的关系型数据库和非关系型都有那些？

关系型：Oracle，SQLserver，MySQL，Access

非关系型：SQLite，Redis，MongoDB

### 2、MySQL 常见数据库引擎及比较？

InnoDB，默认事务型引擎，支持事务、安全表、行锁定和外键、崩溃后恢复

myisam，拥有较快的插入、查询速度，但不支持事务，支持表锁、全文索引

memory，将表中数据存储到内存中，为查询及引用其他表数据提供快速访问

### 3、简述数据三大范式？

[解释一下关系数据库的第一第二第三范式？](https://www.zhihu.com/question/24696366)

范式：一张数据表的表结构所符合的某种设计标准的级别。数据库范式也分为1NF，2NF，3NF，BCNF，4NF，5NF。一般在我们设计关系型数据库的时候，最多考虑到BCNF就够。

1NF：符合1NF的关系中的每个属性都不可再分。

2NF：在1NF的基础之上，消除了非主属性对于码的部分函数依赖。(字段必须完全依赖于全部主键)

3NF：在2NF的基础之上，消除了非主属性对于码的传递函数依赖。(非主键字段必须互不依赖)

### 4、什么是事务？MySQL 如何支持事务？

数据库事务（简称：事务）是数据库管理系统执行过程中的一个逻辑单位，由一个有限的数据库操作序列构成。

ACID 特性：原子性，一致性，隔离性，持久性

用 BEGIN, ROLLBACK, COMMIT来实现；直接用 SET 来改变 MySQL 的自动提交模式。

### 5、简述数据库设计中一对多和多对多的应用场景？

一对多：博客系统，文章与评论，一篇文章可以有多条评论

多对多：选课系统，课程与学生，每个学生可以选多门课，多个学生可以选同一门课

### 6、如何基于数据库实现商城商品计数器？

[Mysql计数器表设计](https://blog.csdn.net/xue632777974/article/details/72765724)

### 7、常见 SQL（必备）

> 详见[武沛齐博客](https://www.cnblogs.com/wupeiqi/articles/5729934.html)

### 8、简述触发器、函数、视图、存储过程？

对某个表进行【增/删/改】操作的前后如果希望触发某个特定的行为时，可以使用触发器，触发器用于定制用户对表的行进行【增/删/改】前后的行为。

函数包括系统函数和自定义函数。自定义函数应该属于某个数据库，函数内部可以有各种编程语言的元素：变量，流程控制，函数调用；还可以有增删改等语句，但是不可以有select（或show或desc）这种返回结果集的语句！

视图是一个虚拟表（非真实存在），其本质是【根据SQL语句获取动态的数据集，并为其命名】，用户使用时只需使用【名称】即可获取结果集，并可以将其当作表来使用。

存储过程是一个SQL语句集合，当主动去调用存储过程时，其中内部的SQL语句会按照逻辑执行。

### 9、MySQL 索引种类

普通、唯一、全文、组合(复合)

### 10、索引在什么情况下遵循最左前缀的规则？

使用组合索引时

### 11、主键和外键的区别？

主键：唯一标识一条记录，不能有重复的，不允许为空

外键：表的外键是另一表的主键, 外键可以有重复的, 可以是空值

### 12、MySQL 常见的函数？

abs, floor, least, mod, pi

### 13、列举 创建索引但是无法命中索引的 8 种情况。

1. 如果条件中有or，即使其中有条件带索引也不会使用。(需要使用 or 时，条件中每列都加索引)
2. 多列索引，未使用第一部分
3. like 以 % 开始
4. 列类型为字符串时，条件中数据需要使用引号
5. MySQL 系统估计全表扫描比索引快，不使用索引
6. 无查询条件，或条件上未使用索引列
7. 索引不存储 NULL 值
8. 不适合键值较少的列

### 14、如何开启慢日志查询？

`set slow_query_log='ON';`

### 15、数据库导入导出命令（结构 + 数据）？

`mysqldump -u username -p password databasename > databasename.sql`

`mysql -u username -p password databasename < databasename.sql`

### 16、数据库优化方案？

### 17、char 和 varchar 的区别？

char 固定长度；varchar 变长

### 18、简述 MySQL 的执行计划？

[执行计划](https://juejin.im/post/5a52386d51882573443c852a)就是Mysql如何执行一条Sql语句,包括Sql查询的顺序、是否使用索引、以及使用的索引信息等内容。

### 19、在对 name 做了唯一索引前提下，简述以下区别：

```sql
select * from tb where name = ‘Oldboy - Wupeiqi’
select * from tb where name = ‘Oldboy - Wupeiqi’ limit1
```

没有太大区别。？

### 20、1000w 条数据，使用 limit offset 分页时，为什么越往后翻越慢？如何解决？

### 21、什么是索引合并？

将几个索引的范围扫描合并成一个索引。

### 22、什么是覆盖索引？

如果索引包含满足查询的所有数据，就称为覆盖索引。

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


## 第四部分 前端、框架和其他（155 题）


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

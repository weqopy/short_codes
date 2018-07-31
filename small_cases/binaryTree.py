
# 二叉树


# 二叉树
# 添加子树
# 深度查找 & 广度查找


from queue import Queue


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.lc = None
        self.rc = None

    def insert_left(self, value):
        if self.lc is None:
            self.lc = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.lc = self.lc
            self.lc = new_node

    def insert_right(self, value):
        if self.rc is None:
            self.rc = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.rc = self.rc
            self.rc = new_node

    def pre_order(self):
        print(self.value)

        if self.lc:
            self.lc.pre_order()

        if self.rc:
            self.rc.pre_order()

    def in_order(self):
        if self.lc:
            self.lc.in_order()

        print(self.value)

        if self.rc:
            self.rc.in_order()

    def post_order(self):
        if self.lc:
            self.lc.post_order()

        if self.rc:
            self.rc.post_order()

        print(self.value)

    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)

            if current_node.lc:
                queue.put(current_node.lc)

            if current_node.rc:
                queue.put(current_node.rc)


a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.lc
b_node.insert_right('d')

c_node = a_node.rc
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.rc
e_node = c_node.lc
f_node = c_node.rc


for i in 'abcdef':
    print(i + '_node: ', eval(i + '_node').value)
print('a_node.pre_order: ')
a_node.pre_order()
print('a_node.in_order: ')
a_node.in_order()
print('a_node.post_order: ')
a_node.post_order()
print('a_node.bfs: ')
a_node.bfs()

class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def __init__(self):
        self.r = []

    def flatten(self, nestedList):
        # 递归方法
        if isinstance(nestedList, int):
            self.r.append(nestedList)
        else:
            for i in nestedList:
                if isinstance(i, int):
                    self.r.append(i)
                else:
                    self.flatten(i)
        return self.r

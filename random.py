# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List
from functools import reduce

class NestedInteger(object):
    def __init__(self, o):
        self.integer = None
        self.list = None
        if type(o) == int:
            self.integer = o
        else:
            self.list = [NestedInteger(e) for e in o]

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.integer is not None

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.integer

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.list

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def flatten(nl) -> List[int]:
            if type(nl) is list:
               return reduce(lambda a,b: flatten(a).extend(flatten(b)), nl.getList())

            elif nl.isInteger():
                return [nl.getInteger()]

            else:
        reduce(lambda a,b: flatten(a).extend(flatten(b)), nl.getList())

        self.flat = []
        self.i = 0
        flatten(nestedList, self.flat)
        
    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            raise IndexError()
        
        self.i += 1
        return self.flat[self.i - 1]
            
            
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.flat)

# Your NestedIterator object will be instantiated and called as such:
nestedList = [NestedInteger(e) for e in [1, [2, 3]]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): 
    val = i.next()
    v.append(val)
print(v)
'''
Problem:

    Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

    Each element is either an integer, or a list -- whose elements may also be integers or other lists.

    Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. 
    i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

    Example 1:
    Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

    Example 2:
    Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)

'''



#class NestedInteger(object):
#    def isInteger(self):
#
#    def getInteger(self):
#
#    def getList(self):

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
            :type nestedList: List[NestedInteger]
            :rtype: int
            """
        def getListSum(nestedList, prevSum):
            intSum = prevSum
            newList = []
            for elem in nestedList:
                if elem.isInteger():
                    intSum += elem.getInteger()
                else:
                    newList.extend(elem.getList())    # note: extend
            listSum = 0 if len(newList) == 0 else getListSum(newList, intSum)

            return intSum + listSum


        return getListSum(nestedList, 0)

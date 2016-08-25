'''
Problem:

Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext


The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
     The name of a file contains at least a . and an extension.
     The name of a directory or sub-directory will not contain a ..

Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
'''

'''
Solution 1:

See this example:

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

Becasue, “tfile1.ext” and “tsubsubdir1” are in the same depth 而且 这两个 filename 和 dirname 是按顺序出现的。也就是说同一层的两个file是按顺序先后出现，然后才是再到下一层的或者回到上一层，开始一个新的path.所以发现后面的可以直接overwrite pathlen里面对应的index的lenth (它们之中如果有maxlen 也已经被 maxlen = max(maxlen, pathlen[depth]+len(name))给update过了)

Reference:
    https://discuss.leetcode.com/topic/55097/simple-python-solution/5
    https://discuss.leetcode.com/topic/55104/very-concise-5-liner-in-python-52ms
'''

class Solution(object):
    def lengthLongestPath(self, input):

        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if "." in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth+1] = pathlen[depth] + len(name) + 1
        return maxlen

'''
Solution 2: using int to store length not list

have to update length every time meet a new dir depth. Use path as a stack.

Reference:
    https://discuss.leetcode.com/topic/55097/simple-python-solution/5
'''
class Solution(object):
    def lengthLongestPath(self, input):
        """
            :type input: str
            :rtype: int
            """
        maxlen,curlen = 0,0
        maxdepth = 0
        path = []

        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if depth <= maxdepth and path:
                for i in range(maxdepth-depth+1):  #开始一个新的 pop out 旧的

                    last = path.pop()
                    curlen -= len(last)
                    if "." not in last:
                        curlen -= 1

            path.append(name)
            curlen += len(name)

            if "." in name:
                maxlen = max(maxlen, curlen)
            else:
                curlen += 1
                maxdepth = depth

        return maxlen

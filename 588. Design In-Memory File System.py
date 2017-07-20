'''
Problem:


Design an in-memory file system to simulate the following functions:

ls: 
    Given a path in string format. If it is a file path, return a list that only contains this file's name. 
    If it is a directory path, return the list of file and directory names in this directory. 
    Your output (file and directory names together) should in lexicographic order.

mkdir: 
    Given a directory path that does not exist, you should make a new directory according to the path. 
    If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: 
    Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. 
    If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: 
    Given a file path, return its content in string format.

Example:
Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]
'''

class FileSystem(object):

    def __init__(self):
        self.root = {'dirs' : {}, 'files': {}}


    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        node, type = self.getExistedNode(path)
        if type == 'dir': # dir
            return sorted(node['dirs'].keys() + node['files'].keys())
        else: # file
            return [path.split('/')[-1]]


    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        node = self.root
        for dir in filter(len, path.split('/')):
            if dir not in node['dirs']: 
                node['dirs'][dir] = {'dirs' : {}, 'files': {}}
            node = node['dirs'][dir]


    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        dirs = filePath.split('/')
        path, file = '/'.join(dirs[:-1]), dirs[-1]
        self.mkdir(path)
        node, type = self.getExistedNode(path)
        if file not in node['files']: node['files'][file] = ''
        node['files'][file] += content


    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        dirs = filePath.split('/')
        path, file = '/'.join(dirs[:-1]), dirs[-1]
        node, type = self.getExistedNode(path)
        return node['files'][file]
        
        
    def getExistedNode(self, path):
        """
        :type path: str
        :rtype: str
        """
        node = self.root
        for dir in filter(len, path.split('/')):
            if dir in node['dirs']: 
                node = node['dirs'][dir]
            else: 
                return node, 'file'
        return node, 'dir'

'''
Problem:

    Given a pattern and a string str, find if str follows the same pattern.
    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
     pattern = "abab", str = "redblueredblue" should return true.
     pattern = "aaaa", str = "asdasdasdasd" should return true.
     pattern = "aabb", str = "xyzabcxzyabc" should return false.

Notes:
     You may assume both pattern and str contains only lowercase letters.
'''



class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
            :type pattern: str
            :type str: str
            :rtype: bool
            """
        def isMatch(pattern, pstart, str, strStart, mp, st):
            # base case
            if pstart == len(pattern) and strStart == len(str):
                return True
            if pstart == len(pattern) or strStart == len(str):
                return False

            # get current pattern character
            p = pattern[pstart]

            # case 1: the pattern character exists
            if mp.has_key(p):
                word = mp[p]
                # then check if we can use it to match str[i...i+s.length()]
                if not str.startswith(word, strStart):
                    return False
                return isMatch(pattern, pstart+1, str, strStart+len(word), mp, st)


            # case 2: the pattern character does not exist in the map
            for k in range(strStart, len(str)):
                newStr = str[strStart:k+1]
                # if the newStr already exist in the set,
                # and we can't find the pattern - string pair in the map (case1)
                # we should also ignore this string here and append more character to the string
                if newStr in st:
                    continue
                # create new key in map and add the new string in the map
                mp.setdefault(p, newStr)
                st.add(newStr)
                # continue to match the rest
                if isMatch(pattern, pstart+1, str, strStart+len(newStr), mp, st):
                    return True
                # backtracking
                else:
                    del mp[p]           # delete the entry in the map
                    st.remove(newStr)   # delete the element in the set
            # we've tried our best but still no luck
            return False

        st = set()
        mp = {}
        return isMatch(pattern, 0, str, 0, mp, st)

'''
Problem:
   
Given a string that contains only digits 0-9 and a target value, 
return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
   
     Examples:
     "123", 6 -> ["1+2+3", "1*2*3"]
     "232", 8 -> ["2*3+2", "2+3*2"]
     "105", 5 -> ["1*0+5","10-5"]
     "00", 0 -> ["0+0", "0-0", "0*0"]
     "3456237490", 9191 -> []
'''

'''
Solution:                
           
Complexities:
    Time: O(n)
    Space: O(1)

'''

class Solution(object):
    def addOperators(self, num, target):
        def dfs(res, num, target, curstr, pos, cur_total, pre_val, pre_op):
            if pos == len(num) and cur_total == target:    # base case
                res.append(curstr[:])
            else:
                for i in range(pos+1,len(num)+1):
                    t = num[pos:i]
                    t_val = int(t)
                    if str(t_val) != t: continue    # note
                    # + operation
                    dfs(res, num, target, curstr+"+"+t, i, cur_total+t_val, t_val, "+")
                    # - operation
                    dfs(res, num, target, curstr+"-"+t, i, cur_total-t_val, t_val, "-")
                    # * operation
                    if pre_op == "+":    # 3+5*2   8-5 + 5*2
                        #cur_total = cur_total-pre_val+pre_val*t_val
                        dfs(res, num, target, curstr+"*"+t, i, cur_total-pre_val+pre_val*t_val, pre_val*t_val,pre_op)
                    elif pre_op == "-":  # 3-5*2
                        #cur_total = cur_total+pre_val-pre_val*t_val
                        dfs(res, num, target, curstr+"*"+t, i, cur_total+pre_val-pre_val*t_val, pre_val*t_val,pre_op)
                    else: # pre_op == "*"
                        #cur_total = pre_val*t_val
                        dfs(res, num, target, curstr+"*"+t, i, pre_val*t_val, pre_val*t_val,pre_op)
            return



        res = []
        if not num:
            return res
        for i in range(1,len(num)+1):
            s = num[:i]
            s_val = int(s)
            if str(s_val) != s: continue
            dfs(res, num, target, s, i, s_val, s_val, "#")
        return res

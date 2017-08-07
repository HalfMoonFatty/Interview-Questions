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
        
        def dfs(num, pos, target, curstr, cur_total, pre_val, pre_op, result):
            if pos == len(num) and cur_total == target:    # base case
                result.append(curstr[:])
                return

            for i in range(pos+1,len(num)+1):
                t = num[pos:i]
                t_val = int(t)
                if str(t_val) != t: continue    # note
                # + operation
                dfs(num, i, target, curstr+"+"+t, cur_total+t_val, t_val, "+", result)
                # - operation
                dfs(num, i, target, curstr+"-"+t, cur_total-t_val, t_val, "-", result)
                # * operation
                if pre_op == "+":    # 3+5*2   8-5 + 5*2
                    #cur_total = cur_total-pre_val+pre_val*t_val
                    dfs(num, i, target, curstr+"*"+t, cur_total-pre_val+pre_val*t_val, pre_val*t_val,pre_op, result)
                elif pre_op == "-":  # 3-5*2
                    #cur_total = cur_total+pre_val-pre_val*t_val
                    dfs(num, i, target, curstr+"*"+t, cur_total+pre_val-pre_val*t_val, pre_val*t_val,pre_op, result)
                else: # pre_op == "*"
                    #cur_total = pre_val*t_val
                    dfs(num, i, target, curstr+"*"+t, pre_val*t_val, pre_val*t_val,pre_op, result)



        result = []
        if not num:
            return result
        for i in range(1,len(num)+1):
            s = num[:i]
            s_val = int(s)
            if str(s_val) != s: continue
            dfs(num, i, target, s, s_val, s_val, "#", result)
        return result

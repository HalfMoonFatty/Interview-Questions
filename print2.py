* Knapsack Problem:

	- 单次选择+最大价值
	- 重复选择+最大价值

	- 单次选择+装满可能性总数   
	- 重复选择+唯一排列+装满可能性总数
	- 重复选择+不同排列+装满可能性总数




* String Matching:

	- Wildcard Matching 	

		if p[j-1] != '*': dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == '?')
        else: dp[i][j] = dp[i][j-1] or dp[i-1][j]
		
	- Regular Express Matching

	 	if p[j-1] != '*': dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == '.')
        else: dp[i][j] = dp[i][j-2] or (p[j-2] == s[i-1] or p[j-2] == '.') and dp[i-1][j]
		
	- Edit Distance

		if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
        else: dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
		
	- Interleaving String

		dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
		
	- Distinct Subsequence

		if t[i-1] != s[j-1]: dp[i][j] = dp[i][j-1]
        else: dp[i][j] = dp[i][j-1] + dp[i-1][j-1]




* Partition Array / String <Recursion>:
	
	- Break string S into words in Dict
	- Partition string S to be palindrome

	for i in range(1, len(s)+1):
		for j in range(i-1,-1,-1):




* Longest / Largest Sequence:
	
	- Longest Valid Parentheses

		if s[i - 1] == "(": dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
        elif i-1-dp[i-1] >= 0  and s[i-1-dp[i-1]] == '(': dp[i] = 2 + dp[i-1] + (dp[i-2-dp[i-1]] if i-dp[i-1]-2 >= 0 else 0)
		
		
	- Longest Palindromic Subsequence  
														|_________j_______________|_________|	
		for i in range(len(s)):                         0 ----------------------> i
            dp[i][i] = 1
            for j in range(i-1,-1,-1):    # j 从 i 到 0	
			
														|_________|_______________j_________|	
		for i in range(n-1,-1,-1):              		0         i <--------------------- n-1
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
                else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
				
			
	- Larget Subset Si % Sj == 0 or Sj % Si == 0

		for i in range(len(nums)):
            for j in range(i,-1,-1):    # j 从 i 到 0	
			
			
	- Longest Wiggle Subsequence

		for i in range(1,len(nums)):
            for j in range(i):    # j 从 0 到 i			
			
			
	- LIS 1D/2D (LCS)
	
		for i in range(len(nums)):
            for j in range(i):    # j 从 0 到 i
			
	    for i in range(1,n+1):
            ind = bisect.bisect_left(seqLength,nums[i-1])
            seqLength[ind] = nums[i-1]
            maxLen = max(maxLen, ind+1)
			
			
	- Number of Arithmetic Slice

		for i in range(len(A)):
            for j in range(i):    # j 从 0 到 i
			    delta = A[i] - A[j]
                dp[i][delta] += 1
                if delta in dp[j]: dp[i][delta] += dp[j][delta]

			
			
			
* Growing Intervals:
	
	- Burst Ballons

		for k in range(2,n):
            for left in range(0,n-k):        
                right = left + k
                for last in range(left+1,right):    # last in [left+1,right-1]
                    dp[left][right] = max(dp[left][right], nums[left]*nums[last]*nums[right]+dp[left][last]+dp[last][right])
		    
			
	- Guess Number (min of max)

		for length in range(1,n):
            for start in range(1,n-length+1):  # as number starts from [1 to n]
                dp[start][start+length] = sys.maxint
                for k in range(start,start+length+1):      # [start,start+length]
                    if k == n: guessCost = k + dp[start][k-1]
                    else: guessCost = k + max(dp[start][k-1],dp[k+1][start+length])
                    dp[start][start+length] = min(dp[start][start+length],guessCost)
					
					
	- Shortest Encode String
	
	    for l in range(length):
            for i in range(length - l):
                if s[i:i+l+1] == s[i] * length: 
                    res[i][i+l] = str(length) + '[' + s[i] + ']'
                    dp[i][i+l] = len(res[i][i+l])
                else:
                    res[i][i+l] = s[i:i+l+1]
                    dp[i][i+l] = l+1

                for j in range(i, i + l):

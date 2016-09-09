'''
Problem:


'''

# Solution:
state: 
	f[x][y] 现在还第x到第y的硬币,现在先手取硬币的人最后最多取硬币价值 

function:
	f[x][y] = max(min(f[x+2][y], f[x+1][y-1])+a[x] ) , (min(f[x][y-2], f[x+1][y-1])+a[y] )

intialize:
	f[x][x] = a[x]
	f[x][x+1] = max(a[x],a[x+1])
	
Answer:
	f[0][n] > sum(a)/2

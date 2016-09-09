'''
Problem:

There are n coins with different value in a line. Two players take turns to take one coins from left side or right side until there are no more coins left. 
The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?
'''

# Solution:
state: 
	f[x][y] 现在还第x到第y的硬币,现在先手取硬币的人最后最多取硬币价值 

function:
	f[x][y] = max(min(f[x+2][y], f[x+1][y-1])+a[x]) , (min(f[x][y-2], f[x+1][y-1])+a[y])

intialize:
	f[x][x] = a[x]
	f[x][x+1] = max(a[x],a[x+1])
	
answer:
	f[0][n] > sum(a)/2

note: 
	f[x+2][y]:   后手拿x+1,先手拿x
	f[x+1][y-1]: 后手拿y,先手拿x
	f[x][y-2]:   后手拿y-1,先手拿y
	f[x+1][y-1]: 后手拿x,先手拿y
	f[x][y] = max(min(f[x+2][y], f[x+1][y-1])+a[x]) , (min(f[x][y-2], f[x+1][y-1])+a[y])

'''
Problem:

亚洲微软研究院所在的希格玛大厦一共有6部电梯。在高峰时间，每层都有人上下，电梯每层都停。小飞常常会被每层都停的电梯弄的很不耐烦，于是他提出了这样一个办法：
由于楼层并不算太高，那么在繁忙的上下班时间，每次电梯从一层往上走时，我们只允许电梯停在其中的某一层。所有乘客从一楼上电梯，到达某层后，电梯停下来，
所有乘客再从这里爬楼梯到自己的目的层。在一楼的时候，每个乘客选择自己的目的层，电梯则计算出应停的楼层。

问：电梯停在哪一层楼，能够保证这次乘坐电梯的所有乘客爬楼梯的层数之和最少？

Follow - up: 往上爬一层要耗费K个单位的能量，往下走耗费1个单位的能量, 电梯应该停在哪一层？
* 只需要计算N1+N2-N3变成N1+N2-N3*K即可。其余的都是一样的。
'''

'''
Solution 1: 暴力枚举

Time: O(N^2)
'''

def findTargetFloor(personOnFloor, numFloors):
    min_floors = sys.maxint
    target_floor = 1
    
    for i in range(1, numFloors):
        total_floors = 0
        for j in range(1, numFloors):
            total_floors += personOnFloor[j] * abs(j - i)
            
        if total_floors < min_floors:
            min_floors = total_floors
            target_floor = i
    return target_floor
    
    
    
'''
Solution 2: DP

假设电梯停在i层楼，可以计算出所有乘客要爬楼层的层数为T,假设此时有N1个乘客在i层楼以下，N2个乘客在I层楼，N3个乘客在I层楼以上，
则当电梯停在i+1层的时候，N1+N2个乘客要多上一层楼，共多上N1+N2层，N3个乘客要少下一层楼，少下N3层楼，此时T(i+1) = T(i) + N1+N2-N3；T1很容易算出来。 
很显然，当N1+N2<N3的时候，T不断减小。另外我们还可以看出，N1+N2是递增的，N3是递减的，所以N1+N2一旦大于N3的时候，我们直接退出循环即可，没有必要再计算下去了。
'''

def findTargetFloor(personOnFloor, numFloors):
    min_floors = 0    # dp[1]
    target_floor = 1 
    
    N1, N2, N3 = 0, personOnFloor[1], 0
    for i in range(2, numFloors+1):
        N3 += personOnFloor[i]
        min_floors += personOnFloor[i] * (i-1)
    
    for i in range(2, numFloors+1):
        if N1 + N2 < N3:
            target_floor = i
            min_floors += N1 + N2 - N3

            N1 += N2
            N2 = personOnFloor[i]
            N3 -= personOnFloor[i]
        else: 
            break
    return target_floor
    
    

'''
Solution 3:  中位数

其实这道题目仔细分析起来就是求一组数据的中位数而已。
假设两人，分别到3层楼和8层楼下，在3和8之间取一点，使得到两个点距离最小，很显然，在3和8中的每一点到3和8的距离之和都是相等的。
推广到2 3 5 5 6 7 8 8 9这样一组数据，target_floor为中位数。
'''

def findTargetFloor(personOnFloor, numFloors):
    median = numFloors/2
    return median
  
'''
def findTargetFloor(personOnFloor, numFloors):
    left, right = 0, numFloors-1
    while right-left > 1:

        while personOnFloor[left] == 0: left += 1
        personOnFloor[left] -= 1

        while personOnFloor[right] == 0: right -= 1
        personOnFloor[right] -= 1

    return left
'''

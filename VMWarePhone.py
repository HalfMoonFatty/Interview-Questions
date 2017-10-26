4轮
1: Razvan Cheveresan
   Poject + Coding



2: Yang Zhe

    - Introduce Team (5 - 10 min)
    - Resume (20 mins)
    - Java synchronized collection HashMap (not synchronized) and HashTable (thread-safe)
    - Performance:
		- Q: 如果我给你一个web application 你会想要怎么evaluate web application 的 performance?
		  A: QPS, reseponse time, HA, CPU utilization (performance metrics / resource consumption)
		- Q: Given a performance issue how would you approach this problem? 
		  A: Check resource consumption / saturation (sanity check) / memory swapping...
	- Coding:
    1. Easy (5 min)
	2. Given an array (a1, a2 ... an, b1, b2 ... bn) convert that to (a1, b1, a2, b2... an, bn) in place




3: Yong Li

   - Resume (5 min)
   - Java (c++) static keyword 什么意思？Finalize?
   - c static keyword 什么意思？ - globle 
   - Synchronization 的问题：Lock 有哪几种？ 它们的差别在哪里？Critical Section在哪里 - Each node associate with a lock？
   - 看一段 code (Tree, node - VM) 
       - 在做什么？- BFS / 有问题在哪里？- 少一个check condition (少了一个if statement) 我要找一个VM name == hello: return 
       - 哪里不是很efficient?? Queue 是怎么implement的？ 用linkedlist 很好 O(1)； 用array就不好...
       - 如果mutiple threads access this tree, 如何 protect 这个tree ???
         当 pop node 和 enqueue tree node （getChildren()）之前，每个pop out的node加一个lock.
   - 加面Coding: Sorted Array of Int, Generate another Array Input Array Square, make sure output is sorted (-2,-1,0,1,2)




4: Vishnu Priya Muthukrishnan

	- Resume
	- Performance: 
		- Q: Given a performance issue how would you approach this problem? 
		  A: Quick sanity check, CPU saturation
		- Q: Linux system which can check system performance
		  A: vmstat...
	- Java:
		- What does Finalize do?
		- java string pool? Memory layout?
		  string pool: http://www.buggybread.com/2014/04/java-interview-questions-and-answers-on_5185.html
	- Coding:
		1. Sorted Array of Int, Generate another Array Input Array Square, make sure output is sorted (-2,-1,0,1,2)
		2. 2Sum (不同种做法，O(n^2), nlogn + 2pointers, hashtable(O(n)))





Lunch - Hiring Manager (Chungyen Chang  -  Director, Performance Engineering)



   





Performance:

    - Synchronization 的问题：Lock 有哪几种？ 它们的差别在哪里？
      
	    Mutex Locks: Only the holder of the lock can operate. Others block and wait off-CPU.
	      
	    Spin-Lock: Spin locks allow the holder to operate, while others requiring the lock spin on-CPU in a tight loop, checking for the lock to be released. While these can provide lock-latency access - the blocked thread never leaves CPU and is ready to run in a matter of cycles once the lock is availble - they also waste CPU resources while threads spin waiting.
	      
	    RW Lock: Reader/writer locks ensure integrity by allowing either multiple readers, or one writer only and no readers.

	- Q: 如果我给你一个web application 你会想要怎么evaluate web application 的 performance?
	  A: QPS, reseponse time, HA, CPU utilization (performance metrics / resource consumption)

	- Q: Given a performance issue how would you approach this problem? 
	  A: Check resource consumption / saturation (sanity check) / memory swapping...
	  A: Quick sanity check, CPU saturation

	- Q: Linux system which can check system performance
	  A: vmstat...

                                                                                                   
	NUMA:

	NUMA is Non-Uniform Memory Access, which links several small, cost-effective nodes using a high-performance connection. Each node contains processors and memory, much like a small SMP system. However, an advanced memory controller allows a node to use memory on all other nodes, creating a single system image. When a processor accesses memory that does not lie within its own node (remote memory), the data must be transferred over the NUMA connection, which is slower than accessing local memory. Memory access times are not uniform and depend on the location of the memory and the node from which it is accessed, as the technology’s name implies.


	Disadvantage:

	- The high latency of remote memory accesses can leave the processors under-utilized, constantly waiting for data to be transferred to the local node, and the NUMA connection can become a bottleneck for applications with high-memory bandwidth demands.
	
	- Furthermore, performance on such a system can be highly variable. It varies, for example, if an application has memory located locally on one benchmarking run, but a subsequent run happens to place all of that memory on a remote node. This phenomenon can make capacity planning difficult. 

	如果有一个CPU怎么知道L3Cache有多大？有什么方法？第一次填进去，第二次再读... Memory Access Time...


Java:

1. Java synchronized collection HashMap (not synchronized) and HashTable (thread-safe)
    1. Hashtable is synchronized, whereas HashMap is not. This makes HashMap better for non-threaded applications, as unsynchronized Objects typically perform better than synchronized ones.
	2. Hashtable does not allow null keys or values.  HashMap allows one null key and any number of null values.
	3. One of HashMap's subclasses is LinkedHashMap, so in the event that you'd want predictable iteration order (which is insertion order by default), you could easily swap out the HashMap for a LinkedHashMap. This wouldn't be as easy if you were using Hashtable.


2. Synchronize:
	First, it is not possible for two invocations of synchronized methods on the same object to interleave. When one thread is executing a synchronized method for an object, all other threads that invoke synchronized methods for the same object block (suspend execution) until the first thread is done with the object.
	  
	Second, when a synchronized method exits, it automatically establishes a happens-before relationship with any subsequent invocation of a synchronized method for the same object. This guarantees that changes to the state of the object are visible to all threads.


3. Java static keyword 什么意思？
	- Class level ownership (for both variable and method); 
	- For method only, static method cannot call non-static method and cannot reference non-static vairable. 


4. Finalize?
   Final - variable (premitive and reference); method; class
   Finally - try; catch; finally
   Finalize - finalize() is a method on java.lang.Object so exists on all Objects. The default implementation does nothing. It is called by the garbage collector when it determines there are no more references to the object. It is used for clean up, such as file references. It will never be called more than once on an object (by the JVM).


5. Java string pool? Memory layout?
   String s1 = "abc";
   String s2 = "abc";
   string pool: http://www.buggybread.com/2014/04/java-interview-questions-and-answers-on_5185.html




===
2 sums:

class Solution(object):
    def twoSum(self, nums, target):

        mp = {}

        for i in range(len(nums)):
            if mp.has_key(target-nums[i]):
                return [mp[target-nums[i]], i]
            else:
                mp[nums[i]] = i





Given a sorted array of integers: [-3, -1, 0, 1, 2]. 
Generate a sorted array of their squares: [0, 1, 1, 4, 9]


def sortArraySquares(nums):
    if not nums: return []

    result = [0] * len(nums)
    i,j = 0, len(nums)-1
    k = len(nums)-1
    while i <= j:
        if abs(nums[i]) < abs(nums[j]):
            result[k] = nums[j]*nums[j]
            j -= 1
        else:
            result[k] = nums[i]*nums[i]
            i += 1
        k -= 1
    return result



n = [-3, -1, 0, 1, 2]
print sortArraySquares(n)





Rearrange:

def rearrange(nums):
    left, right = 1, len(nums)/2
    while left < right:
        for i in range(right, left, -1):
            nums[i], nums[i-1] = nums[i-1], nums[i]

        left += 2
        right += 1

nums = [1,2,3,4,5,6,7,8]
rearrange(nums)
print nums



def rearrange2(nums):
  if len(nums) <= 2:
    return nums
  mid = len(nums)/2
  l1 = rearrange2(nums[:mid/2]+nums[mid:mid+mid/2])
  l2 = rearrange2(nums[mid/2:mid]+nums[mid+mid/2:])
  return l1+l2



nums = [1,2,3,4,5,6,7,8]
print rearrange2(nums)
print rearrange2([1,2,3,4])
# [1,3,2,4]
# [1,5,2,6,3,7,4,8]






====


Performance
===========


+ CPU

  vmstat - system CPU utilization
  mpstat - processor CPU utilization
  prstat - who is using the CPU



+ Memory

  System Memory: vmstat -p

  Process Memmory: 
    Process Virtual and Resident Set Size – ps –eo pid,vsz,rss,args
    Using pmap to Inspect Process Memory Usage – pmap –x pid

  Swap: 
    Swap Summary: swap –s
    iostat to determine if the physical swap devices are currently busy with I/O



+ Disk

Writing:
  writeback mode: the completion interrupt is sent as soon as the cache receives the data. 
  writethrough mode, writes now suffer a delay as the storage array waits for them to write to disk, before an I/O completion is sent. 

Reading:
  The storage array tries its best to serve reads from (its very large) cache, especially effective if prefetch is enabled and the workload is sequential. 

IO Size:
  For sequential access, larger I/O sizes are better; 
  For random access, I/O sizes should to be picked to match the workload. First need to know your workload.

iostat:
  3 Starting points of disk behavior: Utilization Saturation and Tput
  %b: this is percent busy and tells us disk utilization.
  wait: the average wait queue length; it is a measure of disk saturation. 
  kr/s and kw/s: kilobytes read and written per second, which tells us the current disk throughput.



+ Network

  • Packets. netstat –i Network interface packet counts.
  • Bytes. Kstat, SNMP, nx.se, and nicstat Measuring throughput in terms of bytes/sec.
  • Utilization. nicstat calculates utilization = current throughput / known maximum.
  • Saturation. network applications usually experience delays.
  • Errors. netstat -i to print error counts: collisions (small numbers are normal), input errors, and output errors (late collisions).


  netstat : packet counts and error counts
  nicstat Tool: network utilization and saturation by interface.
  ping Tool – host up and resp time
  traceroute Tool - discover the hops to a host (print response time to each hop)



+ Process
  ps
  prstat
  • SIZE. The total virtual memory size of mappings within the process, including all mapped files and devices.
  • RSS. Resident set size. The amount of physical memory mapped into the process.
  • TIME. The cumulative execution time for the process, printed in CPU hours, minutes, and seconds.
  • CPU. The percentage of recent CPU time used by the process.
  • PROCESS/NLWP. The name of the process (name of executed file) and the number of threads in the process.


  pstack - you can often determine where the process is spending most of its time
  truss - traces system calls made on behalf of a process.
  dtrace



+ Lockstat

  Two main types of user-level locks:
  • Mutex lock. An exclusive lock. A mutex lock attempts to spin while trying obtain the lock if the holder is running on a CPU, or blocks if the holder is not running or after trying to spin for a predetermined period.
  • Reader/Writer Lock. A shared reader lock. Only one person can hold the write lock, but many people could hold a reader lock while there are no writers.



+ CPU Caches

size, cache line size and  set-associativity.
• A greater size improves cache hit ratio;
• A larger cache line size can improve throughput;
• A higher set-associativity improves the effect of the Least Recently Used policy, which can avoid hot spots where the cache would otherwise have flushed frequently accessed data.






OS
====


process/thread区别，thread如何安全访问共享内存->mutex，

Both processes and threads are independent sequences of execution. 
The typical difference is that threads (of the same process) run in a shared memory space, 
while processes run in separate memory spaces.


==

Race condition:

A race condition occurs when two or more threads can access shared data and they try to change it at the same time. Because the thread scheduling algorithm can swap between threads at any time, you don't know the order in which the threads will attempt to access the shared data. Therefore, the result of the change in data is dependent on the thread scheduling algorithm, i.e. both threads are "racing" to access/change the data.


==

semaphone/mutex区别


Strictly speaking, a mutex is locking mechanism used to synchronize access to a resource. 
Only one task (can be a thread or process based on OS abstraction) can acquire the mutex. 
It means there is ownership associated with mutex, and only the owner can release the lock (mutex).

Mutexes are typically used to serialise access to a section of re-entrant code that cannot be executed 
concurrently by more than one thread. A mutex object only allows one thread into a controlled section, 
forcing other threads which attempt to gain access to that section to wait until the first thread has exited from that section.

--------

Semaphore is signaling mechanism (“I am done, you can carry on” kind of signal). 

A semaphore restricts the number of simultaneous users of a shared resource up to a maximum number. 
Threads can request access to the resource (decrementing the semaphore), and can signal that they have 
finished using the resource (incrementing the semaphore).


==

Deadlock

Deadlock describes a situation where two or more threads are blocked forever, waiting for each other. 

4 Conditions for deadlock:

Mutual Exclusion
Hold and Wait
Circular Wait
No Preemption

==

Virtual Memory

It maps memory addresses used by a program, called virtual addresses, into physical addresses in computer memory. Main storage, as seen by a process or task, appears as a contiguous address space or collection of contiguous segments. The operating system manages virtual address spaces and the assignment of real memory to virtual memory. 

Address translation hardware in the CPU, often referred to as a memory management unit or MMU, 
automatically translates virtual addresses to physical addresses. 


==

Trashing

Thrashing occurs on a program that works with huge data structures, as its large working set causes continual page faults that drastically slow down the system. Satisfying page faults may require freeing pages that will soon have to be re-read from disk. 
 
 
==

Page Fault 

An interrupt that occurs when a program requests data that is not currently in real memory. 
The interrupt triggers the operating system to fetch the data from a virtual memory and load it into RAM.


==

TLB

A translation lookaside buffer (TLB) is a memory cache that stores recent translations of 
virtual memory to physical addresses for faster retrieval.


==





===

OOM:
producer - consumer
1. allocating memory faster than GC 
2. don't even give GC the chance to collect garbage (allocate object in main and never used it)


HashTable vs HashMap:
HashTable is thread safe while HashMap is not. This makes HashMap better for non-threaded applications, as unsynchronized Objects typically perform better than synchronized ones.


JVM or Engineer:
Too low level shouldn't be concern by application engineer
GC is well tested and widely used so it is unlikely application engineers can write a better GC.
In general, whenever java libary support certain feature, the application engineer should rearly reinvent the wheel unless there is very specific goal. In terms of GC, the goal of GC is very general purpose, so it shouldn't be implemented by application engineers. 




def inPlaceReverseArray(arr):
    s, e = 0, len(arr)-1
    while s <= e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1
    return arr


test = [1,2]
print inPlaceReverseArray(test)


===
public class Main {
	public static void ReverseArray(int[] arr) {
		for(int i = 0; i < data.length / 2; i++) {
		    int temp = data[i];
		    data[i] = data[data.length - i - 1];
		    data[data.length - i - 1] = temp;
		}
	}

	public static void main(String[] args) {
		int[] arr = {1, 2, 3, 4, 5};
		ReverseArray(arr);
		for (int i = 0; i < arr.length; ++i) {
			System.out.println(arr[i]);
		}
	}
}

===



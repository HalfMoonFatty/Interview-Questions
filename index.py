Data Structures

    >> Array                        *61
    >> String                       *21
    >> Linked List                  *25
    >> Stack and Queue              *26
    >> Hash Table                   *26
    >> Heap                         *09
    >> Tree                         *56
    >> Trie                         *07
    >> Graph                        *27

Algorithms

    >> Bit Manipulations            *14
    >> Math                         *28
    >> Backtracking                 *20
    >> Sorting                      *17
    >> Searching                    *14
    >> Divide and Conquer           *08
    >> Greedy                       *07
    >> DP                           *44

Design                              *19

Data Structures

#################### Array ####################

>> 1D Array

    (M) 163. Missing Ranges
    (M) 228. Summary Ranges

    (E) 325. Maximum Size Subarray Sum Equals k
    (M) 209. Minimum Size Subarray Sum
    (H) 076. Minimum Window Substring
    (H) 239. Sliding Window Maximum
    (H) 030. Substring with Concatenation of All Words

>> Remove Dup

    (E) 026. Remove Duplicates from Sorted Array
    (M) 080. Remove Duplicates from Sorted Array II

    (E) 083. Remove Duplicates from Sorted List
    (M) 082. Remove Duplicates from Sorted List II

    (E) 027. Remove Element
    (E) 203. Remove Linked List Elements
    (E) 283. Move Zeroes

    (E) 028. Implement strStr()
    (H) 214. Shortest Palindrome

>> 2D Array

    (M) 048. Rotate Image
    (M) 054. Spiral Matrix
    (M) 059. Spiral Matrix II
    (M) 073. Set Matrix Zeroes
    (M) 289. Game of Life

>> Recursion

    (E) 153. Find Minimum in Rotated Sorted Array
    (H) 004. Median of Two Sorted Arrays
    (H) 295. Find Median from Data Stream
    (M) 306. Additive Number

>> 方形长方形系列

    (H) 084. Largest Rectangle in Histogram - stack
    (H) 085. Maximal Rectangle   - array hash table  dp stack
    (H) 164. Maximum Gap - sort
    (M) 221. Maximal Square  - dp

>> 进阶题

    (H) 135. Candy(Greedy)
    (H) 041. First Missing Positive (Tricky)
    (M) 268. Missing Number
    (H) 287. Find the Duplicate Number

>> 2 pointers

    (E) 344. Reverse String
    (E) 345. Reverse Vowels of a String
    (M) 151. Reverse Words in a String
    (M) 186. Reverse Words in a String II

    (M) 061. Rotate List
    (E) 189. Rotate Array

     (E) 349. Intersection of Two Arrays
     (E) 350. Intersection of Two Arrays II

>> Sum 类
    (E) 001. 2 Sum - HashTable
    (M)  167.  2 Sum II – Input array is sorted - 1)对撞指针 2) Binary Search
    (M) 015. 3 Sum - 难点去重
    (M) 016. 3 Sum Closest - 无需去重
    (M) 259. 3 Sum Smaller - 无需去重
    (M) 018. 4 Sum
    (H) LintCode k Sum - BackTracking / 3D DP
    (M) LintCode Triangle Count
    (M) 011. Container With Most Water
    (H)  042. Trapping Rain Water

>> Partition 类
    (E) 125. Valid Palindrome (Corner Cases / String Manipulation)
    (E) LintCode Partition-array
    (E) LintCode Partition Array by Odd and Even
    (E) LintCode Sort Letters by Case
    (M) 075. Sort Colors - 3 pointers (2 pointers: http://www.jiuzhang.com/solutions/sort-colors/)
    (E) 283. Move Zeros

>> 窗口类

    (E) 019. Remove Nth Node From End of List
    (E) 387. First Unique Character in a String
    (M) 209. Minimum Size Subarray Sum (2种模板）
    (H) 076. Minimum Window Substring （模板2）
    (M) 003. Longest Substring Without Repeating Characters (2种模板）
     (H) 159. Longest Substring with At Most K Distinct Characters （模板2）

>> 快慢类

    (E) 237. Delete Node in a Linked List
    (M) 141. Linked List Cycle
    (M) 142. Linked List Cycle II

>> 进阶题:好难啊

    * 非常有意思的 wiggle sort (*)
        (E) 283. Move Zeroes
        (M) 075. Sort Colors
        (M) 280. Wiggle Sort
        (M) 324. Wiggle Sort II
        (M) 148. Sort List
        (M) 251. Kth Largest Element in an Array

    * Sliding Window
        (H) 030. Substring with Concatenation of All Words
        (H) 239. Sliding Window Maximum


#################### String ####################

>> 基础题

    (E) 058. Length of Last Word
    (E) 038. Count and Say
    (E) 014. Longest Common Prefix
    (M) 271. Encode and Decode Strings
    (M) 297. Serialize and Deserialize Binary Tree

>>
    (E) 013. Roman to Integer
    (M) 012. Integer to Roman
    (H) 273. Integer to English Words
    (E) 246. Strobogrammatic Number
    (M) 247. Strobogrammatic Number II
    (H) 248. Strobogrammatic Number III

>> Zigzag Problem

    (E) 006. ZigZag Conversion
    (M) 103. Binary Tree Zigzag Level Order Traversal
    (M) 281. Zigzag Iterator

>>
    (M) 151. Reverse Words in a String I
    (M) 186. Reverse Words in a String II

>> Palindrome Problems — Manacher’s Algorithm

    * 基础题:
        (E) 266. Palindrome Permutation
        (M) 267. Palindrome Permutation II

    * 进阶题:
        (H) 005. Longest Palindromic Substring
        (H) 214. Shortest Palindrome
        (H) 336. Palindrome Pairs

#################### Linked List ####################

这类题没有什么特别难的，只是代码比较繁琐。常用技巧：dummy node

>> 基础题

    (E) 160. Intersection of Two Linked Lists
    (E) 203. Remove Linked List Elements
    (M) 086. Partition List (dummy head)
    (E) 019. Remove Nth Node From End of List — fast slow ptr
    (E) 206. Reverse Linked List I
    (M) 092. Reverse Linked List II
    (M) 156. Binary Tree Upside Down  (***)
    (E) 234. Palindrome Linked List
    (M) 143. Reorder List 一个链表拧麻花一样交替重组连接
    (M) 328. Odd Even Linked List  一个链表拆成两段，然后连接

>> Math

    (E) 067. Add Binary
    (M) 002. Add Two Numbers
    (M) 043. Multiply Strings
    (E) 066. Plus One

>> Marge / Merge Sort系列

    (E) 021. Merge Two Sorted Lists
    (H) 023. Merge k Sorted Lists  — Ugly Number II
    (E) 088. Merge Sorted Array
    (M) 148. Sort List
    (M) 244. Shortest Word Distance II
    Merge Sort Linked List (!!! 难 !!!)

    (M) 024. Swap Nodes in Pairs
    (H) 025. Reverse Nodes in k-Group

>>
    (M) 199. Binary Tree Right Side View
    (M) 116. Populating Next Right Pointers in Each Node
    (H) 117. Populating Next Right Pointers in Each Node II (** dummy node)

#################### Stack and Queue ####################

>> 基础题

    (E) 225. Implement Stack using Queues
    (E) 232. Implement Queue using Stacks

>> Stack

    (E) 020. Valid Parentheses
    (M) 071. Simplify Path
    (M) 341. Flatten Nested List Iterator
     (M) 385. Mini Parser
     (M) 388. Longest Absolute File Path

    (M) 224. Basic Calculator
    (M) 227. Basic Calculator II — 技巧但是没有高深算法
    (M) 150. Evaluate Reverse Polish Notation
    (H) 282. Expression Add Operators (!!! 好难啊!!!)
    (M) 241. Different Ways to Add Parentheses
    (H) 316. Remove Duplicate Letters (非常难，多种解法)

>> Stack and Shapes

    (H) 042. Trapping Rain Water
    (H) 218. The Skyline Problem
    (H) 084. Largest Rectangle in Histogram - stack
    (H) 085. Maximal Rectangle   - array hash table  dp stack
    (M) 221. Maximal Square  - dp
    (H) 164. Maximum Gap - sort

>>

    (E) 155. Min Stack
    (H) 239. Sliding Window Maximum (Heap)

>> Tree and stack

    (E) 144. Binary Tree Preorder Traversal
    (M) 094. Binary Tree Inorder Traversal
    (H) 145. Binary Tree Postorder Traversal
    (M) 173. Binary Search Tree Iterator
    (H) 272. Closest Binary Search Tree Value II
    (M) 255. Verify Preorder Sequence in Binary Search Tree
    (M) 331. Verify Preorder Serialization of a Binary Tree

>> Queue

#################### Hash Table ####################

>>
    (E) 359. Logger Rate Limiter
    (E) 362. Design Hit Counter
    (E) 299. Bulls and Cows (tricky 1-pass solution)
    (E) 242. Valid Anagram
    (E) 049. Group Anagrams
    (E) 249. Group Shifted Strings
    (E) 288. Unique Word Abbreviation
    (H) 149. Max Points on a Line - 题不难就是烦
    (M) 311. Sparse Matrix Multiplication

>>
    (E) 001. Two Sum
    (M) 015. 3 Sum
    (M) 016. 3 Sum Closest
    (M) 259. 3 Sum Smaller
    (M) 018. 4 Sum
    (M) 167. Two Sum II - Input array is sorted
    (E) 170. Two Sum III - Data structure design

>>
    (E) 205. Isomorphic Strings
    (E) 290. Word Pattern
    (H) 291. Word Pattern II

>>
    (E) 036. Valid Sudoku
    (H) 037. Sudoku Solver

>>
    (E) 243.Shortest Word Distance
    (M) 244.Shortest Word Distance II
    (M) 245.Shortest Word Distance III
    (M) 274. H-Index

>> 进阶题

    (E) 325. Maximum Size Subarray Sum Equals k
    (M) 209. Minimum Size Subarray Sum
    (H) 076. Minimum Window Substring

#################### Heap ####################

>>

    (M) 215. Kth Largest Element in an Array - 第K个：quick-selection
    (M) 347. Top K Frequent Elements - 前K个：heap; bucket sort;

    (M) 373. Find K Pairs with Smallest Sums - heap
    (M) 378. Kth Pairs Smallest Elements in a Sorted Matrix - heap
    (H) 023. Merge k Sorted Lists  — Ugly Number II

    (H) 295. Find Median from Data Stream - heap
    (H) 239. Sliding Window Maximum - Deque
    (H) 358. Rearrange String k Distance Apart - heap

    (H) 218. The Skyline Problem
    (M) 264. Ugly Number II
    (M) 313. Super Ugly Number
    (M) 253. Meeting Rooms II

#################### Tree ####################

>>
    (E) 100. Same Tree
    (E) 101. Symmetric Tree

     (M) 236. Lowest Common Ancestor of a Binary Tree
    (E) 235. Lowest Common Ancestor of a Binary Search Tree

    (E) 110. Balanced Binary Tree
    (E) 111. Minimum Depth of Binary Tree
    (E) 104. Maximum Depth of Binary Tree
    (M) 222. Count Complete Tree Nodes

>>
    (E) 257. Binary Tree Paths
    (E) 112. Path Sum
    (M) 113. Path Sum II
    (M) 129. Sum Root to Leaf Numbers
    (H) 124. Binary Tree Maximum Path Sum
    (M) 333. Largest BST Subtree
    (E) 226. Invert Binary Tree
    (M) 250. Count Univalue Subtrees

>>
    (E) 101. Symmetric Tree
    (E) 226. Invert Binary Tree
    (E) 102. Binary Tree Level Order Traversal
    (E) 107. Binary Tree Level Order Traversal II
    (M) 103. Binary Tree Zigzag Level Order Traversal
    (M) 314. Binary Tree Vertical Order Traversal

    (M) 199. Binary Tree Right Side View
    (M) 116. Populating Next Right Pointers in Each Node
    (H) 117. Populating Next Right Pointers in Each Node II (** dummy node)

>> Tree Traversal: in-order; pre-order; post-order; DFS; BFS;

    >>
        (M) 297. Serialize and Deserialize Binary Tree
        (M) 271. Encode and Decode Strings

    >>

        (E) 102. Binary Tree Level Order Traversal
        (E) 107. Binary Tree Level Order Traversal II
        (M) 103. Binary Tree Zigzag Order Traversal
        (M) 314. Binary Tree Vertical Order Traversal

>> Binary Tree

    (E) 144. Binary Tree Preorder Traversal
    (M) 094. Binary Tree Inorder Traversal
    (H) 145. Binary Tree Postorder Traversal
    (M) 255. Verify Preorder Sequence in Binary Search Tree
    (M) 331. Verify Preorder Serialization of a Binary Tree

    (M) 105. Construct Binary Tree from Preorder and Inorder Traversal
    (M) 106. Construct Binary Tree from Inorder and Postorder Traversal
    (M) 108.  Convert Sorted Array to Binary Search Tree
    (M) 109. Convert Sorted List to Binary Search Tree

>> BST

    (M)  098. Validate Binary Search Tree (inorder, lower_bound)
     (H)  099.  Recover Binary Search Tree (inorder / morris traversal)
    (M) 230. Kth Smallest Element in a BST (inorder traversal)
     (M) 173. Binary Search Tree Iterator (stack)
     (M) 255. Verify Preorder Sequence in Binary Search Tree (stack, lower_bound)

    (M) 285. Inorder Successor in BST
    (E) 270. Closest Binary Search Tree Value
    (H) 272. Closest Binary Search Tree Value II

    (M) 096. Unique Binary Search Trees
    (M) 095. Unique Binary Search Trees II

    (M) 241. Different Ways to Add Parentheses
    (M) 114. Flatten Binary Tree to Linked List (**不是trivial的recursion,很有意思的dfs,多看几遍)

>> 进阶题

    (H) 315. Count of Smaller Numbers After Self [ * Tricky]
    (H) 099. Recover Binary Search Tree [ * Algo] Morris Traversal方法遍历二叉树（非递归，不用栈，O(1)空间）

#################### Trie ####################

>> 基础题

    (M) 208. Implement Trie (Prefix Tree)
    (M) 211. Add and Search Word - Data structure design  — Tricky !!!
    (M) 079. Word Search I
    (M) 212. Word Search II
    (H) 336. Palindrome Pairs
    (M) 005. Longest Palindromic Substring
    (H) 214. Shortest Palindrome

#################### Graph ####################

>> Topological Sort

    (M) 323. Number of Connected Components in an Undirected Graph (无向图)
    (M) 207. Course Schedule
    (M) 210. Course Schedule II
    (H) 269. Alien Dictionary
    (M) 310. Minimum Height Trees (无向图)

>> Union Find

    (M) 323. Number of Connected Components in an Undirected Graph
    (M) 200. Number of Islands
    (H) 305. Number of Islands II
    (M) 261. Graph Valid Tree  (DFS)

>> DFS

    (M) 079. Word Search I  (DFS)
    (H) 212. Word Search II  (DFS + Trie)
    (H)  329. Longest Increasing Path in a Matrix

    (M) 133. Clone Graph
    (H) 138. Copy List with Random Pointer
    (M)332. Reconstruct Itinerary

>> BFS

    (M) 130. Surrounded Regions  (BFS: start from 4 boundaries)
    (M) 286. Walls and Gates     (Shortest Path: start from destination: Gates )
    (H) 317. Shortest Distance from All Buildings
    (H) 296. Best Meeting Point
    (M) 247. Strobogrammatic Number II
    (H) 248. Strobogrammatic Number III

>> Binary Indexed Tree / Segment Tree

    (H) 315. Count of Smaller Numbers After Self
    (H) 218. The Skyline Problem
    (M) 307. Range Sum Query - Mutable
    (H) 308. Range Sum Query 2D - Mutable
    (H) 327. Count of Range Sum (Divide and Conquer / BST)

** (M)  277.  Find the Celebrity

Algorithms

#################### Bit Manipulations ####################

>> 基础题

    (M) 136. Single Number I
    (M) 137. Single Number II
    (M) 260. Single Number III
    (M) 286. Missing Number
    (H) 287. Find the Duplicate Number

    (E) 007. Reverse Integer
    (E) 190. Reverse Bits
    (M) 191. Number of 1 Bits
    (H) 233. Number of Digit One
    (M) 338. Counting Bits
    (M) 201. Bitwise AND of Numbers Range

>> masks

    (M) 089. Gray Code
    (M) 318. Maximum Product of Word Lengths (masks)
    (M) CC150 Duplicate Chars(masks)

#################### Math ####################

大部分这种string (array) manipulation的题都是要考虑很多corner cases，很繁琐，但是不难

>> 基础题

    (E) 007. Reverse Integer
    (E) 008. String to Integer (atoi)
    (E) 171. Excel Sheet Column Number
    (E) 168. Excel Sheet Column Title
    (E) 009.Palindrome Number
    (E) 172. Factorial Trailing Zeroes
    (M) 166. Fraction to Recurring Decimal
    (M) 029. Divide Two Integers

>>
    (E) 258. Add Digits (brain teaser)
    (M) 201. Bitwise AND of Numbers Range
    (M) 050. Pow(x, n)
    (M) 069. Sqrt(x)
    (E) 231. Power of Two
    (E) 326. Power of Three
    (E) 342. Power of Four
    (E) 191. Number of 1 Bits
    (H) 233. Number of Digit One
    (M) 319. Bulb Switcher (brain teaser)

>>
    (E) 204. Count Primes
    (E) 202. Happy Number
    (E) 263. Ugly Number
    (M) 264. Ugly Number 2
    (M) 313. Super Ugly Number
    (M) 279. Perfect Squares
    (M) 343. Integer Break
    (M) 233. Number of Digit One
    (H) 065. Valid Number

>>
    (E) 223. Rectangle Area

#################### Backtracking ####################

    (M) 386. Lexicographical Numbers
    (M) 078. Subset
    (M) 090. Subset II

    (M) 077. Combinations
    (M) 039. Combination Sum
    (M) 040. Combination Sum II
    (M) 216. Combination Sum III
    (M) 254. Factor Combinations
    (M) 017. Letter Combinations of a Phone Number

    (M) 046. Permutations
    (M) 047. Permutations II
    (M) *031. Next Permutation
    (M) *060. Permutation Sequence


     (M)  131.  Palindrome Partitioning
    (M) *266. Palindrome Permutation
    (M) *267. Palindrome Permutation II

    (M) 247. Strobogrammatic Number II
    (H) 248. Strobogrammatic Number III

     (M) 093. Restore IP Addresses
    (M) 320. Generalized Abbreviation
    (H) 291. Word Pattern II
Word Break I
Word Break II

#################### Sorting ####################

>>
    (H) 056. Merge Intervals
    (H) 057. Insert Interval
    (E) 252. Meeting Rooms
    (M) 253. Meeting Rooms II

>>
    (H) 164. Maximum Gap
    (M) 179. Largest Number

    (M) 274. H-Index
    (H) 296. Best Meeting Point
    (H) 317. Shortest Distance from All Buildings

>> Merge Sort

    (E) 088. Merge Sorted Array
    (E) 021. Merge Two Sorted Lists
    (H) 023. Merge k Sorted Lists  — Ugly Number II
    (H) 315. Count of Smaller Numbers After Self

>>

    (M) 147. Insertion Sort List
    (M) 148. Sort List
    (M) 075. Sort Colors
    (M) 244. Shortest Word Distance II

#################### Searching ####################

>> Binary Search

    *
        (H) 033. Search in Rotated Sorted Array
        (M) 081. Search in Rotated Sorted Array II
        (M) 074. Search a 2D Matrix
        (M) 240. Search a 2D Matrix II
        (H) 302. Smallest Rectangle Enclosing Black Pixels
        (M) 153. Find Minimum in Rotated Sorted Array
        (H) 154. Find Minimum in Rotated Sorted Array II

    *
        (E) 349. Intersection of Two Arrays
        (E) 350. Intersection of Two Arrays II
        (E) 278. First Bad Version
        (M) 034. Search for a range;
        (M) 035. Search insert position 很像

        (M) 275. H-Index II
        (M) 300. Longest Increasing Subsequence

#################### Divide and Conquer ####################

    (M) 095. Unique Binary Search Trees II
    (H) 224. Basic Calculator
    (M) 227. Basic Calculator II
    (H) 282. Expression Add Operators  (!!! 非常难 !!!)
    (H) 312. Burst Balloons (!!! 非常难 !!!)
    (E) 169. Majority Element
    (M) 229. Majority Element II
    (H) 327. Count of Range Sum

#################### Greedy ####################

    (M) 055. Jump Game I
    (M) 045. Jump Game II
    (M) 134. Gas Station
    (M) 135. Candy
    (M) 330. Patching Array
    (H) 321. Create Maximum Number
    (H) 316. Remove Duplicate Letters (非常难，多种解法)

#################### DP ####################

所有DP原题，记住动态方程！！！
>> 一维 Array

    >> Fibonacci - 取或者不取

        (E) 070. Climb Stairs     dp[i] = dp[i-1] + dp[i-2]
        (M) 091. Decode Ways      dp[i] = dp[i-1] + dp[i-2] or dp[i] = dp[i-1]

        (E) 198. House Robber     dp[i] = max(dp[i-1], dp[i-2] + num[i-1])
        (M) 213.  House Robber II
        (M) 337. House Robber III res[0] = root.val + leftVals[1] + rightVals[1]
                                     res[1] = max(leftVals[0],leftVals[1]) + max(rightVals[0],rightVals[1])

        (E) 276. Paint Fence      dp[i] = (dp[i-2]+dp[i-1])*(k-1)
        (M) 256. Paint House
        (H) 265. Paint House II
        (M) 322. Coin Change
        (H) 321. Create Maximum Number
        (H) 312. Burst Balloons (!!! 非常难 !!!)
        (M) 338. Counting Bits (Math) dp[i] = dp[i / 2] + i % 2

    >>
        (E) 121. Best Time to Buy and Sell Stock
        (E) 122. Best Time to Buy and Sell Stock II
        (E) 123. Best Time to Buy and Sell Stock III
        (E) 188. Best Time to Buy and Sell Stock IV
        (M) 309. Best Time to Buy and Sell Stock with Cooldown

    >>
        (M) 053. Maximum Subarray
        (M) 152. Maximum Product Subarray
        (M) 238. Product of Array Except Self
        (M) 279. Perfect Squares
        (M) 343. Integer Break

    >>
        (M) 300. Longest Increasing Subsequence
        (M) 334. Increasing Triplet Subsequence
        (LintCode) Longest Increasing Subsequence 2D

    >> 一维 String

        (M) 092. Decode Ways   dp[i] = dp[i-1] + dp[i-2] or dp[i] = dp[i-1]
        (H) 139. Word Break
        (H) 140. Word Break II   (好难啊)

        (H) 087. Scramble String
        (H) 097. Interleaving String
        (H) 115. Distinct Subsequences
        (H) 132. Palindrome Partitioning II

        (M) 161. One Edit Distance (not DP)
        (H) 072. Edit Distance
        (H) 044. Wildcard Matching (基础题)
        (H) 010. Regular Expression Matching (进阶题)

>> 二维

    >>
    (M) 062. Unique Paths I
    (M) 063. Unique Paths II
    (M) 064. Minimum Path Sum
    (H) 174. Dungeon Game


    >>
    (M) 221. Maximal Square
    (H) 085. Maximal Rectangle


    >>
    303. Range Sum Query - Immutable
    304. Range Sum Query 2D - Immutable

>> 博弈类：

     (LintCode) Coins in a Line i
     (LintCode) Coins in a Line ii
     (LintCode) Coins in a Line iii
     375. Guess Number Higher or Lower II

#################### Design ####################

>>

    (H) 146. LRU Cache
    (E) 155. Min Stack
    (M) 173. Binary Search Tree Iterator
    (E) 232. Implement Queue using Stacks
    (M) 208. Implement Trie (Prefix Tree)
    (H) 297. Serialize and Deserialize Binary Tree
    (E) 225. Implement Stack using Queues
    (H) 295. Find Median from Data Stream
    (M) 284. Peeking Iterator
    (M) 211. Add and Search Word - Data structure design
    (E) 288. Unique Word Abbreviation
    (M) 251. Flatten 2D Vector
    (E) 170. Two Sum III - Data structure design
    (M) 281. Zigzag Iterator
    (M) 244. Shortest Word Distance II
    (M) 341. Flatten Nested List Iterator
    (E) 346. Moving Average from Data Stream
    (M) 348. Design Tic-Tac-Toe
    (M) 355. Design Twitter

#################### Other ####################

>> Palindrome Series

    (E) 266. Palindrome Permutation
    (M) 267. Palindrome Permutation II
    (M) 005. Longest Palindromic Substring
    (H) 214. Shortest Palindrome
    (H) 336. Palindrome Pairs

    (E) 009. Palindrome Number
    (E) 125. Valid Palindrome
    (E) 234. Palindrome Linked List
    (M) 131. Palindrome Partitioning
    (H) 132. Palindrome Partitioning II

>> Permutaion Series

    (M) 031. Next Permutation
    (M) 046. Permutations
    (M) 047. Permutations II
    (M) 060. Permutation Sequence
    (M) 266. Palindrome Permutation
    (M) 267. Palindrome Permutation II

>> Combinations Series

    (M) 017. Letter Combinations of a Phone Number
    (M) 077. Combinations
    (M) 039. Combination Sum
    (M) 040. Combination Sum II
    (M) 216. Combination Sum III
    (M) 254. Factor Combinations

>> Parentheses Series

    (E) 020. Valid Parentheses
    (M) 022. Generate Parentheses
    (H) 032. Longest Valid Parentheses
    (H) 301. Remove Invalid Parentheses (BFS/DFS)
    (M) 247. Strobogrammatic Number II (DFS)
    (H) 248. Strobogrammatic Number III (BFS)

>> Iterator Series

    (M) 173. Binary Search Tree Iterator
    (M) 281. Zigzag Iterator
    (M) 284. Peeking Iterator
    (M) 251. Flatten 2D Vector
    (M) 341. Flatten Nested List Iterator

>> Flatten Series

    (M) 114. Flatten Binary Tree to Linked List
    (M) 251. Flatten 2D Vector
    (M) 341. Flatten Nested List Iterator

>> Game

    (E) 292. Nim Game     — BrainTeaser
    (E) 293. Flip Game     — String
    (M) 294. Flip Game II  — Backtracking

CareerCup
Part 1: 1, 2, 3, 4, 5, 6
Part 2: 7, 8, 9
Part 3: 10, 11, 12

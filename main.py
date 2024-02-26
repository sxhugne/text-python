##
#**#

#XX#
#   i的阶乘
# count = 1
# i = int(input("输入数："))
# for x in range(1,i+1):
#     count *= x
# print(count)


#XX#
# #求素数
# i = int(input("输入数"))
# for x in range(2,i+1):
#     for y in range(2,x+1):
#         if x%y == 0:
#             break
#         elif y == x-1:
#             print(x)


#圆面积
# import math
#
# r = int(input("圆半径："))
#
# area = math.pi * r * r
# print(area)


# #从列表中移除多个元素
# li = [1,3,5,7,9,11,13,15,17]
# move = [3,7,11]
#
# for i in move:
#     li.remove(i)
#
# print(li)


#**#列表元素去重
#NO.1
# list_1 = [10, 20, 30, 10, 30]
#
# list_1 = set(list_1) #列表转集合
# list_1 = list(list_1)
# print(list_1,type(list_1))

#NO.2
# list_1 = [10, 20, 30, 10, 30]
# list_un = []
#
# for x in list_1:          #**#
#     if x not in list_un:
#         list_un.append(x)
#
# print(list_un)


#列表排序 reverse(反向)
# a = [4,15,2,74,5,7,8,1,2,4,56,4,8,2]
# b = sorted(a)  #得到新列表
# a.sort()       #修改源列表
# print(a)
# print(b)
##降序
# a.sort(reverse = True)
# print(a)


#读取文件排序 文件名：text_1
# stu = []
# with open("D:/python/python.project/practice_1/text_1","r",encoding = "UTF-8") as f: #with as 会自动调用close()关闭文件
#     for x in f.readlines():
#         x = x.split("，") #从字符串 x 中切片
#         x[0] = int(x[0])
#         x[2] = int(x[2].replace("\n",""))
#         stu.append(x)
#
#
# stu.sort(key=lambda x: x[2])
# for x in stu:
#     print(x)


# 读取文件计算最高分和最低分 文件名：text_1
# score = set()   #空集合定义,score = {}定义为空字典   #**#
#
# with open("D:/python/python.project/practice_1/text_1","r",encoding = "UTF-8") as f: #with as 会自动调用close()关闭文件
#     for x in f.readlines():
#         score.add(int(x.split("，")[2].strip()))
# NO.1
#  score = list(score)  #集合（Set）是无序的，并没有直接的方法对集合进行排序。如果你希望对集合中的元素进行排序，可以将集合转换为列表，对列表进行排序，然后再将排序后的列表转回集合。
#  score.sort()
#  print(f"max = {score[1]},min = {score[-1]}")
#
#  NO.2
# _max = max(score)
# _min = min(score)
# print(f"max = {_max},min = {_min}")


#**#给定两个字符串 s1 和 s2,编写一个程序,确定其中一个字符串的字符重新排列后,能否变成另一个字符串
# s1 = "d我aws"
# s2 = "daws我"
# print(sorted(s1) == sorted(s2))


#翻转字符串
# s = input("字符串:")     #**#相对于scanf

# NO.1
# print(s[::-1])

# # NO.2
# result = []
# for x in s:
#     result.append(x)
#
# result = result[::-1]
# print("".join(result))


#列表[1,2,3,4,5]，请使用map函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数
#map(方法,列表)    用于将一个函数应用于迭代器（例如列表）的每个元素，返回一个新的迭代器（映射后的结果）
# NO.1
# a = [1,2,3,4,5]
# a = map(lambda x:x*x,a)       #**#
# print(a)


#选择排序
#
# def select(arr):
#     for i in range(len(arr)-1):   #排列次数
#         tmp = i
#         for j in range(i,len(arr)):
#             if arr[tmp] > arr[j]:
#                 tmp = j
#         if tmp != i:
#             arr[tmp],arr[i] = arr[i],arr[tmp]       #**#替换两个数
#         print(arr)
#     return arr
#
# a = [13,84,82,48,46,46,98,32,138,782,75,75,219,35]
# print(select(a))


#快速排序
# def select_partition(arr,left,right):
#     while left < right:
#         while left < right and arr[right] >= arr[left]:
#             right-=1
#         arr[right],arr[left] = arr[left],arr[right]
#         while left < right and arr[right] >= arr[left]:
#             left+=1
#         arr[right],arr[left] = arr[left],arr[right]
#     return left
#
# def select_quick(arr,left,right):
#     if left<right:
#         mid = select_partition(arr,left,right)
#         select_quick(arr,left,mid-1)
#         select_quick(arr,mid+1,right)
#
#
# a = [130,84,82,48,46,46,98,32,138,782,75,75,219,35]
# select_quick(a,0,len(a)-1)
# print(a)

#位运算加法
# def sum(a,b):
#     if b == 0:
#         return a
#     else:
#         return sum(a^b,(a&b)<<1)
#
# print(sum(10,4))


# 堆排序
# def select_sift(arr,low,high):   #大根堆支点向下调整函数     #大根堆改小根堆：最后两大于号改为小于号
#     """
#     :param arr:列表
#     :param low:堆顶
#     :param high:堆的最后一个元素
#     """
#     i = low
#     j = 2 * i + 1   #起始为左侧子支点
#     while j <= high:    #j有位置
#         if j+1 < high and arr[j] < arr[j+1]:    #右侧子支点存在 and 如果左侧子支点小于右侧子支点
#             j = j+1                             #j指向右侧子支点
#         if arr[i] < arr[j]:                     #子支点与父支点比较
#             arr[i],arr[j] = arr[j],arr[i]
#             i = j                               #向下看一层
#             j = 2 * i + 1
#         else:
#             break
#
# def heap_sort(arr):
#     """
#     :param arr:列表
#     :param len:数组长
#     """
#     for i in range((len(arr)-2) // 2,-1,-1):   #len-2 = 下标-1     #建堆
#         select_sift(arr,i,len(arr)-1)
#
#     for i in range(len(arr)-1,-1,-1):   #排序
#         arr[i],arr[0] = arr[0],arr[i]
#         select_sift(arr,0,i-1)      #x-1:新的堆底
#
# import random
# arr = [i for i in range(1,20)]  #**# arr == list(range(1,20)
# random.shuffle(arr) #**#打乱序列
# print(arr)
#
# heap_sort(arr)
# print(arr)

#堆排序内置模块(heapq) q->queue 优先队列
# heapify(iterable): 将可迭代对象转换为小根堆。
# heappush(heap, item): 将一个元素添加到堆中。
# heappop(heap): 弹出并返回堆中最小的元素。
# heapreplace(heap, item): 弹出并返回堆中最小的元素，然后将新元素添加到堆中。
# nlargest(n, iterable): 返回可迭代对象中最大的 n 个元素。
# nsmallest(n, iterable): 返回可迭代对象中最小的 n 个元素。


# #归并排序(归并：假设有两段有序，将其合为一段有序)
#     #递归思路：
#     # 分解:将列表越分越小,直至分成一个元素。
#     # 终止条件：一个元素是有序的。
#     # 合并：将两个有序列表归并，列表越来越大。
# def merge(arr,low,mid,high):    #归并函数
#     i = low       #**#很重要，防止后面源列表替换时low和high发生改变
#     j = mid+1     #**#
#     arr_tmp = []
#     while i <= mid and j <= high:   #两边都有数
#         if arr[i] < arr[j]:
#             arr_tmp.append(arr[i])
#             i += 1
#         if arr[i] > arr[j]:
#             arr_tmp.append(arr[j])
#             j += 1
#     while i <= mid:
#         arr_tmp.append(arr[i])
#         i+=1
#     while j <= high:
#         arr_tmp.append(arr[j])
#         j+=1
#     arr[low:high+1] = arr_tmp       #**#替换下标为low到high的元素
#
# def merge_sort(arr,low,high):
#     if low < high:      #至少有两个元素
#         merge_sort(arr,low,(low+high)//2)
#         merge_sort(arr,(low+high)//2 + 1,high)
#         merge(arr,low,(low+high)//2,high)
#
# import random
# arr = list(range(1,20))
# random.shuffle(arr)
# print(arr)
# merge_sort(arr,0,len(arr)-1)
# print(arr)


#希尔排序
# def insert_sort(arr,gap):
#     for i in range(gap,len(arr)):
#         tmp = arr[i]
#         while i - gap >= 0 and arr[i - gap] > tmp:  #i - gap若写为i 会指向-1,即与最尾部的数相比较
#             arr[i] = arr[i - gap]
#             i = i - gap
#         arr[i] = tmp
#
# def shell_sort(arr):
#     d = len(arr) // 2
#     while d >= 1:
#         insert_sort(arr,d)
#         d //= 2
#
# import random
# arr = list(range(1,20))
# random.shuffle(arr)
# print(arr)
# shell_sort(arr)
# print(arr)


#计数排序
# def count_sort(li,count_max = 100):
#     """
#     :param li:
#     :param count_max: li中最大不能超过的数
#     :return:
#     """
#     count = [0 for _ in range(count_max + 1)]   # 创建了一个创建一个包含100个元素的列表,每个元素都是0,_ 表示不需要使用
#     for i in li:
#         count[i] += 1
#     li_tmp = []
#     for i,val in enumerate(count):  #**#返回(下标,元素) val->value
#         for x in range(val):
#             li_tmp.append(i)
#     return li_tmp
#
# import random
# arr = list(range(1,20))
# random.shuffle(arr)
# print(arr)
# arr = count_sort(arr)
# print(arr)

#############################################################
#桶排序
# def bucket_sort(li,n=100,max_num=10000):
#     """
#     :param li:
#     :param n:桶的个数
#     :param max_num:li里最大不能超过的数
#     :return:
#     """
#     buckets = [[] for _ in range(max_num)] #创建桶
#     for var in li:
#         i = min(var // (max_num // n),n-1) #选择桶
#         buckets[i].append(var)
#         for j in range(len(buckets[i])-1,0,-1):
#             if buckets[i][j] < buckets[i][j-1]:
#                 buckets[i][j-1],buckets[i][j] = buckets[i][j],buckets[i][j-1]
#             else:       #break 可不加
#                 break
#     sorted_li = []
#     for buc in buckets:
#         sorted_li.extend(buc)  # 用于将另一个列表中的所有元素添加到当前列表的末尾。
#     return sorted_li
#
# import random
# arr = list(range(1,200))
# random.shuffle(arr)
# print(arr)
# arr = bucket_sort(arr)
# print(arr)

#############################################################
#基数排序
# def radix_sort(li):
#     max_num = max(li)
#     it = 0
#     while 10 ** it <= max_num:
#         buckets = [[] for _ in range(10)]
#         for val in li:
#             # 798 it=1 987//10->98 98%10->8;  987 it=1 987//100->9 9%10->8;
#             digit = (val // 10 ** it ) % 10
#             buckets[digit].append(val)
#         li.clear()
#         for buc in buckets:
#             li.extend(buc)
#         it += 1
#
# import random
# arr = list(range(1,200))
# random.shuffle(arr)
# print(arr)
# radix_sort(arr)
# print(arr)


#############################################################
#1.text_1
# 给两个字符串s和t，判断t是否为s的重新排列后组成的单词
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# def text_1(s,t):
#     li_s = []
#     li_t = []
#     for i in s:
#         li_s.append(i)
#     for i in t:
#         li_t.append(i)
#     for j in t:
#         for x in range(len(li_s)):
#             if j == li_s[x]:
#                 li_s.remove(j)
#                 li_t.remove(j)
#                 break
#
#     if len(li_s) == 0 and len(li_t) == 0:
#         print("true")
#     else:
#         print("falue")
# text_1("abcc","cbac")

#solution_1
# def isanagram_1(s,t):
#     ss = list(s)
#     tt = list(t)
#     ss.sort()   #ss.sort(reverse=True)  升序改降序
#     tt.sort()   #sorted(ss)   返回一个排序好的新列表, 不改变原列表
#     return ss == tt


#solution_2
# def isanagram_2(s,t):
#     dict_s = {}
#     dict_t = {}
#     for ch in s:
#         dict_s[ch] = dict_s.get(ch,0) + 1   #get() 会在字典中查找指定的键 key，如果找到了该键，则返回对应的值；
#                                             #         如果键不存在，则返回默认值 ，或者返回 None（如果没有提供默认值）
#     for ch in t:
#         dict_t[ch] = dict_t.get(ch,0) + 1
#     return dict_s == dict_t
##############################################################
# #2.给定一个m*n的二维列表,查找一个数是否存在。
#              1.每一行的列表从左到右已经排序好
#              2.每一行第一个数比上一行最后一个数大

#二分查找
# def search(li,target):
#     h = len(li)       #一维列表个数
#     if h == 0:
#         return False
#     w = len(li[0])    #一维列表元素个数
#     if w == 0:
#         return False
#     left = 0
#     right = h * w - 1
#     while left <= right:            #**#
#         mid = (left + right) // 2
#         i = mid // w
#         j = mid % w
#         if li[i][j] == target:
#             return True
#         elif li[i][j] < target:
#             right = mid - 1
#         elif li[i][j] > target:
#             left = mid + 1
#     else:
#         return False
# # arr = [[1,2,3], [4,5,6],[7,8,9]]      #  print(arr[0])   ->  [1,2,3]
# # print(len(arr))                       # print(arr[1])   ->  [4,5,6]
# #                                       #  print(len(arr)) ->   3


##############################################################
#3.给定一个列表和一个整数,设计算法找到两个数的下标，使得两个数之和为给定的整数。
# 保证肯定仅有一个结果。例如,列表[1,2,5,4]与目标整数3, 1+2=3,结果为(0,1).

# def twoSum(li,target):
#     for i,val in enumerate(li):
#         x = target - li[i]
#         left = i+1
#         right = len(li) - 1
#         while left <= right:
#             mid = (right + left) // 2
#             if li[mid] == x:
#                 return (i,mid)
#             elif li[mid] < x:
#                 left = mid + 1
#             elif li[mid] > x:
#                 right = mid - 1
#     return None
#
# li = list(range(1,100,3))
# a = twoSum(li,20)
# print(a)

##############################################################
# #栈
#
# class Stack:            #定义栈
#     def __init__(self):
#         self.stack = []
#
#     def push(self,element):        #加入元素
#         self.stack.append(element)
#
#     def pop(self):          #移除并返回栈顶的元素。栈顶指的是最后一个被压入栈的元素。
#         return self.stack.pop()
#
#     def get_top(self):          #确认栈顶元素
#         if len(self.stack) > 0:
#             return self.stack[-1]
#         else:
#             return None
#
#     def is_empty(self):         #判断栈是否为空
#         return len(self.stack) == 0
#
#
# def brace_match(str):         #栈确认括号是否匹配
#     stack = Stack()         #创建栈
#     match = {')':'(',']':'[','}':'{'}
#     for ch in str:
#         if ch in {'(','[','{'}:     #**#    如果ch为{}中的任何一个   ()\{}\[]都可以
#             stack.push(ch)
#         else:
#             if stack.is_empty():        #栈为空
#                 return False
#             elif stack.get_top() == match[ch]:      #括号匹配
#                 stack.pop()
#             else:       #括号不匹配
#                 return False
#     if stack.is_empty():        #括号一一匹配
#         return True
#     else:
#         return False
#
# li = '[{[{({})}]}]'
# print(brace_match(li))

##############################################################
#队列——环形队列
# class Queue:
#     def __init__(self,size = 100):
#         """
#         :param size: 环形队列大小
#         """
#         self.queue = [0 for _ in range(size)]
#         self.rear = 0   #对尾指针
#         self.front = 0  #对首指针
#
#     def push(self,element):
#         if not self.is_filled():
#             self.rear = (rear + 1) % self.size
#             self.queue[rear] = element
#         else:
#             raise IndexError("Queue is filled")  # 手动报错
#
#     def pop(self):
#         if not self.is_empty():     #**#
#             self.front = (self.front + 1) % self.size
#             return self.queue[front]
#         else:
#             raise IndexError("Queue is empty")      #手动报错
#
#     def is_empty(self):     #判断队空
#         return self.front == self.rear
#
#     def is_filled(self):    #判断队
#         return self.front == (self.rear + 1) % self.size

##############################################################
#内置python队列模块——双向队列
#
# from collections import deque
#
# # 创建一个双端队列对象
# d = deque()           #**# deque(elements,n)  n表示队列的长度，n为0或不加n则队列不限制长度
                             #队列满时再添加元素，队首元素将被弹出
#
# # 在队列尾部插入元素
# d.append(1)
# d.append(2)
#
# # 在队列头部插入元素
# d.appendleft(0)
#
# # 从队列头部弹出元素
# print(d.popleft())  # 输出: 0
#
# # 从队列尾部弹出元素
# print(d.pop())  # 输出: 2
#
# # 输出队列中的元素
# print(d)  # 输出: deque([1])
# print(type(d))  #输出: <class 'collections.deque'>

##############################################################
# #栈和队列的应用——迷宫问题
# 回溯法
#
# 思路:从一个节点开始,任意找下一个
# 能走的点,当找不到能走的点时,退回
# 上一个点寻找是否有其他方向的点。
#
#使用栈存储当前路径

# maze = [
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],     #迷宫
#         [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#         [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#         [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
#         [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#         [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#         [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
#         [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]
#
# def maze_path(x1,y1,x2,y2,maze): #1起点  2终点
#     stack = []  #栈：存储岔路口
#     stack.append((x1,y1))
#
#     dirs = [
#         lambda x, y: (x + 1, y),     #lambda不用写return
#         lambda x, y: (x - 1, y),
#         lambda x, y: (x, y + 1),
#         lambda x, y: (x, y - 1)
#     ]
#
#     while len(stack) > 0:
#         curNode = stack[-1]    #当前地块
#         if curNode[0] == x2 and curNode[1] == y2:    #到达终点
#             for p in stack:
#                 print(p)
#             print("有路")
#             return True
#
#         for dir in dirs:        #四周地块状况
#             nextNode = dir(curNode[0],curNode[1])       #下一地块
#             if maze[ nextNode[0] ] [ nextNode[1] ] == 0:    #该地块能走
#                 stack.append(nextNode)                      #注意x,y不表示x轴y轴,(x,y) -> mize[x][y]
#                 maze[ nextNode[0] ] [ nextNode[1] ] = 2     #标记为已走过
#                 break
#         else:
#         #    maze[ nextNode[0] ] [ nextNode[1] ] = 2     #标记为已走过
#             stack.pop()
#     else:
#         print("没有路")
#         return False
#
# maze_path(1,1,8,8,maze)

##############################################################
# #队列———广度优先搜索
#
# maze = [
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],     #迷宫
#         [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#         [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#         [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
#         [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
#         [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#         [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#         [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
#         [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]
#
# from collections import deque
#
# def print_r(path):
#     curNode = path[-1]
#     real_path = []
#     while not curNode[2] == -1:     #回到起点
#         real_path.append(curNode[0:2])
#         curNode = path[curNode[2]]
#
#     real_path.append(curNode[0:2])     #添加起点
#     real_path.reverse()         #终点到起点  -> 起点到终点
#     return real_path
#
# def maze_path_queue(x1,y1,x2,y2,maze):
#     dirs = [
#             lambda x, y: (x + 1, y),     #lambda不用写return
#             lambda x, y: (x - 1, y),
#             lambda x, y: (x, y + 1),
#             lambda x, y: (x, y - 1)
#         ]
#     queue = deque()
#     queue.append((x1, y1, -1))
#     maze[x1][y1] = 2
#     path = []       #记录出队节点的下标
#     while len(queue) > 0:
#         curNode = queue.popleft()       #弹出队首
#         path.append(curNode)
#
#         if curNode[0] == x2 and curNode[1] == y2:       #轮到重点
#             path = print_r(path)            #自定义函数:回溯寻找原路
#             print("有路")
#             print(path)
#             return True
#
#         for dir in dirs:    #dir 返回元组（x,y)
#             nextNode = dir(curNode[0], curNode[1])
#             if maze[ nextNode[0] ] [ nextNode[1] ] == 0:
#                 queue.append( (nextNode[0], nextNode[1], len(path)-1) )   #(x, y, 母节点在path里的下标 )
#                 maze[ nextNode[0] ][ nextNode[1] ] = 2     #节点已走
#     else:
#         print("没有路")
#         return False
#
# maze_path_queue(1,1,8,8,maze)

##############################################################
#链表
# class Node:     #定义节点
#     def __init__(self,item):
#         self.item = item
#         self.next = None
#
# # def create_linklist_head(li):        #创建链表(头插法)
# #     head = Node(li[0])               #[1,2,3] -> 3 - 2 - 1
# #     for element in li[1:]:  #从下标1开始
# #         node = Node(element)
# #         node.next = head
# #         head = node
# #     return head
# #
# # lk = create_linklist_head([1,2,3])
# # print(lk.item)  # ->print(3)
# # print(lk.next.item) # ->print(2)
#
# def create_linklist_tail(li):        #创建链表(尾插法)
#     head = Node(li[0])               #[1,2,3] -> 1 - 2 - 3
#     tail = head
#     for element in li[1:]:  #从下标1开始
#         node = Node(element)
#         tail.next = node
#         tail = node
#     return head
#
# lk = create_linklist_tail([1,2,3])
# print(lk.item)
# print(lk.next.item)


#二叉树搜索、
# 二叉搜索树是一颗二叉树且满足性质：设x是二叉树的一个节点。
# 如果y是x左子树的一个节点，那么y.key <x.key;
# 如果y是x右子树的一个节点，那么y.key <x.Key;key > x.key。

class BiTreeNode:   #二叉树节点
    def __init__(self, data):
        self.data = data
        self.lchild = None  #左节点
        self.rchild = None  #右节点
        self.parent = None  #父节点

class BST:  #二叉树
    def __init__(self, li = None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def query_no_rec(self, val):    #查找val
        tmp = self.root             #教程没有，自己写的
        while tmp:
            if val == tmp.data:
                return tmp
            elif val < tmp.data:
                tmp = tmp.lchild
            elif val > tmp.data:
                tmp = tmp.rchild
        return False


    def insert(self, node, val):    #插入节点函数(递归法)
        if not node:
            node = BiTreeNode(val)
        elif val <= node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):   #插入节点函数(非递归法)
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val <= p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return

    #三种遍历法
    def pre_order(self, root):       #前序遍历
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self,root):        #中序遍历 #能排序
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    def post_order(self,root):      #后序遍历
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

    def __remove_node_1(self, node):    #普通方法[ abc() ]可以随时通过类的实例或类本身调用，
                                        #而特殊方法[ __abc() ]通常由解释器在特定情况下自动调用，不需要手动调用。
        # 情况1：node无孩子
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:  #node是它父亲的左孩子
            node.parent.lchild = None
        else:                           #node是它父亲的右孩子
            node.parent.rchile = None

    def __remove_node_21(self, node):
        # 情况2：node只有一个左孩子
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:    #node是它父亲的左孩子
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:                               #node是它父亲的右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况2：node只有一个右孩子
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.parent.lchild:    #node是它父亲的左孩子
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:                               #node是它父亲的右孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent



    def delect(self, val):       # 删除节点函数
        if self.root:     #不是空树
            node = self.query_no_rec(val)
            if not node:        #val不存在
                return False
            if not node.lchild and not node.rchild:     #没有孩子
                self.__remove_node_1(node)
            elif not node.rchild:           #只有左孩子
                self.__remove_node_21(node)
            elif not node.lchild:           #只有右孩子
                self.__remove_node_22(node)
            else:
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

# tree = BST()
# tree.root = tree.insert(tree.root,2)
# tree.root = tree.insert(tree.root,3)
# tree.in_order(tree.root)


# li = [2,7,5,55,9,3,4,66,7,5,11,6]
# tree = BST(li)
# tree.in_order(tree.root)
# tree.delect(4)
# print()
# tree.in_order(tree.root)


#AVL树(平衡二叉树)   使用了上面的二叉树函数  AVL树一般不插入树中已有的元素    ## 未完成
class AVLNode(BiTreeNode):      #此AVL树的平衡因子： bf = left - right
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0

class AVLTree():
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, a):               #左旋     RR
        """
        :param a: 平衡因子出范围的节点
        :param b:  a的右节点
        :return: 返回整理好的节点接回源根
        """
        b = a.rchild
        if b.lchild:
            b_l_tmp = b.lchild       #**#传的是c.lchild的地址
            a.rchild = b_l_tmp
            b_l_tmp.parent = a

        b.lchild = a
        a.parent = b

        a.bf = 0
        b.bf = 0
        return b

    def rotate_right(self, a):               #右旋    LL
        """
        :param a: 平衡因子出范围的节点
        :param b: a的左节点
        :return a: 返回整理好的节点接回源根
        """

        b = a.lchild
        if b.rchild:
            a.lchild = b.rchild
            b.rchild.parent = a

        b.rchild = a
        a.parent = b

        a.bf = 0
        b.bf = 0
        return a

    def rotate_left_right(self, a):
        b = a.lchild
        c = b.rchild
        a.lchild = rotate_left(b)
        rotate_right(a)
        if b.right == None:
            a.bf = 0
            b.bf =1
            c.bf = 0
        else:
            a.bf = -1
            b.bf = 0
            c.bf = 0

    def rotate_right_left(self, a):
        b = a.rchild
        c = a.lchild
        a.rchild = rotate_right(b)
        rotate_left(a)
        if b.left == None:
            a.bf = 0
            b.bf = -1
            c.bf = 0
        else:
            a.bf = 1
            b.bf = 0
            c.bf = 0

        def Tree_high(Node):        #节点处树高
            if Node == None:
                return None
            high_l = Tree_high(Node.lchild)
            high_r = Tree_high(Node.rchild)
            return max(high_l, high_r) + 1



    def insert_no_rec(self, val):
        p = self.root
        if not p:   #空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    node = p.lchild     #node: 插入的节点
                    break
            if val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break

        while node.parent:
            if node.parent.lchild == node:  #插入为左边
                pass

            else:       #插入为左边
                pass


#########################################################
# #钢条切割
# 某公司出售钢条，出售价格与钢条长度之间的关系如下表：
# 长度i   0 1 2 3 4 5  6  7  8  9  10
# 价格pi  0 1 5 8 9 10 17 17 20 24 30
# 问题：现有一段长度为n的钢条和上面的价格表，求切割钢条方案，使得总收益最大。

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]    #价格表

def cur_rod_recurision(p, n):       #求长度为n的钢条的收益最大值
    """
    :param p: 价格列表
    :param n: 钢条长度
    :return:  收益
    """
    if n == 0:      #长度为零
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            pass


#########################################################
# #辗转相除法求最大公因数
# def das(a,b):
#     if b == 0:  #除数为0
#         return a
#     else:
#         return das(b,a%b) #被除数改为余数，除数改为余数
#
# print(das(6,8))

#########################################################
#回溯算法   最好抽象为树形结构来思考

# #NO.1-1 列表里全部的无序的3个不同数的组合
# def back(li, li_two, index, x = []):          index: 控制树形结构的深度
#     if len(x) >= 3:
#         li_two.append(x[:])     #**#在 Python 中，当你执行 y.append(x) 时，实际上是将 x 的引用添加到了 y 中，而不是将 x 的值复制到 y 中。因此，如果之后你修改了 x，y 中的值也会相应地改变，因为它们指向的是同一个对象。
#         return                      #如果你想要在修改 x 后 y 的值不变，你需要确保 y 中添加的是 x 的副本而不是引用。可以使用切片操作 y.append(x[:]) 来添加 x 的浅拷贝（shallow copy）到 y 中。
#     for val in li[index:]:
#         x.append(val)
#         back(li, li_two, index + 1, x)
#         #li_two.append(x)
#         x.pop()
#         index += 1
#     return li_two
#
# li = [1,2,3,4,5]
# li_two = []
# back(li, li_two, 0)
# print(li_two)


# NO.1-2 列表里全部的无序的3个不同数的组合(含剪枝操作)
# def back(li, li_two, index, x = []):
#     if len(x) >= 3:
#         li_two.append(x[:])     #**#在 Python 中，当你执行 y.append(x) 时，实际上是将 x 的引用添加到了 y 中，而不是将 x 的值复制到 y 中。因此，如果之后你修改了 x，y 中的值也会相应地改变，因为它们指向的是同一个对象。
#         return                      #如果你想要在修改 x 后 y 的值不变，你需要确保 y 中添加的是 x 的副本而不是引用。可以使用切片操作 y.append(x[:]) 来添加 x 的浅拷贝（shallow copy）到 y 中。
#     for val in li[index:]:
#         if len(li[index:]) < 3 - len(x):    #剪枝操作: 在回溯算法中，剪枝操作是一种用于减少搜索空间的技术，通过提前判断某些分支不可能达到最优解，从而避免不必要的搜索。
#             return                          #这可以大大提高算法的效率。剪枝操作通常基于一些条件或者限制，如果当前搜索路径不满足这些条件或限制，则可以提前终止该路径的搜索。
#         x.append(val)
#         back(li, li_two, index + 1, x)
#         #li_two.append(x)
#         x.pop()
#         index += 1
#     return li_two
#
# li = [1,2,3,4,5]
# li_two = []
# back(li, li_two, 0)
# print(li_two)
#


#NO.2   组合总和(数字不重复)
# k = 3, n = 9  -> [1,2,6] [1,3,5] [2,3,4]

def find(li_range, k, target, index, li_tmp, li_save = [] ):
    if len(li_tmp) == k:
        pass


li_range = [x for x in range(1,11)]     #数字范围


#########################################################
# Python语句中一般以新行作为语句的结束符,可以使用斜杠（\）将一行的语句分为多行显示
# total = 1 + \ #**#
#         2 + \
#         3
#
# print(total)

# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
#
# days = ['Monday', 'Tuesday', 'Wednesday',
#         'Thursday', 'Friday']


#########################################################
# li = [1,2,3,4,5]
# li_two = []
# x = []
# for i in li:
#     for j in li:
#         x.append(j)
#     li_two.append(x)
#     print(li_two)
#     x.clear()
# print(li_two)
#打印结果       #**#添加的是地址，相当于链表，需要在每次循环开始时创建一个新的空列表 x，而不是在循环结束后清空它。
# [[1, 2, 3, 4, 5]]
# [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
# [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
# [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
# [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
# [[], [], [], [], []]











学习笔记

学习技巧：
  不要死磕，反复练习。
  COPY和掌握优秀的题解是必要的。
  自顶而下的思考和解题方式。
  
Data Structures are created to serve different algorithms. Need to practice more to better understand how they are used. 

Queue - 
  Queue class initiate a deque as self.queue and operations borrowed from deque
  LiFoQueue is just a stack
  PriorityQueue is heapq

Priority Queue -
  In python it is called heapq (heap queue). And by default it maintains the smallest number. Thread safe
  APIs: heappush, heappop, heappushpop, heapify, heapreplace, merge, nlargest, nsmallest
  Implementation: 
    It uses a list to host all the elements. All elements meet heap[k] <= heap[2*k+1] and heap[k] < heap[2*k+2]
    For the elements that have the same values it reserves the same order of entering the heap.
    heapify is BigO(n) - n is the length of the heap
    heappop - Remove the smallest element, replace root with the biggest element and _siftup rest nodes
    heappush - Adding a new element to the end of the list then _siftdown one side of the tree
    So both need BigO(log(n)) time complexity
  
    
     

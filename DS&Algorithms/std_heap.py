# in-defalut heapq is min heap. If we need max heap we can mul each element with -1 
from heapq import heapify, heappop, heappush, heapreplace
hp = [19,4, 4,13,20,2]
heapify(hp)
print("after heapify", hp)
heappush(hp, 3)
print("after push 3", hp)
arr = []
while len(hp) > 0:
    arr.append(heappop(hp))
print("sorted data are", arr)

# max heap
items = [19,4, 4,13,20,2]
hp = [i * -1 for i in items]
heapify(hp)
arr = []
while len(hp) > 0:
    arr.append(heappop(hp) * -1)
print("desc order using max heap", arr)
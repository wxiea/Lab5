class Heap:
 def __init__(self):
    self.heap_array = []
    
 def insert(self, k):
     self.heap_array.append(k)
     current = len(self.heap_array) - 1
     while current > 0:
         parent = (current - 1) // 2
         parentItem = self.heap_array[parent]
         if parentItem <= k:
             return
         else:
             self.heap_array[current] = self.heap_array[parent]
             self.heap_array[parent] = k
             current = parent

 def extract_min(self):
    if self.is_empty():
        return None
    min_elem = self.heap_array[0]
    bottomItem = self.heap_array.pop(len(self.heap_array) - 1)
    if len(self.heap_array) == 0:
        return bottomItem           
    self.heap_array[0] = bottomItem
    last = len(self.heap_array) - 1
    current = 0
    while True:
        left = 2 * current + 1 
        right = 2 * current + 2
        if left > last:
            break
        if right > last:
            temp = left;
        else:
            leftItem  = self.heap_array[left]
            rightItem = self.heap_array[right]
            if leftItem < rightItem:
                temp = left
            else:
                temp = right
        Item = self.heap_array[temp]
        if bottomItem <= Item:
            break
        else:
            self.heap_array[current] = self.heap_array[temp]
            self.heap_array[temp] = bottomItem
            current = temp
    return min_elem

    
 def is_empty(self):
    return len(self.heap_array) == 0

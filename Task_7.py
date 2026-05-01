def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def display(self):
        return self.items
stack = Stack()
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input("Enter value: "))
    stack.push(val)
print("Stack:", stack.display())
lst = stack.display()
sorted_list = selection_sort(lst)
print("Sorted List:", sorted_list)
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def display(self):
        return self.items
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
q = Queue()
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input("Enter value: "))
    q.enqueue(val)
print("Queue:", q.display())
key = int(input("Enter element to search: "))
index = linear_search(q.display(), key)
if index != -1:
    print("Element found at position", index)
else:
    print("Element not found")
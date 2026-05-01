lst = [5, 10, 15, 20, 25, 30]
print("List:", lst)
key = int(input("Enter element: "))
block_size = 2
found = False
for i in range(0, len(lst), block_size):
    if lst[i] <= key <= lst[min(i + block_size - 1, len(lst) - 1)]:
        for j in range(i, min(i + block_size, len(lst))):
            if lst[j] == key:
                print("Element found")
                found = True
                break
        break
if not found:
    print("Element not found")
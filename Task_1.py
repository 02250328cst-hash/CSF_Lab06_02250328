lst = [10, 20, 30, 40, 50]
print("List:", lst)
key = int(input("Enter element to search: "))
for i in range(len(lst)):
    if lst[i] == key:
        print("Element found at position", i + 1)
        break
else:
    print("Element not found")
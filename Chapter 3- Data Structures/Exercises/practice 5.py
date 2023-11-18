# find value 20 in the list. update the first occurrence of an item.

list1 = [5, 10, 15, 20, 25, 50, 20]

if 20 in list1:
    a = list1.index(20)
    list1[a] = 200
else:
    print("Value 20 is not in the list.")

print("Updated list:", list1)
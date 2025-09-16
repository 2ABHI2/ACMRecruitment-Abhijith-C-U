list = [3, 2, 4, 1, 9, 5, 6, 8, 7]
for i in range(1, len(list)):
    temp = list[i]
    j = i - 1
    while j >= 0 and list[j] > temp :
        list[j + 1] = list [j]
        j = j - 1
    list [ j + 1] = temp
print("Sorted list:", list )
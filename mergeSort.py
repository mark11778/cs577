def mergeSort(partion):
    if len(partion) == 1:
        return partion
    
    mid = (len(partion)) // 2

    left =  mergeSort(partion[:mid ])
    right = mergeSort(partion[mid :])

    r = 0
    l = 0

    rebuilt = []

    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            rebuilt.append(right[r])
            r += 1
        else:
            rebuilt.append(left[l])
            l += 1

    if l < len(left):
        for i in range(l, len(left)):
            rebuilt.append(left[i])
    else:
        for i in range(r, len(right)):
            rebuilt.append(right[i])

    return rebuilt

arr = [6,3,7,1,8,34]

# arr = [2,1]

print(mergeSort(arr))
        

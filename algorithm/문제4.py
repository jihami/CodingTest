'''4.Bubble Sort 구현'''
arr = [4,3,2,7]

for i in range(0, len(arr)-1):
    for j in range(0, len(arr)-i-1):
        if(arr[j]>arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)


if arr[0] > arr[1]:
    arr[0], arr[1] = arr[1], arr[0]
if arr[1] > arr[2]:
    arr[1], arr[2] = arr[2], arr[1]
if arr[2] > arr[3]:
    arr[2], arr[3] = arr[3], arr[2]

if arr[0] > arr[1]:
    arr[0], arr[1] = arr[1], arr[0]
if arr[1] > arr[2]:
    arr[1], arr[2] = arr[2], arr[1]

if arr[0] > arr[1]:
    arr[0], arr[1] = arr[1], arr[0]

print(arr)
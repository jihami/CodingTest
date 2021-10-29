'''버블 소트 구현'''
arr = [4,3,2,7]

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
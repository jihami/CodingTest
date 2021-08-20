# 1단계. 리스트에 들어있는 각 자연수의 개수를 셉니다.
arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
count=[0]*4
for x in arr:
    count[x] += 1

print(f"1의 갯수:{count[1]}")
print(f"2의 갯수:{count[2]}")
print(f"3의 갯수:{count[3]}")

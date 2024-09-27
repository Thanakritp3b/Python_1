num = int(input())
arr = list(map(int, input().split()))
new_list = []
for i in range(len(arr)) :
    if arr[i] not in new_list :
        new_list.append(arr[i])

print(len(new_list))

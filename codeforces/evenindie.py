num_of_num = int(input())
lst = list(map(int, input().split()))
newlst = []
for i in range (len(lst)) :
    if i % 2 == 0 :
        newlst.append(lst[i])
print(*newlst)
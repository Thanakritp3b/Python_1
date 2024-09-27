flag = False
n = int(input())
lst = list(map(int, input().split()))

for i in range(len(lst)) :
    if i != len(lst) - 1:
        if (lst[i] < 0 and lst[i+1] < 0) or (lst[i] > 0 and lst[i+1] > 0):
            flag = True

if flag == True :
    print('YES')
else :
    print('NO')
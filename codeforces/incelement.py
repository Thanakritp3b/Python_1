num_of_num = int(input())
lst = list(map(int, input().split()))
plus_num = int(input())
new_lst = [x+plus_num for x in lst]
print(*new_lst)
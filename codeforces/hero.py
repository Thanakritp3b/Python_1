all_num = int(input())
sum_of_input_num = 0
sum_of_real_num = 0
for num in range(1,all_num) :
    input_num = int(input())
    sum_of_input_num += input_num

for num in range(1,all_num+1) :
    sum_of_real_num += num
answer = sum_of_real_num - sum_of_input_num
print(answer)

first_c = int(input())
second_c = int(input())
third_c = int(input())

if (first_c <= second_c) & (first_c <= third_c) :
    min_c = first_c
elif (second_c <= first_c) & (second_c <= third_c) :
    min_c = second_c
else :
    min_c = third_c
max_sum = (first_c + second_c + third_c) - min_c
 
print(max_sum)

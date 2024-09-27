cake_1 = int(input())
cake_2 = int(input())
bag_1 = int(input())
bag_2 = int(input())

if cake_1 > cake_2 :
    cake_mx = cake_1
    cake_mn = cake_2
else :
    cake_mx = cake_2
    cake_mn = cake_1

if bag_1 > bag_2 :
    bag_mx = bag_1
    bag_mn = bag_2

else :
    bag_mx = bag_2
    bag_mn = bag_1


if (bag_mx < cake_mx) or (bag_mn < cake_mn) :
    print("NO")
else :
    print("YES")




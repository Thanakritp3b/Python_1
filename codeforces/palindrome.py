s = input()
flag = False

for i in range(len(s)) :
    if s[i] != s[ len(s) - 1 - i] :
        flag = True

if flag == 1 :
    print ("NO")
else :
    print ("YES")


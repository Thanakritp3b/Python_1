s = input()
if s.count('A') > s.count('B') :
    print("ALICE")
elif s.count('A') == s.count('B') :
    print("DRAW")
else : 
    print("BOB")
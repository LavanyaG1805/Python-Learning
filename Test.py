try:
    a = int(input()) #Step 1 -> getting input 10
    b = int(input()) #Step 2 -> hi -> it gives error so, it go into except block
    print(a+b)
except Exception as e:
    print("Something", e) #step 3 -> after coming to except block it will print "something"
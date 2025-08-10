for i in range(1,5):
    print()#Gap
    for j in range(1,i+1):
        print("*", end="")

#i=1   j(1,2)->j=1
#i=2   j(1,3)->j=1,2
#i=3   j(1,4)->j=1,2,3
#i=4   j(1,5)->1,2,3,4
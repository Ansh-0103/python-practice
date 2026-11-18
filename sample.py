import statistics
def grade():
    l=[]
    a=int(input("enter no of subject"))
    for i in range(a):
        marks=int(input("enter marks"))
        l+=[marks]
    G=[]
    for j in l:
        if j>=90:
            G+=['A']
        elif (j>=75):
            G+=['B']
        elif (j>=50):
            G+=['C']
        else:
            G+=['Fail']
    print(G)  
    for k in range(a):
        print(l[k],':',G[k])
    try:
        avg= statistics.mean(l)
        print("average marks",avg)
        print("marks max",max(l))
    except (statistics.StatisticsError, ValueError):
        print("no value provided")              
grade()                        



    
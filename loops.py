                  #Program 1 FizzBuzz
'''The task: for each number from 1 to 30, print:
Fizz if it’s a multiple of 3
Buzz if it’s a multiple of 5
FizzBuzz if it’s a multiple of both
the number itself otherwise
'''
for i in range(1,31):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif (i%3==0):
        print("Fizz")
    else:
        print(i) 
                #Program 2 (loop and comprehension)
l1=[]
for j in range(1,21):
    if j%2==0:
        l1+=[j*j]
print(l1)     
#list comprehension
l2=[ j*j for j in range(1,21) if j%2==0]   
print(l2)
print(l1==l2)
 



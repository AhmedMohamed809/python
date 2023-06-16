#sum all number in arry 
result = 0 
numbers=[1,2,3,4,5,6]
for i in numbers:
    result = result + i
    if i > 4 :
        print("large numbers is :"+str(i))
print("the sum of the arry is : "+str(result))
average= result / len(numbers)
print("average is  :" + str(average))

weight= float(input("Enter your weight? "))
kg= 0.45
lbs= 0.45
k_l=input("(K)g or (L)bs ").upper()
if k_l == "L":
    result=weight*lbs
    print("Weight in Kg is "+ str(result))
else :
    result=weight/kg
    print("Weight in Lbs is "+ str(result))
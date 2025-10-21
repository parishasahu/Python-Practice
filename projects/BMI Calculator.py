def form(age,weight,height,name):
    print(f"Hello {name} welcome")
    print(f"age {age}")
    print(f"weight {weight}")
    print(f" height {height}")
    bmi = weight/(height**2)
    print(f"your bmi is :{bmi}")
    if bmi<18:
        print("underweight")
    elif bmi>18 and bmi<24:
        print("normal")
    else:
        print("obese")
    
form(18,57,1.74,"pritish")
form(18,45,1.68,"aashi")
form(55,64,1.72,"sunil")
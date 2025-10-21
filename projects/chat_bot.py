name = input("What is your name? : ")
print(name)
mood = input(f"hello {name} how is your mood? ")
if mood=="good":
    print("happy")
elif mood == "bad":
    print("sleep")
else:
    print("i cant understand")

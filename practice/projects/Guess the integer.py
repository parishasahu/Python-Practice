import random


file1 = open("score.txt","w+")
print(file1.read())

for i in range(1,6):
    game = random.randint(1,2)
    
    user = int(input("guess the number"))
    if game==user :
        print("win")
        file1.write("win\n")

    else :
        print("lose")
        file1.write("lose\n")


    print(game)

file1.seek(0)
data= file1.read()
print(data)
score= (data.count("win"))*10
print(score)
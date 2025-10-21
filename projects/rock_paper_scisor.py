import random
user_move = input("enter paper, rock, scissor: ")
moves = ["rock","scissor","paper"]
computer_move = random.choice(moves)
print(computer_move)

if computer_move == user_move:
   print("tie")
elif computer_move =="rock" and user_move=="paper":
   print("user win")
elif computer_move =="scissor" and user_move=="rock":
   print("user win")
elif computer_move =="paper" and user_move =="scissor":
   print("user win")

else:
   print("lose")
import random
user_choice = int(input("Enter your choice: Type 0 for Rock,1 for Paper,2 for Scissors"))
computer_choice = random.randint(0,2)
print("computer choice:")
if computer_choice==user_choice:
 print("It's a Draw")
elif computer_choice>user_choice:
 print("Use Lose")
elif user_choice>computer_choice:
 print("you Win")
elif computer_choice==0 and user_choice==2:
 print("you Lose")
elif user_choice==0 and computer_choice==2:
 print("you Win")
else:
  print("You entered invalid number")
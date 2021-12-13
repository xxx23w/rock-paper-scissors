rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_image=[rock,paper,scissors]
user_choice=int(input("What you choose?0 for rock,1 for paper,2 for scissors:"))

if user_choice >=3 or user_choice<0:
  print("invalid")
else:
 print(game_image[user_choice])

 computer_choice=random.randint(0,2)
 print("Computer choice:")
 print(game_image[computer_choice])

'''if user_choice==0 and computer_choice==2:
  print("win")
elif computer_choice==0 and user_choice==2:
  print("loose")'''
if computer_choice > user_choice:
  print("loose")
elif user_choice > computer_choice:
  print("win")
elif computer_choice == user_choice:
  print("draw")





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

import random

rps = ["rock", "paper", "scissors"]
rps_rand = random.choice(rps)

user_input = input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
if rps_rand == rps[0] and user_input == "0":
  print (f"{rock}\nComputer chooses:{rock}\nIt's a draw :>")
elif rps_rand == rps[1] and user_input == "0":
  print(f"{rock}\nComputer chooses:{paper}\nYou lose >:")
elif rps_rand == rps[2] and user_input == "0":
  print(f"{rock}\nComputer chooses: {scissors}\nYou win! n_n")
elif rps_rand == rps[1] and user_input == "1":
  print (f"{paper}\nComputer chooses:{paper}\nIt's a draw :>")
elif rps_rand == rps[2] and user_input == "1":
  print(f"{paper}\nComputer chooses:{scissors}\nYou lose >:")
elif rps_rand == rps[0] and  user_input == "1":
  print(f"{paper}\nComputer chooses: {rock}\nYou win! n_n")
elif rps_rand == rps[2] and user_input == "2":
  print (f"{paper}\nComputer chooses:{paper}\nIt's a draw :>")
elif rps_rand == rps[0] and user_input == "2":
  print(f"{paper}\nComputer chooses:{scissors}\nYou lose >:")
elif rps_rand == rps[1] and  user_input == "2":
  print(f"{paper}\nComputer chooses: {rock}\nYou win! n_n")
else:
  print("Fission Mailed")

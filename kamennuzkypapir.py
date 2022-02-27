import random

user_action = input("Vyber si (kamen, papir, nuzky): ")
possible_actions = ["kamen", "papir", "nuzky"]
computer_action = random.choice(possible_actions)
print(f"\nVybral si {user_action}, pocitac vybral {computer_action}.\n")

if user_action == computer_action:
    print(f"Oba hraci vybrali {user_action}. Je to remiza!")
elif user_action == "kamen":
    if computer_action == "nuzky":
        print("Kamen znicy nuzky! Vyhral si!")
    else:
        print("Papir zabali kamen! Prohral si.")
elif user_action == "papir":
    if computer_action == "kamen":
        print("Papir zabali kamen! Vyhral si!")
    else:
        print("Nuzky roztrihnou papir! Prohral si.")
elif user_action == "nuzky":
    if computer_action == "papir":
        print("Nuzky roztrihnou papir! Vyhral si!")
    else:
        print("Kamen znicy nuzky! Prohral si.")
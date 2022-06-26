import random 

user_wins = 0
computer_wins = 0

options = ["sasso", "carta", "forbici"]

while True:
    user_input = input("Scegli Sasso/Carta/Forbici o Q per chiudere: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("L'avversario ha scelto",computer_pick)
    
    if user_input == "sasso" and computer_pick == "forbici":
        print("Hai vinto!")
        user_wins += 1
        
    elif user_input == "carta" and computer_pick == "sasso":
        print("Hai vinto!")
        user_wins += 1
        
    elif user_input == "forbici" and computer_pick == "carta":
        print("Hai vinto!")
        user_wins += 1
    
    else:
        print("Hai perso!")
        computer_wins += 1
    
print("Hai fatto", user_wins, "punti VS", computer_wins, "dell'avversario")
print("La partita è terminata!")
    
    
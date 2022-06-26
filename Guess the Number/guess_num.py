import random

top_of_range = input("Inserisci un numero: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Inserisci un numero maggiore di 0.')
        quit()
else:
    print('Non hai inserito un numero!')
    quit()


random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Prova ad indovinare il numero: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Non hai inserito un numero!')
        continue
        
    if user_guess == random_number:
        print("Hai indovinato!")
        break
    elif user_guess > random_number:
        print("Il numero da indovinare è più piccolo!")
    else:
        print("Il numero da indovinare è più grande!")

print("Hai indovinato in", guesses, "tentativi")

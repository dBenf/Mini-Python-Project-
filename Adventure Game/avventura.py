name  = input("Inserisci il tuo nome: ")
print("Ciao", name, "e benvenuto nella tua avventura!")

answer = input("Sei ad un bivio su una strada sterrata, dove decidi di andare, a destra o a sinistra? ").lower()

if answer == "sinistra":
    answer = input("Sei arrivato ad un fiume. Vuoi attraversarlo o girarci attorno? Scrivi 'passa' per attraversare o 'gira' per aggirare il fiume: ").lower()
    if answer == 'passa':
        print("Sei stato divorato da un alligatore!")
    elif answer == 'gira':
        print("Hai camminato per ore e sei rimasto senza acqua. Hai perso!")
    else:
        print("Opzione non valida. Hai perso!")
elif answer == "destra":
    answer = input("Ti trovi davanti ad un ponte, che sembra pericoloso. Vuoi attraversarlo? (si/no): ").lower()
    
    if answer == 'si':
        answer = input("Sei sopravvissuto al ponte, e dall'altro lato hai incontrato uno straniero. Vuoi parlare con lui? (si/no): ").lower()
        if answer == 'si':
            print("Lo straniero ti ha regalato dell'oro. HAI VINTO!")
        elif answer == 'no':
            print("Lo straniero è scappato con la ricompensa. Hai perso!")
        else:
            print("Opzione non valida. Hai perso!")
    elif answer == 'no':
        print("Sei tornato indietro ed una tribu indigena ti ha rapito. Hai perso!")
    else:
        print("Opzione non valida. Hai perso!")
else:
    print("Opzione non valida. Hai perso!")
    
    
print("Ciao",name, ", alla prossima avventura!")
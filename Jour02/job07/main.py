import random

def valeur_carte(carte):
    if carte in ['J', 'Q', 'K']:
        return 10
    elif carte == 'A':
        return 11
    else:
        return int(carte)

def total_main(main):
    total = 0
    as_count = 0
    for carte in main:
        if carte == 'A':
            as_count += 1
        total += valeur_carte(carte)
    while as_count > 0 and total > 21:
        total -= 10
        as_count -= 1
    return total

def jouer_blackjack():
    print("Bienvenue au Blackjack !")
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    main_joueur = [deck.pop(), deck.pop()]
    main_croupier = [deck.pop(), deck.pop()]
    print("La main du croupier : X,", main_croupier[1])
    while True:
        print("Votre main :", main_joueur)
        choix = input("Voulez-vous tirer une carte ? (o/n) ")
        if choix == 'o':
            main_joueur.append(deck.pop())
            if total_main(main_joueur) > 21:
                print("Vous avez dépassé 21 ! Vous avez perdu.")
                return
        else:
            break
    croupier_total = total_main(main_croupier)
    while croupier_total < 17:
        main_croupier.append(deck.pop())
        croupier_total = total_main(main_croupier)
    print("La main du croupier :", main_croupier)
    if croupier_total > 21:
        print("Le croupier a dépassé 21 ! Vous avez gagné.")
    elif total_main(main_joueur) > croupier_total:
        print("Vous avez gagné !")
    elif total_main(main_joueur) == croupier_total:
        print("Égalité !")
    else:
        print("Le croupier a gagné.")

jouer_blackjack()

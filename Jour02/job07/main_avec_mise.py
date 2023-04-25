import random

def valeur_carte(carte):
    if carte == "As":
        return 11
    elif carte in ["Valet", "Dame", "Roi"]:
        return 10
    else:
        return int(carte)

def total_main(main):
    total = 0
    nombre_as = 0
    for carte in main:
        valeur = valeur_carte(carte)
        if valeur == 11:
            nombre_as += 1
        total += valeur
    while total > 21 and nombre_as:
        total -= 10
        nombre_as -= 1
    return total

def blackjack():
    print("Bienvenue au Blackjack !")
    deck = []
    couleurs = ["Coeur", "Pique", "Carreau", "Trèfle"]
    cartes = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
    for couleur in couleurs:
        for carte in cartes:
            deck.append(carte + " de " + couleur)
    random.shuffle(deck)
    argent = 100
    while argent > 0:
        print("Vous avez", argent, "euros.")
        mise = 0
        while mise == 0 or mise > argent:
            mise = int(input("Combien voulez-vous miser ? "))
        print()
        main_joueur = [deck.pop(), deck.pop()]
        main_croupier = [deck.pop()]
        print("Votre main :", main_joueur)
        print("Main du croupier :", main_croupier)
        while True:
            choix = input("Voulez-vous tirer une carte ? (o/n) ")
            if choix.lower() == "o":
                main_joueur.append(deck.pop())
                print("Votre main :", main_joueur)
                if total_main(main_joueur) > 21:
                    print("Vous avez perdu !")
                    argent -= mise
                    break
            else:
                while total_main(main_croupier) < 17:
                    main_croupier.append(deck.pop())
                print("Main du croupier :", main_croupier)
                if total_main(main_croupier) > 21:
                    print("Le croupier a perdu !")
                    argent += mise
                    break
                elif total_main(main_croupier) > total_main(main_joueur):
                    print("Le croupier a gagné !")
                    argent -= mise
                    break
                elif total_main(main_joueur) > total_main(main_croupier):
                    print("Vous avez gagné !")
                    argent += mise
                    break
                else:
                    print("Égalité !")
                    break
        print()
    print("Vous êtes ruiné ! Au revoir !")

blackjack()
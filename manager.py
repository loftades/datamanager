import sys

LISTE = []

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajoutez un element a la liste
2: Retirez un element de la liste
3: Affichez la liste
4: vider la base
5: Quitter
Votre choix : """

MENU_CHOICES = ["1","2", "3", "4", "5"]


while True:
    User_Choice = ""
    while User_Choice not in MENU_CHOICES:
        User_Choice = input(MENU)
        if User_Choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")
    if User_Choice == "1":
        item = input("Entrez le nom d'un element a ajouter a la base de donnee : ")
        LISTE.append(item)
        print(f"L'element {item} a bien ete ajoute a la base.")
    elif User_Choice == "2":
        item = input("Entrez le nom de l'element a retirer de la base de donnee : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'element {item} a bien ete supprimer de la base.")
        else :
            print(f"L'element {item} n'est pas dans la base.")
    elif User_Choice == "3":
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else :
            print("Votre base ne contient aucun element.")
    elif User_Choice == "4":
        LISTE.clear()
        print("La base a bien ete vide de son contenu.")

    elif User_Choice == "5":
        print("A bientot!")
        sys.exit()

        print("-" * 50)

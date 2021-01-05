import donnees
import fonctions

# On demande d'abord son nom à l'utilisateur afin d'enregistrer son score dans un fichier.
# Avec la fonction verifier_utilisateur on vérifie si le pseudo est déjà rentré et on met son score à jour
# En plus de récupérer la liste des scores du jeu

nom_utilisateur = input("Entrez votre pseudo : ")
fonctions.verifier_utilisateur(nom_utilisateur)

partie_en_cours = True

# Le jeu définit un mot pour la partie dans la liste et initialise le mot à découvrir avec des *
mot_partie = fonctions.choisir_mot() # Fonctionne
mot_partie = str(mot_partie)
mot_decouvert = "*" * len(mot_partie)
mot_decouvert_temp =""

while partie_en_cours == True:
    mot_decouvert_temp = mot_decouvert
    lettre_utilisateur = str(input("Rentrez une lettre "))
    mot_decouvert = fonctions.verifier_lettre(lettre_utilisateur, mot_partie, mot_decouvert)
    if mot_decouvert_temp == mot_decouvert:
        donnees.vie_joueur -= 1
        print("Vous n'avez pas trouvé de lettre, plus que {} coups\nLe mot est {}".format(donnees.vie_joueur, mot_decouvert))
    else:
        print("Le mot pour le moment est {}, plus que {} coups".format(mot_decouvert, donnees.vie_joueur))
    if mot_decouvert == mot_partie:
        print("Vous avez réussi à trouver le mot, votre score est de {}".format(donnees.vie_joueur))
        fonctions.enregistrer_score(nom_utilisateur, donnees.vie_joueur)
        partie_en_cours = False
    if donnees.vie_joueur < 1:
        partie_en_cours = False
        print("Le mot était", mot_partie, "Vous n'avez plus de coup, GAME OVER")
    

import donnees
import json
from random import randrange
#Contient toutes les fonctions du programme

#On veut vérifier si le nom d'utilisateur existe déjà et mettre ses scores à jour, sinon on le créée dans le fichier score
def verifier_utilisateur(nom_utilisateur):
    # On ouvre le fichier et on importe son contenu dans le dictionnaire score_joueurs
    with open("scores", "r") as ouverture_scores:
        chaine_score = ouverture_scores.read()
    chaine_score = json.loads(chaine_score)
    # print(type(chaine_score))
    # On cherche dans la liste si on a déjà le pseudo enregistré, si oui on acceuille l'utilisateur
    if nom_utilisateur.lower() not in [key.lower() for key in chaine_score.keys()]:
        chaine_score[nom_utilisateur] = 0
        print("Bienvenue", nom_utilisateur, "votre pseudo a bien été enregistré")
    else:
        print("Bon retour", nom_utilisateur)
    print("Liste des scores", chaine_score)
    with open("scores", "w") as ouverture_scores:
        json.dump(chaine_score, ouverture_scores)


# with open("scores", "a") as fichier_score:
#     fichier_score
""" la fonction choisir_mot() va récupérer un mot de la liste dans le fichier donnees.py et l'afficher
    sous forme d'étoiles
"""
def choisir_mot():
    num_mot = randrange(0, 20)
    mot_chaine = donnees.mot_choisis[num_mot]
    return mot_chaine

"""On utilise la fonction pour vérifier si la lettre rentrée par l'utilisateur correspond à une lettre du mot
On parcourt la liste et on affiche les lettres révélées. Il faut remettre en strOn capture le résultat
"""
def verifier_lettre(lettre_utilisateur, mot_partie, mot_decouvert):
    mot_decouvert_liste = list(mot_decouvert)
    for i, lettre in enumerate(mot_partie):
        if lettre.upper() == lettre_utilisateur.upper():
            mot_decouvert_liste[i] = lettre_utilisateur.upper()
    return "".join(mot_decouvert_liste)

""" On parcourt la liste pour chaque lettre dans le mot choisi par le jeu
Si la lettre de l'utilisateur correspond à une lettre du mot, on ajoute la lettre à la chaîne
Les étoiles sont mises automatiquement en place par le jeu suivant la longueur du mot
On renvoie la liste avec le mot déchiffré transformée en chaîne
"""

def enregistrer_score(nom_utilisateur, vie_joueur):
    with open("scores", "r") as ouverture_scores:
        chaine_score = ouverture_scores.read()
    chaine_score = json.loads(chaine_score)
    chaine_score[nom_utilisateur] = vie_joueur
    with open("scores", "w") as ouverture_scores:
        json.dump(chaine_score, ouverture_scores)
    print("Votre score a été enregistré", nom_utilisateur,"\n", chaine_score)
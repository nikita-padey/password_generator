import random
import hashlib
import string

good = False
caracteres_speciaux = "!@#$%^&*"

while not good:

    good = True

    mot_de_pass = input("Veuillez entrer votre mot de pass : ")
    
    if len(mot_de_pass) < 8:
        print("Le mot de pass doit contenir au moins 8 caractères.")
        good = False
        continue

    if not any(char.isupper() for char in mot_de_pass):
        print("Le mot de pass doit contenir au moins une lettre majuscule.")
        good = False
        continue

    if not any(char.islower() for char in mot_de_pass):
        print("Le mot de pass doit contenir au moins une lettre minuscule.")
        good = False
        continue

    if not any(char.isdigit() for char in mot_de_pass):
        print("Le mot de pass doit contenir au moins un chiffre.")
        good = False
        continue

    if not any(char in caracteres_speciaux for char in mot_de_pass):
        print("Le mot de pass doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        good = False
        continue

    print("Mot de passe valide !")

hash_mdp = hashlib.sha256() # Créer un objet de hachage SHA-256
hash_mdp.update(mot_de_pass.encode()) # Encoder le mot de passe en bytes et le passer à l'algorithme de hachage
mot_de_passe_hache = hash_mdp.hexdigest() # Obtenir le mot de passe haché (en hexadécimal)
print("Votre mot de passe haché est :", mot_de_passe_hache)
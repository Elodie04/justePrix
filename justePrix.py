import random

prix = random.randint(1, 100)

tentatives = 0

print("Devinez le juste prix ! Le prix est un nombre compris entre 1 et 100 inclus.")

while True:
    nombre = int(input())
    tentatives += 1
    if nombre < prix:
        print("Le just prix est plus haut")
    if nombre > prix:
        print("Le juste prix est plus bas")
    if nombre == prix:
        print(f"Félicitations, vous avez trouvé le juste prix en {tentatives} essais!")
        break

print("Partie terminée")

# doc: https://code.visualstudio.com/docs/python/python-tutorial

# utilisation du package (librairie) nécessaire pour la génération du nombre aléatoire
import numpy as np

msg = "Hello World!"
print(msg)

#affiche un nombre aléatoire appartenant à [1,9[
print(np.random.randint(1,9))

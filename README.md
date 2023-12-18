
# Alignment free - TP 2 (PHYG TME6)

## Auteurs : Aya Elmesaoudi et Sharane K.Murali

L'objectif du TP est d'implémenter une des méthodes vu en cours pour optimiser le calcul en termes de mémoire.

## Rapport

Dans kmers.py, nous avons ajouté la fonction xorshift ainsi que la fonction d'échanitllonage en stockant les variables dans un arbre heapq. Ensuite la fonction de calcul de la distance de Jaccard a été modifié en conséquence et réside sur la comparaison d'entiers entre les deux listes. 

Voici également le temps d'exécution qu'il a fallu pour calculer cette matrice ainsi que l'espace mémoire maximale. La commande ```/usr/bin/time -v``` a été utilisée sur Ubuntu et la commande ```/usr/bin/time -l``` a été utilisée sur macOS.

Ci-dessous se trouvent les logs d'exécution sur le TME précéndent.

Voici le résultat obtenu sur Ubuntu : 

![Screenshot_from_2023-11-30_11-35-43](https://github.com/RaneMura/Master2_BIM-PHYG-TME6/assets/74711674/bcebee1b-f05e-4308-9acc-9e2381537667)

Voici le résultat obtenu sur Mac : 

<img width="371" alt="Capture_decran_2023-11-30_a_11 27 31" src="https://github.com/RaneMura/Master2_BIM-PHYG-TME6/assets/74711674/f7632040-6a06-40f5-be3a-01fa445484b3">


Ci-dessous se trouvent les logs d'exécution sur ce TME avec k = 21 et s = 10000

Voici le résultat obtenu sur Ubuntu : 

#EN ATTENTE

Voici le résultat obtenu sur Mac : 
<img width="324" alt="Capture d’écran 2023-12-18 à 18 55 16" src="https://github.com/RaneMura/Master2_BIM-PHYG-TME6/assets/74711674/b73b8e54-8f20-45f8-b41d-6f52dac68cfb">


Nous pouvons constater qu'une diminution de l'utilisation de la mémoire est visible.






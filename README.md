
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


Nous pouvons constater qu'une diminution de l'utilisation de la mémoire ainsi que du temps d'exécution est visible.

Si on se penche du côté des résultats : 

Voici la matrice de similarité obtenue sur le précédent TME : 

|                                          | GCF_020526745.1_ASM2052674v1_genomic.fna | GCF_014892695.1_ASM1489269v1_genomic.fna | GCF_008244785.1_ASM824478v1_genomic.fna | GCF_020535205.1_ASM2053520v1_genomic.fna | GCF_000006945.2_ASM694v2_genomic.fna |
|------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------------|------------------------------------------|--------------------------------------|
| GCF_020526745.1_ASM2052674v1_genomic.fna | 1.0                                      | 0.0019466253653915354                    | 0.019325578624672622                    | 0.6138990942236009                       | 0.019091889920944443                 |
| GCF_014892695.1_ASM1489269v1_genomic.fna | 0.0019466253653915354                    | 1.0                                      | 0.00176801912767907                     | 0.0039007084501784146                    | 0.0017591971757668513                |
| GCF_008244785.1_ASM824478v1_genomic.fna  | 0.019325578624672622                     | 0.00176801912767907                      | 1.0                                    | 0.018013179734302463                     | 0.9377564127983907                   |
| GCF_020535205.1_ASM2053520v1_genomic.fna | 0.6138990942236009                       | 0.0039007084501784146                    | 0.018013179734302463                    | 1.0                                      | 0.01791031228841616                  |
| GCF_000006945.2_ASM694v2_genomic.fna     | 0.019091889920944443                     | 0.0017591971757668513                    | 0.9377564127983907                      | 0.01791031228841616                      | 1.0                                  |


Voici la matrice de similarité obtenu sur ce TME :

|                                          | GCF_020526745.1_ASM2052674v1_genomic.fna | GCF_014892695.1_ASM1489269v1_genomic.fna | GCF_008244785.1_ASM824478v1_genomic.fna | GCF_020535205.1_ASM2053520v1_genomic.fna | GCF_000006945.2_ASM694v2_genomic.fna |
|------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------------|------------------------------------------|--------------------------------------|
| GCF_020526745.1_ASM2052674v1_genomic.fna | 1.0                                      | 0.0005148951820522251                    | 0.01924532381879122                     | 0.5662276654643067                       | 0.0190091221936964                   |
| GCF_014892695.1_ASM1489269v1_genomic.fna | 0.0005148951820522251                    | 1.0                                      | 0.0002273933146365497                   | 0.0016763181956720513                    | 0.00022832787883400563               |
| GCF_008244785.1_ASM824478v1_genomic.fna  | 0.01924532381879122                      | 0.0002273933146365497                    | 1.0                                     | 0.01779213454340358                      | 0.9284116331096197                   |
| GCF_020535205.1_ASM2053520v1_genomic.fna | 0.5662276654643067                       | 0.0016763181956720513                    | 0.01779213454340358                     | 1.0                                      | 0.01746613708116916                  |
| GCF_000006945.2_ASM694v2_genomic.fna     | 0.0190091221936964                       | 0.00022832787883400563                   | 0.9284116331096197                      | 0.01746613708116916                      | 1.0                                  |


On voit qu'il y a des différences qui sont minimes et que les résultats restent également fidèles aux résultats obtenus précédemment.





# Alignment free - TP 1 (PHYG TME6)

## Auteurs : Aya Elmesaoudi et Sharane K.Murali

L'objectif du TP est de comparer 5 especes de bactéries entre elles.
Les données sont disponibles sur [ce lien](https://we.tl/t-ACiDxJko7s)

## Rapport

Le but est d'obtenir toutes les distances paire à paire des différentes bactéries.

Après exécution du code, voici la matrice des distances dés bactéries obtenue :

|                                          | GCF_020526745.1_ASM2052674v1_genomic.fna | GCF_014892695.1_ASM1489269v1_genomic.fna | GCF_008244785.1_ASM824478v1_genomic.fna | GCF_020535205.1_ASM2053520v1_genomic.fna | GCF_000006945.2_ASM694v2_genomic.fna |
|------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------------|------------------------------------------|--------------------------------------|
| GCF_020526745.1_ASM2052674v1_genomic.fna | 1.0                                      | 0.0019466253653915354                    | 0.019325578624672622                    | 0.6138990942236009                       | 0.019091889920944443                 |
| GCF_014892695.1_ASM1489269v1_genomic.fna | 0.0019466253653915354                    | 1.0                                      | 0.00176801912767907                     | 0.0039007084501784146                    | 0.0017591971757668513                |
| GCF_008244785.1_ASM824478v1_genomic.fna  | 0.019325578624672622                     | 0.00176801912767907                      | 1.0                                     | 0.018013179734302463                     | 0.9377564127983907                   |
| GCF_020535205.1_ASM2053520v1_genomic.fna | 0.6138990942236009                       | 0.0039007084501784146                    | 0.018013179734302463                    | 1.0                                      | 0.01791031228841616                  |
| GCF_000006945.2_ASM694v2_genomic.fna     | 0.019091889920944443                     | 0.0017591971757668513                    | 0.9377564127983907                      | 0.01791031228841616                      | 1.0                                  |


Voici également le temps d'exécution qu'il a fallu pour calculer cette matrice ainsi que l'espace mémoire maximale. La commande ```/usr/bin/time -v``` a été utilisée sur Ubuntu et la commande ```/usr/bin/time -l``` a été utilisée sur macOS.

Voici le résultat obtenu sur Ubuntu : 

![Screenshot_from_2023-11-30_11-35-43](https://github.com/RaneMura/Master2_BIM-PHYG-TME6/assets/74711674/bcebee1b-f05e-4308-9acc-9e2381537667)

Voici le résultat obtenu sur Mac : 

<img width="371" alt="Capture_decran_2023-11-30_a_11 27 31" src="https://github.com/RaneMura/Master2_BIM-PHYG-TME6/assets/74711674/f7632040-6a06-40f5-be3a-01fa445484b3">


En observant les distances obtenues, deux espèces "GCF_008244785.1_ASM824478v1_genomic.fna" et "GCF_000006945.2_ASM694v2_genomic.fna" sont très proches avec une valeur de 0.9377.

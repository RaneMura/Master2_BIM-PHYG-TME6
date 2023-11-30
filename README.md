
# Alignment free - TP 1 (PHYG TME6)

## Auteurs : Aya Elmesaoudi et Sharane K.Murali

L'objectif du TP est de comparer 5 especes de bactéries entre elles.
Les données sont disponibles sur [ce lien](https://we.tl/t-ACiDxJko7s)

## Rapport

Le but est d'obtenir toutes les distances paire à paire des différentes bactéries.

Après exécution du code, voici la matrice des distances dés bactéries obtenue :

|GCF_020526745.1_ASM2052674v1_genomic.fna|GCF_014892695.1_ASM1489269v1_genomic.fna|GCF_008244785.1_ASM824478v1_genomic.fna|GCF_020535205.1_ASM2053520v1_genomic.fna|GCF_000006945.2_ASM694v2_genomic.fna|
|----------------------------------------|----------------------------------------|---------------------------------------|----------------------------------------|------------------------------------|
|1.0                                     |0.0019466253653915354                   |0.019325578624672622                   |0.6138990942236009                      |0.019091889920944443                |
|0.0019466253653915354                   |1.0                                     |0.00176801912767907                    |0.0039007084501784146                   |0.0017591971757668513               |
|0.019325578624672622                    |0.00176801912767907                     |1.0                                    |0.018013179734302463                    |0.9377564127983907                  |
|0.6138990942236009                      |0.0039007084501784146                   |0.018013179734302463                   |1.0                                     |0.01791031228841616                 |
|0.019091889920944443                    |0.0017591971757668513                   |0.9377564127983907                     |0.01791031228841616                     |1.0                                 |

Voici également le temps d'exécution qu'il a fallu pour calculer cette matrice ainsi que l'espace mémoire maximale. La commande ```/usr/bin/time -v``` a été utilisée sur Ubuntu et la commande ```/usr/bin/time -l``` a été utilisée sur macOS.

En observant les distances obtenues, que pouvez-vous dire des espèces présentes dans cet échantillon ?

Répondre ?

# pi-estimator
Le projet a pour but d'estimer la valeur de pi en utilisant Spark et Numpy pour faire une étude comparative et déterminer le plus performant.

# Resultat obtenu:
Comparaison des résultats obtenu pour les deux fonctions utilisées pour estimé la valeur de Pi: Spark Vs Numpy.

## Le tableau ci dessous resume les resultats obtenues pour le cas de n=100000:

| n =   100000      | spark                 | numpy                   |
|-------------------|-----------------------|-------------------------|
| temps d'exécution | 1.0120198726654053    | 0.0758357048034668      |
| valeurs de pi     | 3.14504               | 3.14112                 |
| écart % Math.pi   | 0.0034473464102067197 |  -0.0004726535897932038 |

## Le tableau ci dessous resume les resultats obtenues pour le cas de n=10000000:

| n =   1000000     | spark                  | numpy                |
|-------------------|------------------------|----------------------|
| temps d'exécution | 4.320241212844849      | 0.7012062072753906   |
| valeurs de pi     | 3.141852               | 3.142616             |
| écart % Math.pi   | 0.00025934641020697313 | 0.001023346410206738 |

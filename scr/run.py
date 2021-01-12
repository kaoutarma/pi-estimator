#Importation des package necessaire
from pyspark import SparkContext, SparkConf
import numpy as np
import math

#initialisation de Spark
conf = SparkConf().setAppName("PI").setMaster("local")
sc = SparkContext(conf=conf)from random import random


#définir une fonction qui vérifie si un point est à l'interieur ou l'extérieur du cercle
def is_point_inside_unit_circle(p):
  x, y = random(), random()
  if x*x + y*y < 1:
    return 1
  else:
  return 0
 
# Definir la fonction qui estime la valeur de pi avec spark
# La fonction prend comme parametre n = nombre de points
# retourne le temps d'execution, la différence entre math.pi le pi estimé et la valeur de pi estimé
def pi_estimator_spark(n):
  t0=time()
#Création d'un RDD avec la fonction is_point_inside_unit_circle et faire la somme de tous les RDD pour avoir le nombre total de points
  count = sc.parallelize(range(0, n)).map(is_point_inside_unit_circle).reduce(add)
# Calcul de PI
def pi_estimator_spark(n):
    t0=time()
#Création d'un RDD avec la fonction is_point_inside_unit_circle et faire la somme de tous les RDD pour avoir le nombre total de points
    count = sc.parallelize(range(0, n)).map(is_point_inside_unit_circle).reduce(add)
# Calcul de PI
    sparkpi=(4.0 * count / n)
#Estimation du temps d'execution
    print(time() - t0, "temps d'execution avec n=", n)
    print("La valeur de pi estimé par Spark est =", sparkpi)
    print("La différence avec math.pi est de ", (sparkpi-math.pi))ath.pi))
      
# Definir la fonction qui estime la valeur de pi avec numpy
# La fonction prend comme parametre n = nombre de points
# retourne le temps d'execution, la différence entre math.pi le pi estimé et la valeur de pi estimé
def pi_estimator_numpy(n):
    t0=time()
    matrix = np.zeros((n,1))
    for i in range(0,n):
        matrix[i,:] = is_point_inside_unit_circle(1)
    count=np.sum(matrix)
    numpypi=4*(count/n)
    print(time() - t0, "temps d'execution avec n=", n)
    print("La valeur de pi estimé par numpy est",numpypi)
    print("la difference avec math.pi est de ",(numpypi-math.pi ))

# Appel des deux fonction et comaraison pour une valeur de n= 10000000
pi_estimator_spark(1000000)
pi_estimator_numpy(1000000)

#arreter Spark
sc.stop()

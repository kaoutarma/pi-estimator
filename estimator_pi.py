from pyspark import SparkContext, SparkConf
import numpy as np#initialisation de Spark
conf = SparkConf().setAppName("PI").setMaster("local")
sc = SparkContext(conf=conf)from random import random
import math#définir une fonction qui vérifie si un point est à l'interieur ou l'extérieur du cercle
def is_point_inside_unit_circle(p):
x, y = random(), random()
if x*x + y*y < 1:
return 1
else:
return0def pi_estimator_spark(n):
t0=time()
#Création d'un RDD avec la fonction is_point_inside_unit_circle et faire la somme de tous les RDD pour avoir le nombre total de points
count = sc.parallelize(range(0, n)).map(is_point_inside_unit_circle).reduce(add)
# Calcul de PI
sparkpi=(4.0 * count / n)
print("la valeur de pi avec spark est:",sparkpi)
#Estimation du temps d'execution
print(time() - t0, "temps d'execution avec n=", n)
print("La différence avec math.pi est de ", (sparkpi-math.pi))def pi_estimator_numpy(n):
t0=time()
matrix = np.zeros((n,1))
for i in range(0,n):
matrix[i,:] = is_point_inside_unit_circle(1)
count=np.sum(matrix)
numpypi=4*(count/n)
print("la valeur de pi avec numpy",numpypi)
print(time() - t0, "temps d'execution avec n=", n)
print("la difference avec math.pi est de ",(numpypi-math.pi ))
#arreter Spark
sc.stop()


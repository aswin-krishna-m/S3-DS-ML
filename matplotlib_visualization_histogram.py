from numpy import array
from matplotlib import pyplot as plt

values = [ 5,12,18,22,25,27,26,30,34,38,39,40,42,46,45,47,49,51,56,53,67,68,64,62,70,72,74,76,77,80]
plt.xlabel("Age Group")
plt.ylabel("Frequenzy")
plt.title("Age of people")
plt.hist(values,bins=5,color='blue',edgecolor='black')
plt.show()

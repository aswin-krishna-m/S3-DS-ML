from numpy import array
from matplotlib import pyplot as plt

month = array([ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
affordable=array([250,346,292,294,154,181,152,243,362,230,314,315])
luxury=array([153,73,94,194,194,197,252,301,299,199,156,150])
superLuxury=array([53,72,87,93,85,163,153,76,90,62,89,96])

plt.xlabel("Months of Year")
plt.ylabel("Sales of Segment")
plt.title("Sales Data")
plt.scatter(month,affordable,color="green",marker="*")
plt.scatter(month,luxury,color="yellow",marker="*")
plt.scatter(month,superLuxury,color="blue",marker="*")
plt.show()

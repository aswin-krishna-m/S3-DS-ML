from numpy import array
from matplotlib import pyplot as plt

year = array([2010,2011,2012,2013,2014,2015,2016])
car_value = array([50000,48000,45500,40700,37500,33500,28000])

plt.xlabel("Year")
plt.ylabel("Car Value")
plt.title("Value Deprecation")
plt.plot(year,car_value, ls = "-",color="red",marker="*",mfc="g",ms="10",mec="b")
plt.show()
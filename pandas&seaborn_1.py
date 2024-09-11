import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("iris.csv")
print("Shape of the dataset: ",data.shape)

print("First 5 rows: \n",data.head())
print("Last 5 rows: \n",data.tail())

print("Size of the dataset: ",data.size)

print("Number of samples available for each variety: \n",data["variety"].value_counts())

print("Description of dataset: \n",data.describe())

sns.pairplot(data,hue="variety",kind="scatter",diag_kind="hist")
plt.style.use("dark_background")
sns.displot(data.sepal_length,bins=10,color="g")
plt.title("Sepal Length distribution",color="white",fontsize=10)
plt.show()
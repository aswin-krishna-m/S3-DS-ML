import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Walking','Cycling','Car','Bus','Train'])
y = np.array([30,12,18,36,4])
plt.title('Students transportation')
plt.xlabel('Transport Mode')
plt.ylabel('No. of Students')

plt.bar(x, y, color="blue",width = 0.4)
plt.show()
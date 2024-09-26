import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("iris.csv") # load dataset file path

X = dataset.iloc[:, :-1].values # independent variables
y = dataset.iloc[:, 4].values # dependent variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20) # split dataset into training and testing sets

classifier = KNeighborsClassifier(n_neighbors=5) # create KNN classifier object
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test) # make predictions

print(classification_report(y_test, y_pred))
print ("Accuracy : ", accuracy_score(y_test, y_pred))

print(pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred}))

new_test_point = np.array([[5.1, 3.5, 1.4, 0.2]]) # new test point to predict

prediction = classifier.predict(new_test_point) # predict the class of the new test point

print(f"\n Predicted class: {prediction[0]}") # print the predicted class of the new test point



""" OUTPUT 



          precision    recall  f1-score   support

      Setosa       1.00      1.00      1.00         9
  Versicolor       0.92      1.00      0.96        12
   Virginica       1.00      0.89      0.94         9

    accuracy                           0.97        30
   macro avg       0.97      0.96      0.97        30
weighted avg       0.97      0.97      0.97        30

Accuracy :  0.9666666666666667
   Real Values Predicted Values
0       Setosa           Setosa
1   Versicolor       Versicolor
2    Virginica        Virginica
3   Versicolor       Versicolor
4       Setosa           Setosa
5       Setosa           Setosa
6       Setosa           Setosa
7   Versicolor       Versicolor
8   Versicolor       Versicolor
9   Versicolor       Versicolor
10  Versicolor       Versicolor
11   Virginica        Virginica
12   Virginica        Virginica
13   Virginica        Virginica
14      Setosa           Setosa
15  Versicolor       Versicolor
16      Setosa           Setosa
17   Virginica        Virginica
18  Versicolor       Versicolor
19   Virginica        Virginica
20  Versicolor       Versicolor
21      Setosa           Setosa
22   Virginica        Virginica
23      Setosa           Setosa
24   Virginica       Versicolor
25  Versicolor       Versicolor
26  Versicolor       Versicolor
27      Setosa           Setosa
28   Virginica        Virginica
29  Versicolor       Versicolor

Predicted class: Setosa



"""
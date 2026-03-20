import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import sys
import csv

# iris = load_iris()
# print(iris)

# X = iris.data[:, :2]
# Y = iris.target

# print(X)
# print("===")
# print(Y)
# print(f"len x: {len(X)} {len(X[0])}")
# print(f"len y: {len(Y)}")

if len(sys.argv) != 2:
    print("You need a single file path")
    exit(1)
X = []
Y = []
with open(sys.argv[1]) as file:
    csv_reader = csv.DictReader(file, delimiter=",")
    headers = csv_reader.fieldnames
    feat_cols = headers[7:9]    # Astronomy, Herbology
    target_col = headers[1]     # Hogwarts House
    for row in csv_reader:
        try:
            features = [float(row[c]) for c in feat_cols]
        except (ValueError, TypeError):
            continue  # skip rows with missing values
        X.append(features)
        Y.append(row[target_col])
X = np.array(X)
Y = np.array(Y)
le = LabelEncoder()
Y = le.fit_transform(Y)
clf = OneVsRestClassifier(LogisticRegression(random_state=0, solver='liblinear'))

clf.fit(X, Y)
res = clf.predict(X)
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, .02),
                     np.arange(y_min, y_max, .02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
print(f"{Z}\n{len(Z)}")
print(f"{res}\n{len(res)}")
# Z = Z.reshape(xx.shape)
# plt.figure(1, figsize=(4, 3))
# plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
# plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k',
#             cmap=plt.cm.Paired)
# plt.xlabel('Astronomy')
# plt.ylabel('Herbology')
# plt.title('One-vs-Rest logistic regression')
# plt.show()
print(accuracy_score(Y, res))
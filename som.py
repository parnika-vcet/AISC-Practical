
import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [1, 1], [1, 2], [2, 1], [2, 2],
    [7, 7], [7, 8], [8, 7], [8, 8]
])

k = 2
epochs = 100

np.random.seed(0)
W = X[np.random.choice(len(X), k, replace=False)].astype(float)

for ep in range(epochs):
    lr = 0.5 * (1 - ep / epochs)
    for x in np.random.permutation(X):
        winner = np.argmin(((W - x) ** 2).sum(axis=1))
        W[winner] += lr * (x - W[winner])

labels = np.argmin(((X[:, None] - W) ** 2).sum(axis=2), axis=1)

for j in range(k):
    print(f"Cluster {j + 1}: patterns {np.where(labels == j)[0].tolist()}")
    print("Neuron weight:", W[j].round(2))

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=60)
plt.scatter(W[:, 0], W[:, 1], c="red", marker="X", s=200)
plt.title("Kohonen SOM Clustering")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

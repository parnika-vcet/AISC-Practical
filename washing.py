
import math
import matplotlib.pyplot as plt

def triangular(x, p):
    a, b, c = p
    if x <= a or x >= c:
        return 0
    elif x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

def trapezoidal(x, p):
    a, b, c, d = p
    if x <= a or x >= d:
        return 0
    elif x < b:
        return (x - a) / (b - a)
    elif x <= c:
        return 1
    else:
        return (d - x) / (d - c)

def gaussian(x, p):
    m, s = p
    return math.exp(-((x - m) ** 2) / (2 * s ** 2))

names = ["Lightly Soiled", "Moderately Soiled", "Heavily Soiled"]
tri_values = [[-50, 0, 50], [0, 50, 100], [50, 100, 150]]
trap_values = [[-10, 0, 20, 40], [20, 40, 60, 80], [60, 80, 100, 110]]
gauss_values = [[0, 20], [50, 15], [100, 20]]

value = float(input("Enter Dirt level (%) (0-100): "))

print("\nTriangular memberships")
for i in range(3):
    print(names[i], ":", f"{triangular(value, tri_values[i]):.2f}")

print("\nTrapezoidal memberships")
for i in range(3):
    print(names[i], ":", f"{trapezoidal(value, trap_values[i]):.2f}")

print("\nGaussian memberships")
for i in range(3):
    print(names[i], ":", f"{gaussian(value, gauss_values[i]):.2f}")

x_list = [x / 2 for x in range(201)]
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
titles = ["Triangular", "Trapezoidal", "Gaussian"]

for n in range(3):
    for i in range(3):
        if n == 0:
            y = [triangular(x, tri_values[i]) for x in x_list]
        elif n == 1:
            y = [trapezoidal(x, trap_values[i]) for x in x_list]
        else:
            y = [gaussian(x, gauss_values[i]) for x in x_list]
        axes[n].plot(x_list, y, label=names[i])

    axes[n].set_title(titles[n] + " Membership Function")
    axes[n].set_xlabel("Dirt Level (%)")
    axes[n].set_ylabel("Membership Value")
    axes[n].legend()
    axes[n].grid(True)

plt.tight_layout()
plt.show()

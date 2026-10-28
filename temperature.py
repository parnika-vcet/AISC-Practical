
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

names = ["Cold", "Comfortable", "Hot"]
tri_values = [[-10, 0, 20], [10, 22, 34], [24, 40, 56]]
trap_values = [[-10, 0, 10, 20], [15, 20, 26, 31], [26, 32, 45, 50]]
gauss_values = [[5, 6], [22, 4], [38, 6]]

value = float(input("Enter Temperature (°C) (0-40): "))

print("\nTriangular memberships")
for i in range(3):
    print(names[i], ":", f"{triangular(value, tri_values[i]):.2f}")

print("\nTrapezoidal memberships")
for i in range(3):
    print(names[i], ":", f"{trapezoidal(value, trap_values[i]):.2f}")

print("\nGaussian memberships")
for i in range(3):
    print(names[i], ":", f"{gaussian(value, gauss_values[i]):.2f}")

x_list = [x / 10 for x in range(401)]
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
    axes[n].set_xlabel("Temperature (°C)")
    axes[n].set_ylabel("Membership Value")
    axes[n].legend()
    axes[n].grid(True)

plt.tight_layout()
plt.show()

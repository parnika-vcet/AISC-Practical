inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

targets = [0, 1, 1, 1]

w1 = 0.1
w2 = 0.1
bias = 0.1

learning_rate = 0.1
max_epochs = 10000

for epoch in range(max_epochs):
    for i in range(len(inputs)):
        x1, x2 = inputs[i]
        target = targets[i]

        output = w1 * x1 + w2 * x2 + bias

        error = target - output

        w1 = w1 + learning_rate * error * x1
        w2 = w2 + learning_rate * error * x2
        bias = bias + learning_rate * error

    correct = True

    for i in range(len(inputs)):
        x1, x2 = inputs[i]
        net = w1 * x1 + w2 * x2 + bias
        predicted = 1 if net >= 0.5 else 0

        if predicted != targets[i]:
            correct = False
            break

    if correct:
        break

print("Final Weights:", round(w1, 4), round(w2, 4))
print("Final Bias:", round(bias, 4))
print("Number of Epochs:", epoch + 1)

print("\nOR Gate Truth Table")
print("X1 X2 Target Predicted")

for i in range(len(inputs)):
    x1, x2 = inputs[i]
    net = w1 * x1 + w2 * x2 + bias
    predicted = 1 if net >= 0.5 else 0

    print(x1, x2, targets[i], predicted)
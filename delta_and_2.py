
# AND Gate using Different Learning Rates
# Delta Learning Rule

inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

targets = [0, 0, 0, 1]

learning_rates = [0.1, 0.3, 0.5]
threshold = 0.5
max_epochs = 10000

def train_and_gate(lr):
    w1 = 0.1
    w2 = 0.1
    bias = 0.1

    for epoch in range(1, max_epochs + 1):
        dw1 = 0
        dw2 = 0
        db = 0

        for i in range(len(inputs)):
            x1, x2 = inputs[i]
            target = targets[i]

            output = w1 * x1 + w2 * x2 + bias
            error = target - output

            dw1 += error * x1
            dw2 += error * x2
            db += error

        w1 += lr * dw1 / len(inputs)
        w2 += lr * dw2 / len(inputs)
        bias += lr * db / len(inputs)

        predictions = []

        for x1, x2 in inputs:
            net = w1 * x1 + w2 * x2 + bias
            predictions.append(1 if net >= threshold else 0)

        if predictions == targets:
            return epoch, w1, w2, bias

    return None, w1, w2, bias

print("Learning Rate | Epochs | Final Weights | Bias")

results = []

for lr in learning_rates:
    epochs, w1, w2, bias = train_and_gate(lr)

    if epochs is not None:
        print(lr, "|", epochs, "|",
              round(w1, 4), round(w2, 4), "|", round(bias, 4))
        results.append((lr, epochs))
    else:
        print(lr, "| Not converged")

print("\nComparison:")

for lr, epochs in results:
    print("Learning rate", lr, "converged in", epochs, "epochs")

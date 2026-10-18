from l_02_dot_product import dot_product

# Matrix multiplication:
# (number of examples, number of features) × (number of features, number of outputs) = (number of examples, number of outputs)

# The first matrix's column count must equal the second matrix's row count.
# Each result comes from one input row's dot product with one weight column.

# Example: (100, 3) × (3, 2) = (100, 2)
# 100 deliveries, 3 features each, 2 predictions per delivery.


def predict_batch(
    deliveries: list[list[float]],
    weights: list[float]
) -> list[float]:
    # Calculate one dot product per delivery.
    # Return the predictions in the same order.
    prediction_batches: list[float]= []
    n = len(deliveries)

    for i in range(0, n):
        prediction_batches.append(dot_product(deliveries[i], weights))

    return prediction_batches


def matrix_multiply(
    inputs: list[list[float]],
    weights: list[list[float]]
) -> list[list[float]]:
    n: int = len(inputs[0])
    m: int = len(weights)

    if n != m:
        raise ValueError(f"metrics feature and it's weight length must be equal")

    predictions: list[list[float]] = []
    number_of_outputs = len(weights[0])

    for input_row in inputs:
        prediction = []
        for col in range(number_of_outputs):
            weight_column = [row[col] for row in weights]
            prediction.append(dot_product(input_row, weight_column))
        predictions.append(prediction)
    return predictions

    

if __name__ == "__main__":

    deliveries = [
        [5, 3],
        [2, 1],
        [8, 4],
    ]
    d_weights = [2, 4]
    print(f"prediction batches: {predict_batch(deliveries, d_weights)}")


    # inputs = [
    #     [5, 3],
    #     [2, 1],
    # ]

    # weights = [
    #     [2, 10],
    #     [4, 5],
    # ]

    inputs = [
        [5, 3],
        [2, 1],
    ]  # shape (2, 2)

    weights = [
        [2, 10, 1],
        [4,  5, 2],
    ]  # shape (2, 3)
    print(f"matrix multiply: {matrix_multiply(inputs, weights)}")
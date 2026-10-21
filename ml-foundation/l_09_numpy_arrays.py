import numpy as np

values = np.array([1, 2, 3])
print(values * 2)
print(values + 10)


deliveries = np.array([
    [5, 3],
    [2, 1],
    [8, 4],
])
# Columns: distance_km, number_of_stops

print(f"shape: {deliveries.shape}")

print(f"first row: {deliveries[0]}")     # First row: [5, 3]
print(f"first row, second col {deliveries[0, 1]}")  # First row, second column: 3
print(f"first col: {deliveries[:, 0]}")  # Every row, first column: [5, 2, 8]
# : means take all the row and select 0 columns. 

#2. boolean indexing

distances = deliveries[:, 0]  # [5, 2, 8]
mask = distances > 4         # [True, False, True]

long_deliveries = deliveries[mask]

print(f"long deliveries {long_deliveries}")

#3. reshaping
values = np.array([1, 2, 3, 4, 5, 6])

matrix = values.reshape(3, 2)
# [[1, 2],
#  [3, 4],
#  [5, 6]]

print(f"auto shape: {values.reshape(2, -1)}") # This means: “Make 2 rows and work out how many columns are needed.”
                                              # With 6 elements, that gives shape (2, 3).


#3. broadcasting: NumPy applies [10, 100] to each row: add 10 to the first column and 100 to the second.

numbers = np.array([[1, 2], [3, 4]])

print(f"Add 5 everywhere \n {numbers + 5}")        # Add 5 everywhere
print(f"Add 5 to col0 and 20 to col1 \n {numbers + [10, 20]}") # Add 10 to column 0, 20 to column 1


adjustments = np.array([
    [10],
    [20],
])

print(f"adjusment \n {numbers + adjustments}")

deliveries = np.array([
    [5, 3],
    [2, 1],
    [8, 4],
])

adjustments = np.array([[10], [20], [30]])

result = deliveries + adjustments
print(f"adjusment2 \n {result}")
print(f"adjusment2 shape \n {result.shape}")
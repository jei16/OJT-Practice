query = [
    ("REG", "BUTTER CAKE SLICE", "2023-09-23", 5, 1, 2, 3, 4, 5),
    ("REG", "BUTTER CAKE SLICE", "2023-09-24", 5, 11, 12, 13, 14, 15),
    ("REG", "BUTTER CAKE SLICE", "2023-09-26", 5, 111, 112, 113, 114, 115),
    ("REG", "BANANA CAKE SLICE", "2023-09-23", 5, 21, 22, 23, 24, 25),
    ("REG", "BANANA CAKE SLICE", "2023-09-24", 5, 31, 32, 33, 34, 35),
    ("REG", "BANANA CAKE SLICE", "2023-09-25", 5, 41, 42, 43, 44, 45),
    ("REG", "BACON ENSAYMADA", "2023-09-23", 1, 51, 52, 53, 54, 55),
    ("REG", "BACON ENSAYMADA", "2023-09-26", 1, 61, 62, 63, 64, 65),
]

distinct_values = set()  # Create an empty set to store distinct values from info[3]

for info in query:
    distinct_values.add(info[2])  # Add info[3] to the set

distinct_count = len(distinct_values)  # Get the count of distinct values

print(f"Distinct values in info[3]: {distinct_count}")
print(sorted(distinct_values))
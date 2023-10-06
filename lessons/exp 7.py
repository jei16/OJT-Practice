from collections import defaultdict

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

psr_data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

# Create a dictionary to store data for each item, date, and category
for info in query:
    category = info[3]
    item = info[1]
    date = info[2]
    for i, value in enumerate(info[4:9]):
        psr_data[category][item][date].append(value)

# Extract distinct dates from the data
distinct_dates = sorted(list(set(info[2] for info in query)))

# Ensure each item, category, and date has data and fill missing dates with zeros
for category_data in psr_data.values():
    for item_data in category_data.values():
        for date in distinct_dates:
            if date not in item_data:
                item_data[date] = [0, 0, 0, 0, 0]

# Convert the data into the specified format with missing dates filled with zeros
result = []
for category, item_data in psr_data.items():
    category_info = [category]
    item_info = []
    for item, date_data in item_data.items():
        item_info.append((item, tuple(date_data[date] for date in distinct_dates)))
    category_info.append(item_info)
    result.append(category_info)

# Group the 1st, 2nd, 3rd, 4th, and 5th sub-tuples within each tuple
final_result = []
for category_info in result:
    grouped_data = [category_info[0]]
    for item_info in category_info[1]:
        grouped_item_info = (item_info[0], tuple(zip(*item_info[1])))
        grouped_data.append(grouped_item_info)
    final_result.append(grouped_data)

print(final_result)

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
    ("REG", "BACON ENSAYMADA", "2023-09-29", 1, 61, 62, 63, 64, 65),
    ("REG", "BACON ENSAYMADA", "2023-09-30", 14, 61, 62, 63, 64, 65),
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

# Convert the result to the desired format
formatted_result = []
for category_info in final_result:
    formatted_category_info = [category_info[0]]
    for item_info in category_info[1:]:
        formatted_item_info = [item_info[0]]
        for sub_tuple in item_info[1]:
            formatted_item_info.extend(sub_tuple)
        formatted_category_info.append(tuple(formatted_item_info))
    formatted_result.append(formatted_category_info)


# print(formatted_result[0][1][2])

for category in formatted_result:
    if len(category) <= 2:
        category.append(('TOTAL',*category[1][1:]))
    else:
        total_values = [0] * (len(category[1])-1)  # Initialize with zero

        for multi_item in range(1, len(category)):
            # print(category[multi_item])
            item_info = category[multi_item][1:]
            # print(item_info)
            # Sum the values from each item's tuples
            total_values = tuple(x + y for x, y in zip(total_values, item_info))
            print(total_values)
            
                
            # Append the "TOTAL" tuple with summed values to the category
        category.append(('TOTAL', total_values))


print(formatted_result)
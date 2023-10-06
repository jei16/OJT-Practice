# filter_list=["hdr.ttyp = 'a'","hdr.ttyp = 'b'","hdr.ttyp = 'c'"]
# updated_filter = []

# for i, query in enumerate(filter_list):
#     keyword, _ = query.split(' ', 1)
#     if keyword not in [" "]:
#         #Add an ADD operator until the last element
#         updated_query = f"{query}" if i == len(filter_list) - 1 else f"{query} AND"
#         #Insert the value for every iteration
#         updated_filter.append(updated_query)

# print(updated_filter)

# query = [
#     ("REG", "BUTTER CAKE SLICE", "2023-09-23", 5, 1, 2, 3, 4, 5),
#     ("REG", "BUTTER CAKE SLICE", "2023-09-24", 5, 1, 2, 3, 4, 5),
#     ("REG", "BANANA CAKE SLICE", "2023-09-23", 5, 1, 2, 3, 4, 5),
#     ("REG", "BANANA CAKE SLICE", "2023-09-24", 5, 1, 2, 3, 4, 5),
#     ("REG", "BANANA CAKE SLICE", "2023-09-25", 5, 1, 2, 3, 4, 5),
#     ("REG", "BACON ENSAYMADA", "2023-09-23", 1, 1, 2, 3, 4, 5),
#     ("REG", "BACON ENSAYMADA", "2023-09-24", 1, 1, 2, 3, 4, 5),
# ]


# psr_data = []

# for info in range(len(query)):
#     psr_data.append((query[info][1], query[info][2], query[info][3]))

# print(psr_data)
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

psr_data = {}


for info in query:
    item = info[1]  # Use the second element as the key
    if item in psr_data:
        # If the key already exists, combine the tuples by concatenating values
        existing_tuple = psr_data[item]
        new_tuple = (
            item,
            existing_tuple[1] + (info[4],),  # Concatenate info[4] values
            existing_tuple[2] + (info[5],),  # Concatenate info[5] values
            existing_tuple[3] + (info[6],),  # Concatenate info[6] values
            existing_tuple[4] + (info[7],),  # Concatenate info[7] values
            existing_tuple[5] + (info[8],),  # Concatenate info[8] values
        )
        psr_data[item] = new_tuple
    else:
        # If the key does not exist, create a new entry in the dictionary
        psr_data[item] = (
            item,
            (info[4],),  # Create a tuple for info[4]
            (info[5],),  # Create a tuple for info[5]
            (info[6],),  # Create a tuple for info[6]
            (info[7],),  # Create a tuple for info[7]
            (info[8],),  # Create a tuple for info[8]
        )

# Convert the dictionary values to a list of tuples
psr_data = list(psr_data.values())

print(psr_data)
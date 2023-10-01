filter_list=["hdr.ttyp = 'a'","hdr.ttyp = 'b'","hdr.ttyp = 'c'"] 
updated_filter = []

for i, query in enumerate(filter_list): 
    keyword, _ = query.split(' ', 1)
    if keyword not in [" "]:
        #Add an ADD operator until the last element
        updated_query = f"{query}" if i == len(filter_list) - 1 else f"{query} AND"
        #Insert the value for every iteration 
        updated_filter.append(updated_query)

print(updated_filter)

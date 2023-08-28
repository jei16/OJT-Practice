courses = ["bsit", "bscs", "bscpe", "computer", "goldilocks", "bscs"]
# replace
courses[0] = "OJT"
# length
print(len(courses))
# count
print(courses.count("bscs"))
# add
courses.append("hrm")
print(courses)
# insert
courses.insert(2, "bsa")
print(courses)
# delete
courses.remove("bscs")
print(courses)
# pop- blank, deletes last part
courses.pop()
courses.pop(0)
print(courses)
# del- blank, deletes all (inaccessible)
# del courses
# print(courses)

# clear
courses.clear()
courses.append("it")
courses.append("com sci")
print(courses)

# copy
course2 = courses.copy()

# add
print(course2 + courses + ["courses"])

# extend
courses.extend(course2)
print(courses)

# reverse
courses.reverse()
print(courses)

# sort
alp = ["Z", "A", "C", "B"]
alp.sort()
print(alp)
alp.sort(reverse=True)
print(alp)

# nested list
wew = ["1", "2", "3", ["4", "5"]]
print(wew[3])
print(wew[3][1])
wewz = ["1", "2", "3", ["4", ["6", "7"], "5"]]
print(wewz[3][1][1])

# tuples
pi = (3, 1, 4)
print(pi[1])
# pi.append("hello")
print(list(pi))
print(max(pi))
pi2 = [3, 1, 4]
print(tuple(pi2))


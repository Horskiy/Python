print("Hello world!")

#Task 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for elem in a:
    if elem < 5:
        print(elem)

print(list(filter(lambda elem: elem < 5, a)))

print([elem for elem in a if elem < 5])

#Task 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = list(set(a) & set(b))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result1 = list(filter(lambda elem: elem in b, a))

#Task 3

my_dict = {'a': 4, 'c': 1, 'b': 2, 'd': 3}

print(sorted(my_dict.items(), key=lambda item: item[1]))

#Task4




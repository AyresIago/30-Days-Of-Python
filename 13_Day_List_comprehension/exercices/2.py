list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten = [i for number in list_of_lists for i in number]
print(flatten)
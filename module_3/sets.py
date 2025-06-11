my_set = {1, 2, 3}

my_set1 = set([4, 5, 6])

my_set2 = set()

my_set3 = {1, 2, 2, 3, 3, 3, 3}
print(my_set3)


set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_result_method = set1.union(set2)
union_result_operator = set1 | set2

print(union_result_method)
print(union_result_operator)


#intersection
intersection_result_method = set1.intersection(set2)
intersection_result_operator = set1 & set2

print(intersection_result_method)
print(intersection_result_operator)

#difference
difference_result_method = set1.difference(set2)
difference_result_operator = set1 - set2

print(difference_result_method)
print(difference_result_operator)

#symetric
symetric_result_method = set1.symetric_difference(set2)
symetric_result_operator = set1 ^ set2

print(symetric_result_method)
print(symetric_result_operator)






























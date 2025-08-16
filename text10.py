def find_single_occurrence_number(numbers: list) -> list:
    same = []
    for i in numbers:
        if numbers.count(i) == 1:
            same.append(i)
    return same


        

print(find_single_occurrence_number([4, 5, 6, 4, 7, 5, 8]))
print(find_single_occurrence_number([1, 2, 2, 3, 3, 4, 4]))
print(find_single_occurrence_number([1, 2, 3, 4, 5, 6 ]))
print(find_single_occurrence_number([1, 1, 1, 1, 1]))
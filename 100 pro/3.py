def find_non_multiples(start: int, end: int) -> list:
    num_list = []

    if start >= end:
            return num_list
    
    for i in range(start, end + 1):
        if i % 3 != 0 and i % 4 != 0 and i % 5 != 0:
            num_list.append(i)
    return num_list  

print(find_non_multiples(start = 10, end=25))
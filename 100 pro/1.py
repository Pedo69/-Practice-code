def find_multiples_of_three(start: int, end: int) -> list:
    num_list = []

    if start >= end:
            return num_list
    
    for i in range(start, end):
        if i % 3 == 0:
            num_list.append(i)
    return num_list  

print(find_multiples_of_three(start = 10, end=25))
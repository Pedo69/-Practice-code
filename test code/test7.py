def filter_prime(nums):
    prime = []
    for i in nums:
        if i % 2 != 0:
            prime.append(i)
        elif i == 2:
            prime.append(i)
    return prime 
            

print(filter_prime([3, 11, 17, 20, 23, 29, 8, 2, 31, 40]))
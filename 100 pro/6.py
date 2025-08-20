def reverse_string(s: str) -> str:
    result = list(s)
    result.reverse()
    result_list = ''.join(result)
    return result_list

print(reverse_string("Hello World"))

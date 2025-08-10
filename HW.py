def format_strings(*args):
    tex_string = ''.join(args)
    string_upper = tex_string.upper()
    formatted_string = string_upper.replace(' ', '')
    return formatted_string


if __name__ == '__main__':
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result)  # Output: "PYTHONISFUN"

    result = format_strings("Hello world")
    print(result)  # Output: "HELLO-WORLD"
def replace_charecter(s: str) -> str:
    text_string = s
    format_string = text_string.replace("a", "@").replace('l', '1').replace('o', '0')

    return format_string
            
print(replace_charecter("Hallo World"))
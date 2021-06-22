def multi_bracket_validation(str_input):
    
    if '(' in str_input and ')' in str_input:
        return True
    if '{' in str_input and '}' in str_input:
        return True

    elif '[' in str_input and ']' in str_input:
        return True

    else:
        return False
   
    
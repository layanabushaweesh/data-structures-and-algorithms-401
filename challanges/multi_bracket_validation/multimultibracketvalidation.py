def multi_bracket_validation(str_input):
    
    # if '(' in str_input and ')' in str_input:
    #     return True
    # if '{' in str_input and '}' in str_input:
    #     return True

    # elif '[' in str_input and ']' in str_input:
    #     return True

    # else:
    #     return False

   # define empty list
    list = [] #list is as stack
    #define bracket as an object have key for close bracket and value of open
    # open_brachet = ['(', '[' ,'{']
    # close_bravhrt=[')' ,']' ,'}']
    brackets = {'}':'{', ']':'[', ')':'('}
    #{key:value ,..}
    for braket in str_input: 
        # check open bracket add it to list
        if braket in brackets.values(): 
            list.append(braket)
        # check closed bracket
        if braket in brackets.keys(): 
            bracket = list.pop() 
            if brackets[braket] != bracket:
                return False
    # if list still have charachter return false
    if list:
        return False
    return True
#    stak =[]


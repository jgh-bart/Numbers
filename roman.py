import re
import numbers

def roman_numeral_valid(roman_string):
    '''checks the validity of a string as a Roman numeral'''
    validity = False
    # traditional Roman numeral
    # permitted subtractions: CM, CD, XC, XL, IX, IV
    if re.match(r'^(M{1,4}(CM|CD|DC{0,4}|C{1,4})?(XC|XL|LX{0,4}|X{1,4})?(IX|IV|VI{0,4}|I{1,4})?)$|^((CM|CD|DC{0,4}|C{1,4})(XC|XL|LX{0,4}|X{1,4})?(IX|IV|VI{0,4}|I{1,4})?)$|^((XC|XL|LX{0,4}|X{1,4})(IX|IV|VI{0,4}|I{1,4})?)$|^(IX|IV|VI{0,4}|I{1,4})$', roman_string):
        print roman_string, '- MATCH: traditional Roman numeral'
        validity = True
    # Roman numeral with all subtractions permitted:
    # [C,L,X,V,I] from [M,D]; [X,V,I] from [C,L], IX, IV
    elif re.match(r'^(M{1,4}([CLXVI][MD]|DC{0,4}|C{1,4})?([XVI][CL]|LX{0,4}|X{1,4})?(IX|IV|VI{0,4}|I{1,4})?)$|^(([CLXVI][MD]|DC{0,4}|C{1,4})([XVI][CL]|LX{0,4}|X{1,4})?(IX|IV|VI{0,4}|I{1,4})?)$|^(([XVI][CL]|LX{0,4}|X{1,4})(IX|IV|VI{0,4}|I{1,4})?)$|^(IX|IV|VI{0,4}|I{1,4})$', roman_string):
        print roman_string, '- MATCH: Roman numeral with alternative subtractions'
        validity = True
    else:
        print roman_string, '- NO MATCH'
    return validity

def roman_numeral_to_number(roman_string):
    '''calculates the value of a Roman numeral'''
    numeral_value = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for idx in range(len(roman_string)):
        # last numeral: add value
        if idx == len(roman_string) - 1:
            total += numeral_value[roman_string[idx]]
        # all other numerals: subtract value if less than
        # following numeral, otherwise add value
        else:
            if numeral_value[roman_string[idx]] < numeral_value[roman_string[idx + 1]]:
                total -= numeral_value[roman_string[idx]]
            else:
                total += numeral_value[roman_string[idx]]
    return total

def roman_numeral_program():
    text_input = input('Roman numeral input: ')
    if roman_numeral_valid(text_input):
        roman_numeral_value = roman_numeral_to_number(text_input)
        print 'VALUE:      ', roman_numeral_value
        print 'NUMBER:     ', numbers.num_to_word_seq(roman_numeral_value)
        print 'ORDINAL:    ', numbers.num_string_to_ordinal(str(roman_numeral_value))
        print 'DEF.ORDINAL:', ['the'] + numbers.num_string_to_ordinal(str(roman_numeral_value))
        print 'CHUNKED NUM:', numbers.num_string_to_chunked_num(str(roman_numeral_value))

numbers_dict = {0: 'zero',
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten',
                11: 'eleven',
                12: 'twelve',
                13: 'thirteen',
                14: 'fourteen',
                15: 'fifteen'}
tens_dict    = {2: 'twenty',
                3: 'thirty',
                4: 'forty',
                5: 'fifty',
                6: 'sixty',
                7: 'seventy',
                8: 'eighty',
                9: 'ninety'}

def num_to_word_seq(number):
    if number < 0:
        return ['minus'] + num_to_word_seq(abs(number))
    elif number <= 15:
        return [numbers_dict[number]]
    elif number <= 19:
        return [numbers_dict[number - 10] + 'teen']
    elif number < 100:
        if number % 10 == 0:
            return [tens_dict[number // 10]]
        else:
            return [tens_dict[number // 10], numbers_dict[number % 10]]
    elif number < 1000:
        if number % 100 == 0:
            return [numbers_dict[number // 100], 'hundred']
        else:
            return [numbers_dict[number // 100], 'hundred', 'and'] + num_to_word_seq(number % 100)
    else:
        output = []
        if number >= 1000000000:
            output += num_to_word_seq(number // 1000000000) + ['billion']
        if (number % 1000000000) >= 1000000:
            output += num_to_word_seq((number % 1000000000) // 1000000) + ['million']
        if (number % 1000000) >= 1000:
            output += num_to_word_seq((number % 1000000) // 1000) + ['thousand']
        if (number % 1000) > 0:
            if (number % 1000) < 100:
                output.append('and')
            output += num_to_word_seq((number % 1000))
        return output

def num_string_to_word_seq(number_string):
    return num_to_word_seq(int(number_string))

def num_string_to_ordinal(number_string):
    word_seq = num_to_word_seq(int(number_string))
    # replace last word with ordinal equivalent: first, second, third
    dict_123 = {'one': 'first', 'two': 'second', 'three': 'third'}
    if word_seq[-1] in dict_123:
        output = word_seq[:-1] + [dict_123[word_seq[-1]]]
    # replace last word with ordinal equivalent: -th forms
    else:
        output = word_seq[:]
        # deletion: 't' (8th), 'e' (9th)
        set_delete = set(['t', 'e'])
        if word_seq[-1][-1] in set_delete:
            output[-1] = word_seq[-1][:-1]
        # assimilation: 've'>'f' (5th, 12th), 'ty'>'tie' (20th etc)
        dict_assim = {'ve': 'f', 'ty': 'tie'}
        if word_seq[-1][-2:] in dict_assim:
            output[-1] = word_seq[-1][:-2] + dict_assim[word_seq[-1][-2:]]
        # append 'th'
        output[-1] += 'th'
    return output

def num_string_to_digits(number_string, zero_word = 'zero'):
    if number_string[0] == '-':
        return ['minus'] + num_string_to_digits(number_string[1:])
    else:
        output = []
        for digit in number_string:
            # for "0", use zero_word
            if digit == '0':
                output.append(zero_word)
            else:
                output.append(numbers_dict[int(digit)])
        return output

def num_string_to_chunked_num(number_string):
    if number_string[0] == '-':
        return ['minus'] + num_string_to_chunked_num(number_string[1:])
    if number_string == '0':
        return ['zero']
    else:
        # split number string into list of 2-digit units
        chunk = []
        while len(number_string) > 0:
            chunk.insert(0, number_string[-2:])
            number_string = number_string[:-2]
        # each 2-digit unit to word sequence
        output = []
        for idx in range(len(chunk)):
            # '00': 'double oh' if leading, else 'hundred'
            if chunk[idx] == '00':
                if idx == 0:
                    output += ['double', 'oh']
                else:
                    output.append('hundred')
            # '0': 'oh'
            elif chunk[idx] == '0':
                output.append('oh')
            # otherwise 'oh' (if 1st digit '0'), number
            else:
                if chunk[idx][0] == '0':
                    output.append('oh')
                output += num_string_to_word_seq(chunk[idx])
        return output

def run_programme():
    num_input = input('numerical input: ')
    print 'INPUT:      ', num_input
    print 'NUMBER:     ', num_string_to_word_seq(num_input)
    print 'ORDINAL:    ', num_string_to_ordinal(num_input)
    print 'DIGITS:     ', num_string_to_digits(num_input, zero_word = 'zero')
    print 'CHUNKED NUM:', num_string_to_chunked_num(num_input)

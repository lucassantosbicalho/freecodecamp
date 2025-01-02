def is_operator_valid(problem):
    return problem.split(' ')[1] in ['+', '-']

def is_operand_valid(problem):
    result = list(map(lambda x: x.isdigit(), problem.split(' ')[0:3:2]))
    return result[0] and result[1]

def is_operand_four_digit_max(problem):
    result = list(map(lambda x: len(x) < 5, problem.split(' ')[0:3:2]))
    return result[0] and result[1]

def arithmetic_arranger(problems, show_answers=False):
    l1 = ''; l2 = ''; l3 = ''; l4 = ''; res = '';

    # Validations
    if len(problems) > 5:
        return ('Error: Too many problems.')
        
    for _ in problems:
        if not is_operator_valid(_):
            return (f"Error: Operator must be '+' or '-'.") 
        if not is_operand_valid(_):
            return ('Error: Numbers must only contain digits.')
        if not is_operand_four_digit_max(_):
            return ('Error: Numbers cannot be more than four digits.')
    
        elements = _.split(' ')
        numerator = elements[0]
        denominator = elements[2]
        operator = elements[1]
        lens = max(len(elements[0]), len(elements[2]))
        dashes = ('-' * (lens + 2))
        space_1 = " "*(len(numerator) - len(denominator) + 1)
        space_2 = " "*(len(denominator) - len(numerator) + 2)
    
        if len(numerator) == len(denominator):
            l1 += '  ' + numerator + '    '
            l2 += operator + ' ' + denominator + '    '
            l3 += dashes + '    '
        elif len(numerator) > len(denominator):
            l1 += '  ' + numerator + '    '
            l2 += operator + space_1 + denominator + '    '
            l3 += dashes + '    '
        else:
            l1 += space_2 + numerator + '    '
            l2 += operator + ' ' + denominator + '    '
            l3 += dashes + '    '

        res = str(eval(f'{numerator} {operator} {denominator}')) 
        l4 += " "*(len(dashes) - len(res)) + res + '    '

    l1 = l1.rstrip()
    l2 = l2.rstrip()
    l3 = l3.rstrip()
    l4 = l4.rstrip()
        
    return (f'{l1}\n{l2}\n{l3}\n{l4}') if show_answers else (f'{l1}\n{l2}\n{l3}')


def arithmetic_arranger_refactored(problems, show_answers=False):
    top = []
    bottom = []
    dashes = []
    results = []

    if len(problems) > 5:
        return ('Error: Too many problems.')
    
    for _ in problems:
        numerator, operator, denominator = _.split()

        if not operator in '+-':
            return (f"Error: Operator must be '+' or '-'.")
        
        if not (numerator.isdigit() and denominator.isdigit()):
            return ('Error: Numbers must only contain digits.')
        
        if not (len(numerator) < 5 and len(denominator) < 5):
            return ('Error: Numbers cannot be more than four digits.')
        
        width = max(len(numerator), len(denominator)) + 2
        top.append(numerator.rjust(width))
        bottom.append(operator + ' ' + denominator.rjust(width - 2))
        dashes.append('-' * width)

        if show_answers:
            results.append((str(eval(f'{numerator} {operator} {denominator}'))).rjust(width))

    arr_results = [
        '    '.join(top),
        '    '.join(bottom),
        '    '.join(dashes)
    ]

    if show_answers:
        arr_results.append('    '.join(results))

    return '\n'.join(arr_results)

if __name__ == '__main__':
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 - 4911"]
    print('arithmetic_arranger(problems, show_answers=True)\n')
    print(arithmetic_arranger(problems, show_answers=True))
    print('arithmetic_arranger_refactored(problems, show_answers=True)\n')
    print(arithmetic_arranger(problems, show_answers=True))

    ''' 
    python3 build-an-arithmetic-formatter-project.py
    arithmetic_arranger(problems, show_answers=True)

    32      3801      45       123
    + 698    -    2    + 43    - 4911
    -----    ------    ----    ------
    730      3799      88     -4788
    arithmetic_arranger_refactored(problems, show_answers=True)

    32      3801      45       123
    + 698    -    2    + 43    - 4911
    -----    ------    ----    ------
    730      3799      88     -4788
    '''
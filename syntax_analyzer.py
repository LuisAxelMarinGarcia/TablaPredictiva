predictive_table = {
    ('S', '{'): ['I', 'M', 'A', 'F'],
    ('A', ';'): [';', 'M', 'A'],
    ('A', '}'): ['epsilon'],
    ('M', 'displayData'): ['D', '(', 'C', ')'],
    ('D', 'displayData'): ['displayData'],
    ('C', '“'): ['“', 'T', '”'],  
    ('I', '{'): ['{'],
    ('F', '}'): ['}'],
    ('T', 'a..z'): ['L', 'R'],
    ('L', 'a..z'): ['a..z', 'R'],  
    ('R', 'a..z'): ['L', 'R'],    
    ('R', ')'): ['epsilon'],       
    ('R', '}'): ['epsilon'],        
    ('R', '”'): ['epsilon'],        
    ('R', '$'): ['epsilon'],
}
terminal_symbols = {key[1] for key in predictive_table.keys()}

def input_transformer(input_str):
    processed_symbols = []
    replaced_input = input_str.replace('{}', ' {} ').replace('(', ' ( ').replace(')', ' ) ')
    elements = replaced_input.split()

    for element in elements:
        if element in terminal_symbols or element == 'displayData':
            processed_symbols.append(element)
        else:
            processed_symbols.extend(['a..z' if char.isalpha() else char for char in element])
    return processed_symbols + ['$']

def syntax_analyzer(input_str):
    stack = ['$', 'S']
    log = [' '.join(stack)]
    input_symbols = input_transformer(input_str.strip())

    while stack and input_symbols:
        stack_top = stack[-1]
        current_input = input_symbols[0]

        if stack_top == current_input:
            stack.pop()
            input_symbols.pop(0)
        elif (stack_top, current_input) in predictive_table:
            stack.pop()
            production_elements = predictive_table[(stack_top, current_input)]
            if production_elements != ['epsilon']:
                stack.extend(reversed(production_elements))
        else:
            return '\n'.join(log) + f'\nError near input "{current_input}"'
        log.append(' '.join(stack) if stack else 'Aceptado')

    return '\n'.join(log)
def extract_command(text: str, start_str: str, stop_char: str = ';') -> str | None:
    try:
        start_index = text.index(start_str) + len(start_str)
    except ValueError:
        return None
    end_index = text.find(stop_char, start_index)
    return text[start_index:] if end_index == -1 else text[start_index:end_index]

def evaluate_expression(expr: str, variables: dict):
    """
    Replaces variable names with their values and evaluates the expression safely.
    """
    # Replace variables with their values
    tokens = expr.split()
    replaced = []
    for token in tokens:
        if token in variables:
            replaced.append(variables[token])
        else:
            replaced.append(token)
    safe_expr = " ".join(replaced)
    
    # Only allow safe characters
    allowed = "0123456789+-*/(). "
    if any(c not in allowed for c in safe_expr):
        raise ValueError("Invalid characters in expression.")
    
    return eval(safe_expr)

variables = {}

filename = input("BlueSpruce File Path: ")
if '.bluespruce' in filename:
    with open(filename) as f:
        for line in f:
            line = line.strip()

            # Variable assignment
            if line.startswith('let '):
                declaration = extract_command(line, 'let ', ';')
                if declaration and '=' in declaration:
                    var_name, value = declaration.split('=')
                    variables[var_name.strip()] = value.strip()

            # Print expression or variable
            elif line.startswith('print '):
                expr = extract_command(line, 'print ', ';')
                if expr:
                    try:
                        result = evaluate_expression(expr.strip(), variables)
                        print(result)
                    except Exception as e:
                        print(f"Error evaluating expression '{expr.strip()}':", e)
else:
    print('Wrong filetype.')

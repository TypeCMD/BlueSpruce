def add(n1, n2, variables):
    # Resolve variables if needed
    n1 = int(variables.get(n1, n1))
    n2 = int(variables.get(n2, n2))
    return n1 + n2

def extract_command(text: str, start_str: str, stop_char: str = ';') -> str | None:
    try:
        start_index = text.index(start_str) + len(start_str)
    except ValueError:
        return None
    end_index = text.find(stop_char, start_index)
    return text[start_index:] if end_index == -1 else text[start_index:end_index]

variables = {}
result = None

filename = f"/{input("BlueSpruce File Path: ")}"
if '.bluespruce' in filename:
    with open(filename) as f:
        for line in f:
            line = line.strip()

            # Handle variables: let x = 10;
            if line.startswith('let '):
                try:
                    declaration = extract_command(line, 'let ', ';')
                    var_name, value = declaration.split('=')
                    variables[var_name.strip()] = value.strip()
                except:
                    print("Invalid variable declaration.")

            # Handle addition: add x y;
            elif line.startswith('add '):
                text = extract_command(line, 'add ', ';')
                if text:
                    parts = text.strip().split()
                    if len(parts) == 2:
                        result = add(parts[0], parts[1], variables)
                    else:
                        print("Error: add requires two arguments.")

            # Handle printing
            elif line.startswith('print '):
                text = extract_command(line, 'print ', ';')
                if text.strip() == "result":
                    print(result)
                elif text.strip() in variables:
                    print(variables[text.strip()])
                else:
                    print(text)
else:
    print('Wrong filetype.')

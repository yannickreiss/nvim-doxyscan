import re

def get_functions(buff_txt):

    lines = buff_txt.split("\n")

    functions = []
    function_line_numbers = []
    line_counter = 1
    documentations = []

    fn_documentation = {
        "name": "-",
        "return": "-",
        "brief": "-",
        "param": []
    }

    for line in lines:

        pm = re.search(r"@(\w+) ([^\n]+)", line)
        if pm:
            key = pm.group(1)
            target = pm.group(2)

            # Commit last documentation and restart
            if key == "name":
                functions.append(target)
                function_line_numbers.append(line_counter)

                if len(functions) > len(documentations):
                    documentations.append(fn_documentation)
                    fn_documentation = {
                        "name": target,
                        "return": "-",
                        "brief": "-",
                        "param": []
                    }
            else:
                if key == "param":
                    fn_documentation[key].append(target)
                else:
                    fn_documentation[key] = target

        line_counter += 1

    if len(functions) > len(documentations):
        documentations.append(fn_documentation)

    status = f"Detected functions in buffer: {len(functions)}\n\n"

    for i in range(len( function_line_numbers )):
        status += f"> {function_line_numbers[i]}:{' ' * (7-len(str( function_line_numbers[i] )))}{functions[i]}\n"

    return status

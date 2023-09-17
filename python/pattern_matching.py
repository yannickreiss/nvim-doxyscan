import re


def get_functions(buff_txt):

    lines = buff_txt.split("\n")

    functions = []
    fln = []  # function_line_numbers
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
                if len(functions) > 0:
                    documentations.append(fn_documentation)
                functions.append(target)
                fln.append(line_counter)

                fn_documentation = {
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

    if len(functions) > 0:
        documentations.append(fn_documentation)

    status = f"Detected functions in buffer: {len(functions)}\n\n"

    for i in range(len(fln)):
        status += f"> {fln[i]}:{' ' * (7-len(str( fln[i] )))}{functions[i]}\n"
        status += f"  {' ' * 8} Return: {documentations[i]['return']}\n"
        status += f"  {' ' * 8} Parameters:"

        pid = 1
        for parameter in documentations[i]['param']:
            if len(documentations[i]['param']) > 0 and pid > 1:
                status += " •"

            ptmp = parameter.replace('\t', ' ')
            status += f" {ptmp}"
            pid = 2

        status += "\n"

        status += f"  {' ' * 8} {documentations[i]['brief']}\n\n"

    return status

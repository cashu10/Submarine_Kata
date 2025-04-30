def parseLine(input_string):
    if not input_string.strip():
        return []
    output = []
    command, value = input_string.strip().split()
    output.append({"command": command, "value": int(value)})

    return output

def parseInputs(input_string):
    lines = input_string.strip().split("\n")
    output = []

    for line in lines:
        output.extend(parseLine(line))

    return output

        
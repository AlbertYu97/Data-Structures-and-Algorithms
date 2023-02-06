def reverse(string):
    # Check input type
    if not isinstance(string, str):
        return "input has to be string"

    string_reversed = ''
    for index in range(len(string) - 1, -1, -1):
        string_reversed = string_reversed + string[index]
    return string_reversed


def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    solution = list(phrase)
    solution.reverse()
    str = ""
    for char in solution:
        str += char
    return (str)



reverse_string("helloLord")
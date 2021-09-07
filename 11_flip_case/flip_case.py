def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    if to_swap.islower():
        return phrase.replace(to_swap, "%temp%").replace(to_swap.upper(), to_swap).replace("%temp%", to_swap.upper())
    else:
        return phrase.replace(to_swap, "%temp%").replace(to_swap.lower(), to_swap).replace("%temp%", to_swap.lower())
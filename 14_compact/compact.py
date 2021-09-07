def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    lst1 = lst.copy()
    for el in lst1:
        if (bool(el) == False):
            lst.remove(el)

    return lst 
def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    dict = {}
    k, v = len(keys), len(values)
    if k < v:
        i = 0
        for key in keys:
            dict[key] = values[i]
            i += 1
        return dict
    elif k > v:
        i = 0
        for val in values:
            dict[keys[i]] = val
            i += 1
        while i < len(keys):
            dict[keys[i]] = None
            i += 1
        return dict
    else:
        i = 0
        for val in values:
            dict[keys[i]] = val
            i += 1
        return dict
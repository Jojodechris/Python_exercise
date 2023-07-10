def compact(lst):
    """Return a copy of lst with non-true elements removed.

    >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
    [1, 2, 'All done']
    """
    copy_list = []
    for element in lst:
        if bool(element):
            copy_list.append(element)
    return copy_list


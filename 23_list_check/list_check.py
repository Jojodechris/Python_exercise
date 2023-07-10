def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

   for items in lst:
        if not isinstance(items, list):  # Check if the item is not a list
            return False
    return True
    
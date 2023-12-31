def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
count = 0
for term in lst :
    if term == search_term :
        count += 1   # increment the counter for each occurrence of 'search_term' found
return count 
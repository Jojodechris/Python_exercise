def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    def same_frequency(num1, num2):
    """Do these nums have the same frequencies of digits?

    >>> same_frequency(551122, 221515)
    True

    >>> same_frequency(321142, 3212215)
    False

    >>> same_frequency(1212, 2211)
    True
    """
    # Convert numbers to strings for easier manipulation
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Check if the lengths of the number strings are equal
    if len(str_num1) != len(str_num2):
        return False

    # Count the frequencies of digits in the first number
    num1_freq = {}
    for digit in str_num1:
        num1_freq[digit] = num1_freq.get(digit, 0) + 1

    # Count the frequencies of digits in the second number
    num2_freq = {}
    for digit in str_num2:
        num2_freq[digit] = num2_freq.get(digit, 0) + 1

    # Check if the frequencies of digits are equal
    return num1_freq == num2_freq
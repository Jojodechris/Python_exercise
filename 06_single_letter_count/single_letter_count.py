def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    count = 0
    letter_case= letter.lower()
    for char in word :
                if char.lower() == letter_case:
            count += 1
    return char_word.count(letter_case)
    

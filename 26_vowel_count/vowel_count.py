def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    # Create a dictionary to store the count for each letter in phrase:
    # freq = {}
    # count = 0
    # vowel= ["a","i","o","u","e"]
    # # Loop through all letters and update their counts if they are vowels (case insensitive)
    # for char in phrase.lower():
    #     if char in vowel:
    #         count += 1
    #         freq[char] = count
    #         result = freq[char]
    # return freq.append(result)

        freq = {}
    vowels = "aeiou"  # Create a string of vowels
    for char in phrase.lower():
        if char in vowels:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq

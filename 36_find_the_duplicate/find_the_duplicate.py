def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
# initializing dict to store frequency of each element
elements_count = {}
# iterating over the elements for frequency
for element in num:
   # checking whether it is in the dict or not
   if element in elements_count:
      # incerementing the count by 1
        return element
   else:
return None

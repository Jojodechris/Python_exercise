def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    diagonal_sum = 0
    size = len(matrix)

    for i in range(size):
        diagonal_sum += matrix[i][i]  # Add elements from top-left to bottom-right diagonal

    for i in range(size):
        diagonal_sum += matrix[i][size - i - 1]  # Add elements from bottom-left to top-right diagonal

    return diagonal_sum
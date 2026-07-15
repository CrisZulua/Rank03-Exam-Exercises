# Assignment
# ----------
# Write a function that returns a new matrix where each row is reversed.
#
# Example:
#   Input:  [[1, 2], [3, 4], [5, 6]]
#   Output: [[6, 5], [4, 3], [2, 1]]


def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix: list[list[int]] = []
    for row in matrix:
        new_matrix.append(row[::-1])
    return new_matrix


if __name__ == "__main__":
    print(mirror_matrix([[1, 2], [3, 4], [5, 6]]))

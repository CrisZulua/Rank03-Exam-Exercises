# Given a 2D matrix (list of lists), return a new matrix where each row
# is reversed.

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix: list[list[int]] = []
    for row in matrix:
        new_matrix.append(row[::-1])
    return new_matrix


if __name__ == "__main__":
    print(mirror_matrix([[1,2],[3,4],[5,6]]))

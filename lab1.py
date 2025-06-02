def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        size = list(map(int, lines[0].split()))
        coords = list(map(int, lines[1].split()))
        return size, coords

def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def fill_rectangle_with_ones(matrix, coords):
    r1, c1, r2, c2 = coords
    top = min(r1, r2) - 1
    bottom = max(r1, r2) - 1
    left = min(c1, c2) - 1
    right = max(c1, c2) - 1

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
                matrix[i][j] = 1

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def count_zeros(matrix):
    return sum(cell == 0 for row in matrix for cell in row)

def main():
    filename = 'test1.txt'
    size, coords = read_input_file(filename)
    rows, cols = size
    matrix = create_matrix(rows, cols)
    fill_rectangle_with_ones(matrix, coords)
    print_matrix(matrix)

    zero_count = count_zeros(matrix)
    print(f"\nNumber of zero cells: {zero_count}")

if __name__ == "__main__":
    main()



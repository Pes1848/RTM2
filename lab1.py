def fill_matrix_from_file(filename):
    with open(filename, 'r') as f:
        rows, cols = map(int, f.readline().split())

        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        coords = list(map(int, f.readline().split()))
        if len(coords) != 4:
            raise ValueError("Error")

        x1, y1, x2, y2 = coords
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        top = min(x1, x2)
        bottom = max(x1, x2)
        left = min(y1, y2)
        right = max(y1, y2)

        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                matrix[i][j] = 1

        return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    filename = 'test1.txt'
    matrix = fill_matrix_from_file(filename)
    print("Result:")
    print_matrix(matrix)

if __name__ == '__main__':
    main()


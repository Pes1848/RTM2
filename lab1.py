def read_input_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def parse_dimensions(line):
    rows, cols = map(int, line.strip().split())
    return rows, cols

def create_zero_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def parse_rectangle_coordinates(line):
    x1, y1, x2, y2 = map(int, line.strip().split())
    return x1 - 1, y1 - 1, x2 - 1, y2 - 1  # в индексы Python

def fill_rectangle(matrix, r1, c1, r2, c2):
    row_start, row_end = min(r1, r2), max(r1, r2)
    col_start, col_end = min(c1, c2), max(c1, c2)
    for r in range(row_start, row_end + 1):
        for c in range(col_start, col_end + 1):
            matrix[r][c] = 1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    lines = read_input_file('test1.txt')
    rows, cols = parse_dimensions(lines[0])
    matrix = create_zero_matrix(rows, cols)
    r1, c1, r2, c2 = parse_rectangle_coordinates(lines[1])
    matrix = fill_rectangle(matrix, r1, c1, r2, c2)
    print_matrix(matrix)

if __name__ == "__main__":
    main()


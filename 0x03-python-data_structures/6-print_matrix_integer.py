#!/usr/bin/python3
if __name__ == "__main__":
    def print_matrix_integer(matrix=[[]]):
        row_str = ["{} {} {}".format(row[0], row[1], row[2] for row in matrix]
        result = "\n".join(row_str)
        print(result)


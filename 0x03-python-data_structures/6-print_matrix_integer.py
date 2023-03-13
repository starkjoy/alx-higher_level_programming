#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_str = ["{} {} {}".format(row[0], row[1], row[2] for irow in matrix]
            result = "\n".join(row_str)
            print(result)


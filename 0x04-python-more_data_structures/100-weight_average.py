#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = sum([x[0]*x[1] for x in my_list])
    denominator = sum([x[1] for x in my_list])
    return numerator / denominator

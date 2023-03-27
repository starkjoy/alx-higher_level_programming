#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            x = my_list_1[i]
            y = my_list_2[i]
            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("wrong type")
            if y == 0:
                raise ZeroDivisionError("division by 0")
            result = x / y
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            result_list.append(result)
    return (result_list)

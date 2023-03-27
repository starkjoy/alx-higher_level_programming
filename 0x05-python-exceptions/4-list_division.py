#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            x = my_list_1[i]
            y = my_list_2[i]
            if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
                raise TypeError("wrong type")
            if y == 0:
                raise ZeroDivisionError("division by 0")
            result.append(x / y)
        except TypeError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("division by 0")
            result.append(0)
        finally:
            pass
    return (result)

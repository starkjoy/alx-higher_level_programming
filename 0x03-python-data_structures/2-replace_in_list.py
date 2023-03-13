#!/usr/bin/python3
if __name__ == "__main__":
    def replace_in_list(my_list, idx, element):
        if idx < 0:
            return (my_list)
        elif idx > len(my_list) - 1:
            return (my_list)
        else:
            return (my_list[idx]=element)


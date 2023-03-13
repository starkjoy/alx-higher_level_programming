#!/usr/bin/python3
if __name__ == "__main__":
    def no_c(my_string):
        new_string = ""
        for i in my_string:
            if i != 'c' or i != 'C':
                new_string = new_string + i
        return (new_string)

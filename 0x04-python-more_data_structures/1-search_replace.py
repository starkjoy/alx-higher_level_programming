#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result_iterator = map(lambda x: replace if my_list[x] == search else my_list[x], range(len(my_list)))
    my_list = list(result_iterator)
    print(my_list)


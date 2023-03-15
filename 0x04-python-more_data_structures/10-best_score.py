#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = max(a_dictionary.values())
    for key, value a_dictionary.items():
        if not value:
            return None
        elif value == max_value:
            return key

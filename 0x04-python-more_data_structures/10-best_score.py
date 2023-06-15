#!/usr/bin/pyhthon3
def best_score(a_dictionary):
    if a_dictionary:
        max_int = max(a_dictionary.values())
        for s, score in a_dictionary.items():
            if score == max_int:
                return s
    else:
        return None

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = tuple_a[:2] + (0, 0)
    tuple_b = tuple_b[:2] + (0, 0)

    sum_tuple_a = tuple_a[0] + tuple_b[0]
    sum_tuple_b = tuple_a[1] + tuple_b[1]

    result_turple = (sum_tuple_a, sum_tuple_b)

    return result_turple

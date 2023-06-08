#!/use/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    if b > 0:
        res = 1
        for _ in range(b):
            res *= a
    if b < 0:
        res = 1
        for _ in range(abs(b)):
            res /= a
    return res

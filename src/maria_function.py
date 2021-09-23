# returns log of y to the base x to the smallest integer
def log(x, y):
    if y/x == 0:
        return 0
    else:
        return 1 + log(x, y/x)
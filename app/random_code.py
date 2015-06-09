import random

def get_random(length):
    """
        will return a interger number with lengh
    """
    if length == 0:
        return 0
    right = 10 ** length  - 1
    return random.randint(0, right)

def get_random_str(length):
    i = get_random(length)
    s = "%0" + "%dd"  % length
    # s = "%0xd", x is length
    return s % i


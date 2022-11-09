import random 

def gen(n=100, high=100, low=-100):
    x = random.randint(low, high)
    y = random.randint(low, high)
    return [(random.randint(low, high), random.randint(low, high)) for _ in range(n) ]

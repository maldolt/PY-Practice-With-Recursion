# Write code for algorithm 4 below
def power(a, b):
    if b <= 1:
        return a
    return a * power(a, b-1)

print(power(2,3))
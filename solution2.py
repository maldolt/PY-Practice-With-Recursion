# Write code for algorithm 2 below
def natural_numbers(x, n):
    if x <= n:
        print(x)
        natural_numbers(x+1, n)
	#your code here
natural_numbers(3, 10)
#output: 1 2 3


def natural_numbers(lowerNum, higherNum):
    if lowerNum > higherNum:
        return
    else:
        print(lowerNum)
        natural_numbers(lowerNum + 1, higherNum)

n=10
natural_numbers(1,n)
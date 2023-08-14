# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max(a, b, c)

print(max_num(1, 2, 3))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(mult_list([1,2,3]))
# Write a Python function called rev_string() to reverse a string.

def rev_string(s):
    return s[::-1]

print(rev_string)
# Function to check whether a number falls in a given range
def num_within(number, start, end):
    return start <= number <= end

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x, a, b):
    return x in range (a,b+1)

print(num_within(1, 2, 3))

def pascal(n):
    def generate_next_row(row):
        next_row = [1]
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(1)
        return next_row
    
    triangle = []
    row = [1]
    for _ in range(n):
        triangle.append(row)
        row = generate_next_row(row)
    
    for row in triangle:
        print(' '.join(map(str, row)).center(n * 3))

# Test the functions
print("max_num:", max_num(5, 8, 3))
print("mult_list:", mult_list([2, 3, 4]))
print("rev_string:", rev_string("hello"))
print("num_within:", num_within(3, 2, 4))
print("num_within:", num_within(3, 1, 3))
print("num_within:", num_within(10, 2, 5))
print("pascal:")
pascal(5)

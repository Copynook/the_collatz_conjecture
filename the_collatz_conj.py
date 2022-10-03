def steps(number):
    if int(number) < 1:
        raise ValueError("Only positive integers are allowed")
        
    if int(number) == 1:
        return 0
        
    return 1 + (steps(int(number) / 2) if int(number) % 2 == 0 else steps(3 * int(number) + 1))

collatz_steps = steps(input())
print(collatz_steps)

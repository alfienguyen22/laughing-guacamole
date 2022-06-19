n = int(input())


for i in range(0,n):
    a = int(input())
    fact = 1

    for j in range(1, a + 1):
        fact = fact * j

    # Get the string representation
    num_str = repr(fact)

    # Access the last string of the digit string:
    last_digit_str = num_str[-1]

    # Convert the last digit string to an integer:
    last_digit = int(last_digit_str)

    print(last_digit)
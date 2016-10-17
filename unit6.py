# Prime numbers.py
# Ryan Ge
# October 14, 2016

def find_prime(number):

    # Define the list
    prime = []

    # When the number pool is not empty
    while len(number) != 0:

        # Tell the first prime number and add it to the prime list
        prime.append(number[0])

        # Search the rest of the number pool and remove multiples of the prime
        for i in number[1:]:
            if i % number [0] == 0:
                number.remove(i)

        # Remove the prime
        number.remove(number[0])

    # Return with the list of prime numbers
    return prime

# Get input from the user
n = int(input('Please input the maximum limit for the prime number:'))

# Define the list
number_pool = []

# Fill the list with integers from 2 to n
for i in range(2, n+1):
    number_pool.append(i)

# Print result
print('The prime numbers are:', find_prime(number_pool))
"""
Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and Eric Tan (CM 2991).  March 2013.
"""  

def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2()
    
def is_prime(n):
    """
    Returns True if the given integer is prime, else returns False.
    
    Note: The algorithm used here is simple and clear but slow.
    
    Precondition:  The given argument is an integer that is at least 2.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False
        
    return True

def sum_of_digits(number):
    """
    Returns the sum of the digits in the given integer.
    For example, if the number is 83135, this function returns 20.
    
    Precondition: the given argument is an integer.
    """
   
    if number < 0:
        number = -number
        
    digit_sum = 0
    while True:
        if number == 0:
            break
        digit = number % 10  # Get the digit
        digit_sum = digit_sum + digit  # Accumulate it into the sum
        number = number // 10  # Get ready for the next digit
        
    return digit_sum

def test_problem2():
    """ Tests the   problem2   function. """
    print('Testing problem2. The next line should be 18, 23536, 61, 5')
    print(problem2(4, 2), end=', ')
    print(problem2(105, 2), end=', ')
    print(problem2(2, 5), end=', ')
    print(problem2(2, 2))

def problem2(m, p):
    """
    Returns the sum of the digits of the prime numbers from m
    to (m to the pth power), where m and p are the given arguments.
    Do NOT include (m to the pth power) as one of the integers
    that you check, as it is definitely NOT a prime number.
    
    For example, if m is 4 and p is 2, this function examines
    the primes numbers from 4 to 15.  Those prime numbers are:
       5   7   11   13
    The sum of the digits of all those prime numbers is
       5 + 7 + (1 + 1) + (1 + 3), which is 18,
    so that is what this function returns in this case.
    
    Other tests you can use:
      -- When m is 105 and p is 2, this function should return 23536.
      -- When m is 2 and p is 5, this function should return 61.
      
    Preconditions: m and p are integers and each is at least 2.
    """
    total = 0
    for k in range(m, m ** p):
        if is_prime(k):
            total = total + sum_of_digits(k)
    return total
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()

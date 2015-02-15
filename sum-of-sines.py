"""
Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and Eric Tan (CM 2991).  March 2013.
"""  
import math
def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2a()
    test_problem2b()
    
def test_problem2a():
    """ Tests the   problem2a   function. """
    print('Testing problem2a. Next line should be -1.601, 1.135, -1.9498 ')
    print(problem2a(3, 5), end=',')
    print(problem2a(1, -2), end=',')
    print(problem2a(2, 5))
    
def problem2a(m, n):
    """
    Returns the sum of the sines of the integers from m squared
    to n squared, inclusive, where m and n are the given arguments.
    
    For example, if m is 3 and n is 5, this function returns:
       sine(9) + sine(10) + sine(11) + sine(12) + ... + sine(24) + sine(25)
    
    Preconditions: m and n are integers and the absolute value of m
                   is less than the absolute value of n.
    
    Examples that you can (AND SHOULD) use for testing include:
      When m is 3 and n is 5, the correct answer is about -1.601.
      When m is 1 and n is -2, the correct answer is about 1.135.
    """
    total = 0
    for k in range(m ** 2, (n ** 2) + 1):     
        total = total + math.sin(k)
    
    return total
    
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
    
def test_problem2b():
    """ Tests the   problem2b   function. """
    print('Testing problem2b. Next line should be 5, 1, 44 ')
    print(problem2b(3, 5), end=', ')
    print(problem2b(2, 1), end=', ')
    print(problem2b(5, 40))
    
def problem2b(m, f):
    """
    Returns the number of integers from m to f*m, inclusive,
    that are prime.
    
    For example, if m is 3 and f is 5, this function returns 5,
       since 3, 5, 7, 11, and 13 are the integers between 3 and 15,
       inclusive, that are prime.
    
    Preconditions: m and f are positive integers and m is at least 2.
    
    Examples that you can (AND SHOULD) use for testing include:
      When m is 3 and f is 5, the correct answer is 5.
      When m is 2 and f is 1, the correct answer is 1
        (since 2 is the only prime between 2 and 2, inclusive).
      When m is 5 and f is 40, the correct answer is 44.
    """
    total = 0
    for k in range(m, (f * m) + 1):
        if is_prime(k):
            total = total + 1
    return total
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()

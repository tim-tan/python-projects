"""
Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and Eric Tan (CM 2991).  March 2013.
"""  
import math
def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1()
    
def test_problem1():
    """ Tests the   problem1   function. """
    problem1()
    
def problem1():
    """
    Prompts the user for and inputs:
      -- A positive floating point number
      -- A positive integer
      -- A string
    in that order (via three separate inputs).
    Then prints, in this order, all on separate lines:
      -- The square root of the floating point number,
         repeated the input integer number of times
      -- The string, repeated the input integer number of times.
    No input validation is required.  Nothing else should be printed.
    
    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a positive floating point number: 1.44
         Enter a positive integer: 4
         Enter a string: Peace & Love.
         1.2
         1.2
         1.2
         1.2
         Peace & Love.
         Peace & Love.
         Peace & Love.
         Peace & Love.
    """
    input1 = input('Name a positive number.')
    input2 = input('Name an integer.')
    input3 = input('Say something.')
    
    n = int(input2)
    
    for k in range(n):
        print('The square root of your number is', math.sqrt(float(input1)))
        
    for k in range(n):
        print(input3)
        
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()

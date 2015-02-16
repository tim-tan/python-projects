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
      -- A floating point number
      -- Another floating point number
      -- A positive integer
      -- A string
    in that order (via four separate inputs).
    Then prints, in this order, all on separate lines:
      -- The cosine of the first floating point number
      -- The sine of the second floating point number
      -- The string, repeated the input integer number of times
      -- The input integer, repeated the input integer number of times.
    No input validation is required.  Nothing else should be printed.
    
    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a positive floating point number: 2.5
         Enter a positive floating point number: 1.3
         Enter a positive integer: 3
         Enter a string: March Madness!
         -0.8011436155469337
         0.963558185417193
         March Madness!
         March Madness!
         March Madness!
         3
         3
         3
    """
    input1 = input('Provide a number.')
    input2 = input('Provide another number.')
    input3 = input('Provide a positive integer.')
    input4 = input('Say something witty.')
    print()
    print(math.cos(float(input1)))
    print(math.sin(float(input2)))
    for k in range(int(input3)):
        print(input4)
    for k in range(int(input3)):
        print(int(input3))
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()

"""
Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and Eric Tan (CM 2991).  March 2013.
"""

import zellegraphics as zg
import random
import time
import math

def main():
    """ Calls the various   TEST   functions in this module. """
    test_wait_for_sum_of_cubes()
    test_random_walk()
    test_wait_for_repetition()
    test_wait_for_sine_sum()
    
def test_wait_for_sum_of_cubes():
    """ Tests the   wait_for_sum_of_cubes    function. """
    wait_for_sum_of_cubes(1000)
    
def wait_for_sum_of_cubes(x):
    """
    Returns the smallest n such that the sum
      1 cubed  +  2 cubed  +  3 cubed  +  ...  + n cubed
    is greater than or equal to x.
    
    Some examples:
      -- if x is 1 or less, this function returns 1.
      -- if x is bigger than 1 but less than or equal to 9,
            this function returns 2.
      -- if x is 12 (or any number in the range (9, 36]),
            this function returns 3.
      -- if x is 100, this function returns 4.
      -- if x is 1000, this function returns 8 because:
             1 + 8 + 27 + 64 + ... + (7**3) = 784
           but
             1 + 8 + 27 + 64 + ... + (8**3) = 1296
             
    Precondition: x is a number.
    """
    total = 0
    n = 0
    while True:
        n = n + 1
        total = total + (n) ** 3
        if total > x:
            break
        
    print(n)
    print() 
    
def close_window(window):
    """
    Displays a message at the bottom of the given window telling the user
    to click the mouse when done, waits for a mouse click, and then
    closes the window when the user clicks the mouse.
    Precondition: the argument is a zg.GraphWin.
    """
    width = window.getWidth()
    height = window.getHeight()
    bottom = zg.Point(width / 2, height - 20)
    text = zg.Text(bottom, 'Click anywhere in here to exit.')
    text.draw(window)
    
    window.getMouse()  # Wait for the user to click,
    window.close()  # then close the window.
    
def test_random_walk():
    """ Tests the   random_walk    function. """
    window = zg.GraphWin('Walk on!', 500, 500)
    circle = zg.Circle(zg.Point(250, 250), 30)
    random_walk(window, circle, 0.5, 50)
    close_window(window)
    
def random_walk(window, circle, probability_up, pixels_to_move):
    """
    Draws the given zg.Circle on the given zg.GraphWin.
    Then repeatedly:
      -- Flips a coin
           -- using random.randrange(100)
           -- HEADS are numbers less than 50
           -- TAILS otherwise
      -- If the coin is HEADS, moves the circle UP the given number of
           pixels, else moves the circle DOWN the given number of pixels.
           
    Stops when the circle's center is no longer in the given zg.GraphWin.
    
    RETURNs the number of movements.
    
    Preconditions: the first argument is a zg.GraphWin,
      the second argument is a zg.Circle,
      and the third argument is a number between 0 and 1.
    """
    circle.draw(window)
    count = 0
   
    while True:
        count = count + 1
        number = random.randrange(100)
        if number < 50:
            circle.move(0, pixels_to_move)
            time.sleep(0.1)
        if number >= 50:
            circle.move(0, -(pixels_to_move))
            time.sleep(0.1)
    
        if circle.getCenter().y > window.height:
            break
        if circle.getCenter().y < 0:
            break
        time.sleep(0.05)
    print(count)
    print()
    
def test_wait_for_repetition():
    """ Tests the   wait_for_repetition    function. """
    print ('Number returned:', wait_for_repetition(20))
  
def wait_for_repetition(m):
    """
    Repeatedly generates random integers in the range [0, m).
    Stops generating random integers when one is generated that is the
    same as the previous one.  Returns that last generated integer.
    
    For example, if the random integers generated are (in order):
      37  23  13  50  32  32
    then 32 is returned.
    
    Precondition: m is a positive integer.
    """
    prevnumber = m + 1
    while True:
        number = random.randrange(m)
        print(number, end=' ')
        if number == prevnumber:
            break
        prevnumber = number
    print()
    return number
     
    
def test_wait_for_sine_sum():
    """ Tests the   wait_for_sine_sum    function. """
    print('Expected: 9. Actual:', wait_for_sine_sum(1.9))
    # TODO: 5a. Implement this function, using it to test the NEXT
    #    function. Write the two functions in whichever order you prefer.
    
def wait_for_sine_sum(x):
    """
    Returns the smallest n such that the sum of the sines
    of the integers 0, 1, 2, ... n, is greater than the given x.
    
    For example, first note that the following chart gives the
    sines of the first few non-negative integers:
       k     sin(k)    total of sines so far
       0      0.0        0.0
       1      0.84       0.84
       2      0.91       1.75
       3      0.14       1.89
       4     -0.76       1.14
       5     -0.96       0.18
       6     -0.28      -0.10
       7      0.66       0.55
       8      0.99       1.54
       9      0.41       1.96
    From the above chart we see that:
      -- if x is negative, this function returns 0.
      -- if x is 0.6, this function returns 1.
      -- if x is 1.8, this function returns 3.
      -- if x is 1.9, this function returns 9.
      
    Another example: if x is 1.958, the answer is 166.
    
    Precondition: x is a number. (If x is too big,
                  this function runs forever -- that's OK.)
    """
    sumofsines = 0
    n = 0
    while True:
        sumofsines = math.sin(n) + sumofsines
        if sumofsines > x:
            break
        n = n + 1
    
    return(n)

#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()
    

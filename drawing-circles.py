"""

Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and Eric Tan (CM 2991).  March 2013.
"""  

import zellegraphics as zg

def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3()
    
def close_window(window):
    """
    Displays a message at the bottom of the given window telling the user
    to click the mouse when done, waits for a mouse click, and then
    closes the window when the user clicks the mouse.
    Precondition: the argument is a zg.GraphWin.
    """
    width = window.getWidth()
    height = window.getHeight()
    bottom = zg.Point(width / 2, height - 15)
    text = zg.Text(bottom, 'Click anywhere in here to exit.')
    text.draw(window)
    
    window.getMouse()  # Wait for the user to click,
    window.close()  # then close the window.
    
def test_problem3():
    """ Tests the   problem3   function. """
    window1 = zg.GraphWin('Testing Circles!', 750, 750)
    circle1 = zg.Circle(zg.Point(300, 300), 200)
    circle2 = zg.Circle(zg.Point(500, 300), 100)
    circle3 = zg.Circle(zg.Point(300, 200), 20)
    problem3(window1, circle1)
    problem3(window1, circle2)
    close_window(window1)
    window2 = zg.GraphWin('Testing Circles!', 770, 770)
    problem3(window2, circle3)
    close_window(window2)
    
    
def problem3(window, circle):
    """
    1. Draws two zg.Circle's on the given zg.GraphWin, as follows:
    
      -- The first zg.Circle is the given zg.Circle.
      
      -- The second zg.Circle is a new zg.Circle whose center is the
         same as the center of the given zg.Circle but whose radius
         is HALF the radius of the given zg.Circle.
         Also, this second zg.Circle has 'blue' as its fill color.
         
    2. Waits for a mouse-click.
    
    3. UN-draws both of the zg.Circle's just drawn.
    
    Drawing the circles in the order listed ensures that the
    second one drawn is visible on top of the (larger) first one drawn.
    
    Preconditions: The first argument is a zg.GraphWin, and the second
         argument is a zg.Circle that fits inside the zg.GraphWin.
    
    """
    
    circle.draw(window)
    newcircle = zg.Circle((circle.getCenter()), (circle.getRadius()) / 2)
    newcircle.setFill('blue')
    newcircle.draw(window)
    window.getMouse()
    circle.undraw()
    newcircle.undraw()
    
    
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()

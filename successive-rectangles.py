"""
Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and Eric Tan (CM 2991).  March 2013.
"""  

import zellegraphics as zg

def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3a()
    test_problem3b()
    
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
    
def test_problem3a():
    """ Tests the   problem3a   function. """
    window1 = zg.GraphWin('My first window!', 300, 500)
    x = 50
    y = 50
    rect1 = zg.Rectangle(zg.Point(x, y), zg.Point(x + 80, y + 100))
    rect2 = zg.Rectangle(zg.Point(x + 120, y + 200), zg.Point(x + 180, y + 280))
    rect3 = zg.Rectangle(zg.Point(x, y), zg.Point(x + 150, y + 150))
    problem3a(window1, rect1)
    problem3a(window1, rect2)
    close_window(window1)
    
    window2 = zg.GraphWin('My second window!', 600, 700)
    problem3a(window2, rect3)
    close_window(window2)
 
def problem3a(window, rectangle):
    """
    Draws the given zg.Rectangle with two lines forming an X inside it,
    and with the lines each having arrow-heads on them.
    
    Preconditions: The first argument is a zg.GraphWin, and
                   the second argument is a zg.Rectangle.
    """
    linea = zg.Line(rectangle.p1, rectangle.p2)
    lineb = zg.Line(zg.Point(rectangle.p2.x, rectangle.p1.y), zg.Point(rectangle.p1.x, rectangle.p2.y))
    rectangle.draw(window)
    linea.setArrow('both')
    linea.draw(window)
    lineb.setArrow('both')
    lineb.draw(window)
    
 
def test_problem3b():
    window = zg.GraphWin('The big finish!', 890, 890)
    problem3b(window, 5, zg.Point(30, 30), zg.Point(100, 120))
    problem3b(window, 3, zg.Point(500, 500), zg.Point(555, 655))
    close_window(window)

def problem3b(window, n, point1, point2):
    """
    Draws n rectangles as follows:
      -- Each rectangle has two lines inside it that form an X.
      -- The upper-left rectangle is has the two given points
           as opposite corners, where point1 is above and to the left
           of point2.
      -- The upper-left corner of each successive rectangle
           is at the lower-right corner of the preceding rectangle.
      -- The width and height of each successive rectangle is 75%
           of the width/height of the preceding rectangle.
    
    Preconditions: The first argument is a zg.GraphWin, the second
                   argument is a non-negative number, and
                   the third and fourth arguments are zg.Points
                   with point1 being above and to the left of point2.
    """
    a = point1.x
    b = point1.y
    c = point2.x
    d = point2.y
    for k in range(n):
        rectangle = zg.Rectangle(zg.Point(a, b), zg.Point(c, d))
        problem3a(window, rectangle)
        a = rectangle.p2.x
        b = rectangle.p2.y
        c = c + (0.75 * (rectangle.p2.x - rectangle.p1.x))
        d = d + (0.75 * (rectangle.p2.y - rectangle.p1.y))
    
 
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()

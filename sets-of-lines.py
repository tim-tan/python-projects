"""
Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and Eric Tan (CM 2991).  December 2012.
"""  

import zellegraphics as zg

def main():
    """ Calls the   TEST   functions in this module. """
    test_problem4a()
    test_problem4b()
    
def close_window(window):
    """
    Displays a message at the bottom of the given window telling the user
    to click the mouse when done, waits for a mouse click, and then
    closes the window when the user clicks the mouse.
    Precondition: the parameter is a zg.GraphWin.
    """
    width = window.getWidth()
    height = window.getHeight()
    bottom = zg.Point(width / 2, height - 15)
    text = zg.Text(bottom, 'Click anywhere in here to exit.')
    text.draw(window)
    
    window.getMouse()  # Wait for the user to click,
    window.close()  # then close the window.
    
def test_problem4a():
    """ Tests the   problem4a   function. """
    window1 = zg.GraphWin('Lines, Lines, Lines!', 500, 500)
    print('Testing problem4a. Next line should be 174. Line after that should be 6.')
    problem4a(window1, zg.Point(10, 10), 20)
    print(problem4a(window1, zg.Point(10, 10), 20))
    close_window(window1)
    window2 = zg.GraphWin('Lines, Lines, Lines!', 500, 500)
    problem4a(window2, zg.Point(100, 250), 3)
    print(problem4a(window2, zg.Point(100, 250), 3))
    close_window(window2)
    
def problem4a(window, point, n):
    """
    Draws a sequence of n zg.Lines's on the given zg.GraphWin,
    as follows:
      -- There are the given number (n) of zg.Lines's.
      -- Each zg.Line is vertical and has length 50.
            (All units are pixels.)
      -- The top of the first (leftmost) zg.Line
            is at the given zg.Point.
      -- Each successive zg.Line is 20 pixels to the right
            and 10 pixels down from the previous zg.Line.
      -- The first zg.Line has width (i.e., thickness) 1.
      -- Each successive zg.Line has width (thickness) 1 greater than
         the zg.Line to its left, but no greater than 12.
         (So once a zg.Line has width 12, it and all the zg.Lines
         to its right have width 12.)

    Returns the sum of the widths (thicknesses) of the zg.Line's.
    
    Preconditions: The first argument is a zg.GraphWin, the second
         argument is a zg.Point that is inside the zg.GraphWin, and
         the third argument is a positive integer.
    """
    x = point.x
    y = point.y
    a = point.x
    b = point.y + 50
    w = 0
    total = 0
    
    for k in range(n):
        line = zg.Line(zg.Point(x, y), zg.Point(a, b))
        if w < 12:
            w = w + 1
        total = total + w
        line.setWidth(w)
        line.draw(window)
        x = x + 20
        y = y + 10
        a = a + 20
        b = b + 10

    return total
        
def test_problem4b():
    """ Tests the   problem4b   function. """
    
    result = problem4b(4, zg.Point(100, 50))
    print('The value returned should be: 94')
    print('The value returned is in fact:', result)
    
    
    result = problem4b(7, zg.Point(30, 30))
    print('The value returned should be: 364')
    print('The value returned is in fact:', result)
        
def problem4b(m, p):
    """
    Constructs and displays a zg.GraphWin that is 400 wide by 600 tall.
    Draws, on the zg.GraphWin, m SETS of lines, where:
      -- Each SET of lines is drawn by a call to problem4a.
      -- The first set has 3 lines that start at point p (the given point).
      -- The second set has 5 lines that start 60 pixels directly below p.
      -- The third set has 7 lines that start 120 pixels directly below p.
      -- The fourth set has 9 lines that start 180 pixels directly below p.
      -- etc until m SETS of lines are drawn (where m is given)
    Each set of lines should have widths (thicknesses) per problem4a.
    
    Waits for the user to click the mouse
    (displaying a message if you wish), then closes the window.
    
    Returns the sum of the widths (i.e., thicknesses)
    of ALL of the lines drawn (over all m sets of lines).
    
    Preconditions: The first argument is a positive integer
                   and the second argument is a zg.Point.
                   
    """
    window1 = zg.GraphWin('Still more lines!', 400, 600)
    lines = 3
    r = p.x
    s = p.y
    total = 0
    for k in range(m):
        startingpoint = zg.Point(r, s)
        problem4a(window1, startingpoint, lines)
        total = total + problem4a(window1, startingpoint, lines)
        lines = lines + 2
        s = s + 60
    
    close_window(window1)
    return total
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()

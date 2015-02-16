"""
This module lets you integrate ROBOTS and ZELLEGRAPHICS.

Authors: David Mutchler, Dave Fisher, Chandan Rupakheti, Matt Boutell
         and their colleagues, and Eric Tan (CM 2991).  March 2013.
"""  

import new_create
import zellegraphics as zg
import time

def main():
    """ Calls the   TEST   functions in this module. """
    test_go_and_show()
    
#------------------------------------------------------------------------
# Students: Use this handy   close_window   function if you wish.
#           It is ALREADY DONE - no need to modify or add to it.
#------------------------------------------------------------------------
def close_window(window):
    """
    Displays a message at the bottom of the given window telling the user
    to click the mouse when done, waits for a mouse click, and then
    closes the window when the user clicks the mouse.
    
    Precondition: the given argument is a zg.GraphWin.
    """
    width = window.getWidth()
    height = window.getHeight()
    bottom = zg.Point(width / 2, height - 20)
    text = zg.Text(bottom, 'Click anywhere in here to exit.')
    text.draw(window)
    
    window.getMouse()  # Wait for the user to click,
    window.close()  # then close the window.
    
def test_go_and_show():
    """ Tests the   go_and_show   function. """
    go_and_show(72, 12)
    go_and_show(-72, 6)
    # TODO: 2a. Implement this function, using it to test the NEXT
    #    function. Write the two functions in whichever order you prefer.
    #    Include tests for BOTH directions,
    #    with at least two distances and two speeds.
    
def go_and_show(centimeters, centimeters_per_second):
    """
    1. Constructs a robot, zg.GraphWin (window), and
         -- zg.Image for the robot picture (use ANY of the ones attached)
         -- zg.Text to display the CUMULATIVE distance the robot travels.
         
    2a. Makes the given robot go straight the given number of centimeters
          at the given speed (in centimeters per second), then stop.
            -- Positive centimeters means go forward
            -- Negative centimeters means go backwards.
    2b. WHILE the robot is moving:
          -- Displays the image of the robot, moving horizontally
               across the window as the robot goes.
               The displayed motion is proportional to the actual distance
               traveled; you can use 1 pixel per millimeter if you wish,
               or you can use another reasonable scaling factor.
          -- Displays the CUMULATIVE distance that the robot has traveled
               in the zg.Text object.  The Text refreshes but does NOT move.
        Query the robot for its distance and redraw periodically;
        details are up to you.
        
    3. Shuts down the robot.
       Waits for the user to click in the window, then closes the window.
       
    See the attached   go_and_show.pdf   for samples of the imaging.
    
    Preconditions: The arguments are numbers,
                   with the 2nd number being positive.
    """
    
    window = zg.GraphWin('Robots are moving!', 700, 700)
    
    if centimeters > 0:
        timer = centimeters / centimeters_per_second
    else:
        timer = -centimeters / centimeters_per_second
    
    port = 5
    robot = new_create.Create(port)
    sensor = new_create.Sensors.distance
    robot.getSensor(sensor)
    
    text = zg.Text(zg.Point(250, 20), str(robot.getSensor(sensor)))
    text.draw(window)
    image = zg.Image(zg.Point(100, 300), 'robot5.gif')
    image.draw(window)
    
    robot.go(centimeters_per_second, 0)
    time.sleep(timer)
    d = 0
    for k in range(5):   
        text.undraw()
        image.undraw()
        d = d + robot.getSensor(sensor)
        text = zg.Text(zg.Point(250, 20), str(d))
        text.draw(window)
        image.move(5 * d, 0)
        time.sleep(timer / 5)
        
    robot.stop()
    
    robot.shutdown()
    close_window(window)
    # TODO: 2b. Implement and test this function.
    # HINT: You may need to "stringify" a number; use   str  for that.
    
#------------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#------------------------------------------------------------------------
if __name__ == '__main__':
    main()

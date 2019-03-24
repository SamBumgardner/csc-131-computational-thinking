# CSC 131 - Computational Thinking
## Lab 8

For this lab, you will develop a GUI application to animate a bouncing ball. 

#### Requirements:
 * The ball will start near the top left corner of an 800 by 400 canvas. 
 * The ball will move at a 45 degree angle, where it moves 2 pixels horizontally and 2 pixels vertically every 15 milliseconds.
 * When the ball hits any of of the four edges of the canvas, it will bounce in the opposite direction. 
     * The angle of reflection is always equal to the angle of incidence. So, if the ball is moving south-east and it hits, let us say, the bottom edge, it will bounce in the north-east direction. 
     * It will be easier to consider the east-west (ie., right-left) movement as independent from the north-south (i.e, up-down movement). 
     * Below, you are given code to deal with the east-west movement and need to add code to deal with the north-south movement.

To help you with this lab, write the code in the following stages and **always make sure your code is working before you move to the next stage**. You may also need to draw/write your ideas on a piece of paper to help you visualize things.  

 1. Create a GUI application with an 800 pixels by 400 pixels canvas
 2. Create a small ball starting near the top left corner of the canvas. You can either draw a small circle, say with diameter of 20 pixels, or use an image of a small ball. Identify the ball (i.e, give it a tags value) so that you can refer to it later
 3. Use two variables, say `left_x` and `top_y`, to track the ball's location. This is needed to figure out when the ball hits an edge and, therefore, should change direction
 4. Use two variables to track the ball's horizonal and vertical directions. Initially, the ball moves east-south. So in my code, I used horizontal_direction and vertical_direction and set them as follows:
    ```python
    horizontal_direction = "east"
    vertical_direction = "south"
    ```
 5. Insert code into the animation loop to move the ball 2 pixels down (i.e. south) and 2 pixels right (i.e., east) every 15 miliseconds. This code will be adjusted in steps 6 and 7. 
     * Hint: see how this was done in the [VerticalBouncingBall.py](../lecture_materials/graphical_user_interfaces/bouncing_ball_example/VerticalBouncingBall.py) example.
 6. Add code to the animation loop to check if the ball has collided with the left or right edge of the canvas. If it has, reverse the direction of its horizontal movement.
     * See the example code below for one method of doing this.
 7. Repeat step 6, but checking for collision with the top and bottom edge and reversing the ball's vertical movement.

```python
# horizontal movement
if horizontal_direction == "east":
    left_x += dx # dx should always be 2 because the ball moves 2 pixels horizontally every 15 milliseconds
    self.canvas.move("ball", dx, 0) # move ball horizontally dx pixels to the right/east
    
    if left_x + ball_diameter >= canvas_width: # ball has hit east wall
        horizontal_direction = "west" # change direction
        
else: # i.e., horizontal_direction is "west"
    left_x -= dx 
    self.canvas.move("ball", -dx, 0) # move ball horizontally dx pixels to the left/west
    
    if left_x <= 0: # ball has hit west wall
        horizontal_direction = "east" # change direction
```

Name your file `lab8.py`. Make sure to include your name and the name of your TRACE folder at the top of the file in a docstring. When you are done, demonstrate your code to the instructor. Make sure to upload an electronic copy of your solution in your CSC131 upload folder in a folder named `LABS\lab8`.

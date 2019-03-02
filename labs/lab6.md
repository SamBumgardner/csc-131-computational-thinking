# CSC 131 - Computational Thinking
## Lab 6

Write a GUI-based program that allows the user to convert temperature values between degrees Fahrenheit and degrees Celsius. 

The interface should have labeled entry fields for these two values. These components should be arranged in a grid where the labels occupy the first row and the corresponding fields occupy the second row. At start-up, the Fahrenheit field should contain `32.0`, and the Celsius field should contain `0.0`. 

The third row in the window contains two command buttons, labeled `>>>>` and `<<<<`. When the user presses the first button, the program should use the data in the Fahrenheit field to compute the Celsius value, which should then be output to the Celsius field. The second button should perform the inverse function.

 The temperature conversion formulas are as follows:

Fahrenheit to Celsius:
```
celsius = (fahrenheit - 32) * 5/9
```

Celsius to Fahrenheit:
```
fahrenheit = celsius * 9/5 + 32
```

Name your file `lab6.py`. Make sure to include your name and the name of your TRACE folder at the top of the file in a docstring. When you are done, demonstrate your code to the instructor and upload your solution in your CSC131 upload folder in a folder called `LABS\lab6`.

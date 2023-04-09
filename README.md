# Calculator
---

I got a task from the  [CrossRoads Team](https://www.youtube.com/@BrototypeMalayalam "title text!") to build a calculator, while the Python Programming Challenge. From a programmer's mind, I accepted the challenge with hope, After start doing things gone worst but at last, I completed it.

Latest Update Feature:   In the old version, the User could not enter inputs using the keyboard. So I created a new function  [bind_key](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L188).
The bind_key() method is used to bind the keys of the keyboard to the buttons of the calculator. This allows the user to type on the keyboard and have the same input registered as if they had clicked the buttons.

This method is called in the [__init__()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L19) method of the Calculator class to ensure that the bindings are set up when the calculator object is created.

Special Thanks: [CrossRoads Team](https://www.youtube.com/@BrototypeMalayalam "title text!") 

Author: Sribin K

Mail: sribin85@gmail.com
___
<img width="180" alt="Screenshot 2023-04-08 031437" src="https://user-images.githubusercontent.com/103424492/230759031-3a7333a9-4044-4933-90bd-dc44bb09f438.png">""<img width="205" alt="Screenshot 2023-04-09 014619" src="https://user-images.githubusercontent.com/103424492/230760887-ac14c5fc-7dfc-4719-8c81-9ec557811144.png">




*This is an calculator fully coded by me with Python. Here I am using Tkinter GUI (Graphical User Interface)*

This is a calculator application written using the tkinter library in Python. The calculator has a GUI with a display frame and a button frame. The GUI has buttons for digits, operators, clear, delete, equal, square, and square root. The calculator can perform basic arithmetic operations such as addition, subtraction, multiplication, and division, and can also calculate the square and square root of numbers.

The calculator class has an init method that initializes various attributes such as the GUI window, the total and current expressions, and the various buttons. It also has methods for creating the display and button frames, creating the various buttons such as digit buttons, operator buttons, clear, delete, equal, square, and square root buttons, and binding the buttons to their respective commands.

The calculator also has various helper methods such as digit_button_click, operator_button_click, clear, delete, and evaluate, which perform the actual calculations based on the user input. The digit_button_click method updates the current expression with the clicked digit, while the operator_button_click method updates the current expression with the clicked operator. The clear method clears the current expression, while the delete method deletes the last character from the current expression. The evaluate method evaluates the current expression and updates the total expression and current expression accordingly.

## how does this calculator work?

The code i provided is a simple calculator application built using the tkinter module in Python. It provides a GUI interface for users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

Here is a brief summary of the main features of the code:

- The [Calculator](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L17) class is defined, which creates an instance of the calculator.

- The GUI window is created using the Tk class from the tkinter module.

- The calculator has a display area and a set of buttons for users to input values and perform operations.

- The [create_display_frame()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L62) method creates a frame for the display area.

- The [create_display_label()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L74) method creates two labels for the display area, one for the total expression and one for the current expression.

- The [create_button_frame()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L67) method creates a frame for the buttons.

- The [create_digit_button()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L85) method creates digit buttons and assigns each of them a command to update the current expression when clicked.

- The [create_operator_button()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L97) method creates operator buttons and assigns each of them a command to update the current expression when clicked.

- The [create_clear_button()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L106) method creates a "C" button to clear the current expression.

- The [create_delete_button()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L111) method creates a delete button to remove the last digit entered in the current expression.

- The [create_equal_button()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L116) method creates an equal button to evaluate the current expression and display the result.

- The [create_square_button()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L121) method creates a button to calculate the square of the current expression.

- The [create_sqrt_button()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L126) method creates a button to calculate the square root of the current expression.

- The [digit_button_click()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L133) method is called when a digit button is clicked and updates the current expression.

- The [operator_button_click()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L139) method is called when an operator button is clicked and updates the current expression.

- The [clear()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L156) method is called when the "C" button is clicked and clears the current expression.

- The [delete()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L163) method is called when the delete button is clicked and removes the last digit entered in the current expression.

- The [evaluate()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L202) method is called when the equal button is clicked and evaluates the current expression.

- The [bind_key()](https://github.com/iamsribin/Calculator/blob/62a834153b25668c1ce60cab3f024d00519a4a87/calculator.py#L188) method binds the number keys and arithmetic operator keys to the corresponding functions.


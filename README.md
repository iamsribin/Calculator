# Calculator
---
I got an task from the [CrossRoads Team](https://www.youtube.com/@BrototypeMalayalam "title text!") to build an calculator, while the python Programing Challenge.
From an Programmers mind I accepted the challenge with hope, After start doing things gone worst but at last I completed.

Latest Update Feature:  In the old version User could not enter inputs using keyboard.So I created a new function  [bind_key](https://github.com/iamsribin/Calculator/blob/5effd7da9eb130dc85266e708bbfe9c8d5e2964e/calculator.py#L161). 
This is a typing function. `self.window.bind("<Return>", lambda event: self.evaluate())`This line of code specifies that pressing the Enter key is equivalent to pressing the Equals button.
The two loops in this funtion display numbers when the numbers key pressed and oparetions when the oparation key is pressed.

Special Thanks: [CrossRoads Team](https://www.youtube.com/@BrototypeMalayalam "title text!") 

Author: Sribin K

Mail: sribin85@gmail.com
___

<img width="276" alt="model of the calculator" src="https://user-images.githubusercontent.com/103424492/205878975-2aa55f66-49c3-461c-8511-84612490254e.png"> "   " <img width="279" alt="calculator" src="https://user-images.githubusercontent.com/103424492/205879343-7aa1ba3a-3e11-42ed-bb86-ec5e5d4b72bc.png">

*This is an calculator fully coded by me with Python. Here I am using Tkinter GUI (Graphical User Interface)*

# Funtions
---

## Frame

- [**create_display_frame**](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L57)

     *this this funtion creates the frame for adding labels*
     
- [**create_button_frame**](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L62)

    *this funtion creates the frame for adding buttons *
    
## Labels

- [**create_display_label**](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L69)
    * **total_label**
     
        *This label is used to view the operations and numbers entered to perform the calculatoin. when the operation button or equal button is clicked,
         those thins will come to this label.The string in the [total_expression](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L26) variable is displayed here.
       
    * **label**
     
        *This label is used to view the currently entered numbers and show the results of the The string in the [current_expression](calculation.https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L27) variable is displayed here.*
 ## Button
 
 - [**create_digit_button**](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L80)
 
     *The digits assigned to the digit variable in the[__ init __ ](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L18) funtion are installed 
     into the [create_button_frame](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L69) using a loop Due to the operation of the loop in the[__ init __ ](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L18) funtion,the size of the created buttons increses  with the  size of the [create_button_frame](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L69).*
      
 - [**create_operator_button**](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L92)
       
      *The operation symbols assingned to the operator variable in the  [__ init __ ](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L18) funtion are installed into the [create_button_frame](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L62) using a loop.Due to the operation of the loop in the[__ init __ ](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L18) funtion,the size of the created buttons increses  with the 
      size of the [create_button_frame](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L69).*
      
 ## Special buttons 
 
These buttons are created and added to the [create_button_frame](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L69)
      
 - [**create_clear_button**](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L101)
 
 - [**create_delete_button**](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L106)
 
 - [**create_squre_button**](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L116)
 
 - [**create_sqrt_button**](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L121)
   
 - [**create_equal_button**](https://github.com/iamsribin/Calculator/blob/098b0245daa1c87c04c7d4992634b63cee0c7170/calculator.py#L111)

    

# How is it working ?
---
*note: There are many methods to do this work But here I am using my own logic and more ideas that I got from researches.*

*In the interface I created Buttons and Label (for display) for user to interact for the calculations. We pass argument to the btn_clicked function.*

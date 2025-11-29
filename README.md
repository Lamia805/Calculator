# Calculator
<br>
1. Create Arithmetic Functions

As the base of your calculator, write four separate Python functions:

 A function to add two numbers

 A function to subtract two numbers

 A function to multiply two numbers

 A function to divide two numbers (must handle division-by-zero safely)

These functions form the foundation for all later steps.

2. User Input & Displaying Results

Ask the user to enter two numbers.

Using the functions above, display:

 The addition result

 The subtraction result

 The multiplication result

 The division result (show appropriate message for division by zero)

3. Input Validation

Create a separate function that:

 Takes user input

 Uses try–except to check if the input is a valid number

 Repeats until the user enters a valid number

This ensures the calculator never crashes due to invalid inputs.

4. Menu-Based Calculator

Turn your calculator into a menu-driven program.

Show a list of options:

1. Add

2. Subtract

3. Multiply

4. Divide

5. Exit

Keep the calculator running inside a while loop so the user can perform unlimited

operations until they choose Exit.

Also print each result in a formatted way, such as:

5 + 3 = 8

5. Convert to Object-Oriented Calculator

Create a Calculator class that contains all the arithmetic methods:

 add()

 subtract()

 multiply()

 divide() (must return a custom message for division by zero)

Then:

A. Add a menu() method

Inside the class, create a method that prints all available options.

B. Add a run() method

This method will:

 Display the menu

 Take user input

 Ask for two numbers

 Perform the selected operation

 Keep looping until the user chooses Exit

This method acts as the “controller” for the whole calculator project.

C. Create a Calculator object

At the end of the program, create an instance of the Calculator class and call the

run() method so the entire calculator system starts automatically.

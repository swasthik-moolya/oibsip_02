# OIBSIP

<h2>BMI Calculator</h2>
<p>The code you provided defines a function called bmi_calculator that calculates and prints a person's Body Mass Index (BMI) along with their weight category based on the BMI value.</p>
<p>Explanation:
<br>
  
**1. Function Defination:** <br>
>This line defines a function named bmi_calculator. <br><br>

**2. User Input Validation with Weight:** <br>
>This block handles user input for weight: A while True loop ensures the loop continues until valid input is received.

>Inside the loop: A try-except block handles potential errors during input conversion. float(input(...)) tries to convert the user's input to a floating-point number (weight). The if statement checks if the weight is less than or equal to zero (negative or zero weight makes no sense for BMI). If the weight is invalid, a ValueError exception is raised with the message "Weight must be positive."

>The except ValueError as e: block catches the exception and prints the error message (e).
>The break statement exits the loop if a valid weight is entered.

<br>**3. User Input Validation with Height:**
>This block is similar to the weight validation but handles user input for height.
**4. BMI Calculation and Category:** <br>
bmi = weight / (height ** 2) calculates the BMI using the standard formula.
The calculated BMI is then printed with a label.
>An if-elif-else statement categorizes the BMI based on predefined ranges:
>>Underweight: BMI less than 18.5
>>Normal: BMI between 18.5 (inclusive) and 25 (exclusive)
>>Overweight: BMI between 25 (inclusive) and 30 (exclusive)
>>Obese: BMI 30 or above
The corresponding category is assigned to the category variable.

**5. Printing Category:**<br>
Finally, the category based on the BMI is printed.

**6. Main Execution Block:** <br>
- This block ensures the bmi_calculator function is only called when the script is run directly (not imported as a module).
- It calls the bmi_calculator function to initiate the BMI calculation and category display process.</p>

# OIBSIP

In this Python Programming internship I have been assigned several tasks to complete. 

#TASK LIST
<h2>BMI Calculator</h2>
<p>The code you provided defines a function called bmi_calculator that calculates and prints a person's Body Mass Index (BMI) along with their weight category based on the BMI value.</p>
<h3>Code breakdown</h3>
<p>1. Function Defination:
This line defines a function named bmi_calculator. 
2. User Input Validation with Weight:
>This block handles user input for weight: A while True loop ensures the loop continues until valid input is received.

>Inside the loop: A try-except block handles potential errors during input conversion. float(input(...)) tries to convert the user's input to a floating-point number (weight). The if statement checks if the weight is less than or equal to zero (negative or zero weight makes no sense for BMI). If the weight is invalid, a ValueError exception is raised with the message "Weight must be positive."

>The except ValueError as e: block catches the exception and prints the error message (e).
>The break statement exits the loop if a valid weight is entered.

3. User Input Validation with Height:
>This block is similar to the weight validation but handles user input for height.
4. BMI Calculation and Category:
bmi = weight / (height ** 2) calculates the BMI using the standard formula.
The calculated BMI is then printed with a label.
>An if-elif-else statement categorizes the BMI based on predefined ranges:
>>Underweight: BMI less than 18.5
>>Normal: BMI between 18.5 (inclusive) and 25 (exclusive)
>>Overweight: BMI between 25 (inclusive) and 30 (exclusive)
>>Obese: BMI 30 or above
The corresponding category is assigned to the category variable.

5. Printing Category:
Finally, the category based on the BMI is printed.

6. Main Execution Block:
- This block ensures the bmi_calculator function is only called when the script is run directly (not imported as a module).
- It calls the bmi_calculator function to initiate the BMI calculation and category display process.</p><br>
<br>
<h2> Simple Password Generator</h2>
<p>It is a basic command-line password generator that allows users to customize the generated password based on their preferences.</p>
<h3>Let me breakdown:

1] We will be importing necessary libraries like:
>>random: This library is used to generate random numbers and characters.
>>string: Provides constants representing the lowercase and uppercase alphabets, digits, and punctuation.

2] Define the "generate_password" Function:
>>This function creates a random password based on the provided parameters.

3]Function Logic

4]Define the "main" Function
>>This function handles user interaction and calls the generate_password function.

5]User Input and Validation

6]Generate and Print Password

7]Main Execution Block</h3><br>
<br>
<br>
<h3>CLI Weather App</h3>
<p>a CLI weather app in Python that fetches and displays current weather data for a user-specified location (e.g., Bengaluru, IN) using a weather API. Show basic information such as temperature, humidity, and weather conditions.</p><br>
<h4>Understanding the Requirements:</h4>
<h4>API Integration:</h4>
<p>We'll use OpenWeatherMap in this task. We'll need to sign up for an API key.
1. User Input: We'll prompt the user for a city name followed by comma and first two letter of the Country.
2. Data Fetching: We'll make an API request to fetch weather data.
3. Data Parsing: We'll extract relevant information from the JSON response.
4. Output Formatting: We'll display the weather information in a user-friendly format.</p>

<h4>Code Explanation:</h4>
<ol>
  <li>get_weather function:<br>
Takes a city name as input.<br>
Constructs the API URL using the city name and API key.</li>
 <li>Import necessary libraries: requests for making API requests and json for parsing JSON data.<br>Makes a GET request to the API.<br>
Parses the JSON response and returns the data.<br>
Includes error handling for potential exceptions.</li>
<li>display_weather function:<br>
Takes weather data as input.<br>
Extracts temperature, humidity, and weather description from the data.<br>
Prints the extracted information in a formatted way.</li>
<li>display_weather function:
Takes weather data as input.
Extracts temperature, humidity, and weather description from the data.
Prints the extracted information in a formatted way.</li>
<li>main function:
Prompts the user for a city name.
Calls get_weather to fetch data.
Calls display_weather to display the results.
</li>
</ol>




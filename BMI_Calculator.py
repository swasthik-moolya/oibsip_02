def bmi_calculator():

  while True:
    try:
      weight = float(input("Enter your weight in kilograms (positive value): "))
      if weight <= 0:
        raise ValueError("Weight must be positive.")
      break
    except ValueError as e:
      print(e)

  while True:
    try:
      height = float(input("Enter your height in meters (positive value): "))
      if height <= 0:
        raise ValueError("Height must be positive.")
      break
    except ValueError as e:
      print(e)

  bmi = weight / (height ** 2)

  print("Your BMI is:", bmi)

  if bmi < 18.5:
    category = "Underweight"
  elif 18.5 <= bmi < 25:
    category = "Normal"
  elif 25 <= bmi < 30:
    category = "Overweight"
  else:
    category = "Obese"

  print("You are classified as:", category)

if __name__ == "__main__":
  bmi_calculator()

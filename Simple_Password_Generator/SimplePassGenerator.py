import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_digits, include_special_chars):

  characters = ""
  if include_lowercase:
    characters += string.ascii_lowercase
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_digits:
    characters += string.digits
  if include_special_chars:
    characters += string.punctuation

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

def main():

  while True:
    try:
      length = int(input("Enter password length (minimum 8 characters): "))
      if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
      break
    except ValueError:
      print("Invalid input! Please enter a positive integer.")

  include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
  include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
  include_digits = input("Include numbers? (y/n): ").lower() == 'y'
  include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

  if not any([include_lowercase, include_uppercase, include_digits, include_special_chars]):
    print("You must select at least one character type.")
    return

  password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_special_chars)
  print("Generated password:", password)

if __name__ == "__main__":
  main()

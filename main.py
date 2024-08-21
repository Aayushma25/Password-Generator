import random
import string

def evaluate_password_strength(password):
    # Password strength criteria
    length_criteria = len(password) >= 10
    upper_criteria = any(char.isupper() for char in password)
    lower_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = any(char in string.punctuation for char in password)
    
    # Evaluate password strength
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    if criteria_met == 5:
        return "Very Strong"
    elif criteria_met == 4:
        return "Strong"
    elif criteria_met == 3:
        return "Medium"
    else:
        return "Weak"

def get_user_preferences():
    # Ask user for preferences
    length = int(input("How long should the password be? "))
    
    
    include_upper = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
   
    return length, include_upper, include_digits, include_special

def generate_password(length=10, min_upper=2, min_digits=2, min_special=2):
    length, include_upper, include_digits, include_special = get_user_preferences()

    if length < (min_upper + min_digits + min_special):
        raise ValueError("Password length is too short for the given constraints.")
    
    # Define character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase if include_upper else ''
    digits = string.digits if include_digits else ''
    special = string.punctuation if include_special else ''
    
    
    # Initialize password with required characters
    password = []
    
    # Add a minimum number of uppercase letters
    if include_upper:
        password.extend(random.choice(upper_case) for _ in range(min_upper))
    
    # Add a minimum number of digits
    if include_digits:
        password.extend(random.choice(digits) for _ in range(min_digits))
    
    # Add a minimum number of special characters
    if include_special:
        password.extend(random.choice(special) for _ in range(min_special))
    
    # Add remaining characters from all available character types
    remaining_length = length - len(password)
    all_characters = lower_case + upper_case + digits + special
    password.extend(random.choice(all_characters) for _ in range(remaining_length))
    
    # Shuffle to ensure the order is random
    random.shuffle(password)
    
    # Convert list to string
    password = ''.join(password)
    
    # Evaluate password strength
    strength = evaluate_password_strength(password)
    
    return password, strength

# Example usage
password, strength = generate_password(min_upper=3, min_digits=3, min_special=3)
print("Generated Password:", password)
print("Password Strength:", strength)



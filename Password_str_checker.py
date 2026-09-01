def check_password_strength(password):
    
    # Length Verification: < 8 chars = immediate fail
    if len(password) < 8:
        return "Weak (Immediate Fail: Must be at least 8 characters)"
        
    # Pattern Recognition using Pythonic short-circuit execution
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    # Checking for symbols (anything that is not a letter or a number)
    has_symbol = any(not char.isalnum() for char in password)
    
    # Calculate strength score based on mandatory criteria
    score = 0
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1
        
    # Risk Classification Output
    if score == 3:
        return "Strong"
    elif score == 2:
        return "Medium"
    else:
        return "Weak (Missing mandatory character types)"

# --- Interactive User Input ---
if __name__ == "__main__":
    print("--- DecodeLabs Password Strength Checker ---")
    print("Type 'quit' to exit.\n")

    while True:
        password = input("Enter a password to check: ")
        
        if password.lower() == "quit":
            print("Exiting. Goodbye!")
            break
        
        strength = check_password_strength(password)
        print(f"Strength: {strength}\n")
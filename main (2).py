import re

def assess_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Calculate strength score
    strength_score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_char_criteria
    ])
    
    # Provide feedback based on strength score
    if strength_score == 5:
        feedback = "Your password is very strong."
    elif strength_score == 4:
        feedback = "Your password is strong."
    elif strength_score == 3:
        feedback = "Your password is medium strength."
    elif strength_score == 2:
        feedback = "Your password is weak."
    else:
        feedback = "Your password is very weak."
    
    # Detailed feedback
    detailed_feedback = []
    if not length_criteria:
        detailed_feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        detailed_feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        detailed_feedback.append("Password should include at least one lowercase letter.")
    if not digit_criteria:
        detailed_feedback.append("Password should include at least one digit.")
    if not special_char_criteria:
        detailed_feedback.append("Password should include at least one special character.")
    
    return feedback, detailed_feedback

# Example usage
password = input("Enter a password to assess its strength: ")
feedback, detailed_feedback = assess_password_strength(password)

print(feedback)
for df in detailed_feedback:
    print(df)
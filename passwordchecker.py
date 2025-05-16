import re

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add digits.")

    if re.search(r"[!@#$%^&*()_+=\-]", password):
        score += 1
    else:
        suggestions.append("Add special characters (!@#$...)")

    if score == 5:
        print("✅ Strong Password!")
    elif 3 <= score < 5:
        print("⚠️ Moderate Password.")
    else:
        print("❌ Weak Password!")

    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print("- " + s)

# Input from user
user_pass = input("Enter your password: ")
check_password_strength(user_pass)

# 🔐 Password Strength Checker

This is a simple **Python project** that checks the **strength of a password** and provides suggestions to make it stronger. Perfect for beginners learning Python and cybersecurity basics.

## 🚀 Features

- Checks password length
- Validates use of:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters (`!@#$%^&*()_+=-`)
- Gives a score and prints:
  - ✅ Strong Password
  - ⚠️ Moderate Password
  - ❌ Weak Password
- Suggests improvements if needed (bonus point)

## 🧠 How It Works

The script evaluates your password using regular expressions and scores it out of 5 based on:

| Criteria               | Points |
|------------------------|--------|
| Length ≥ 8             | +1     |
| Contains lowercase     | +1     |
| Contains uppercase     | +1     |
| Contains digit         | +1     |
| Contains special char  | +1     |





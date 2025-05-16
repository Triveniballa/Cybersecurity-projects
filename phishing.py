def is_phishing_email(text):
    phishing_keywords = [
        "urgent", "click here", "verify your account", "password expired",
        "win", "limited time", "free", "update your info", "suspicious activity"
    ]

    found = []
    for word in phishing_keywords:
        if word in text.lower():
            found.append(word)

    if found:
        print("⚠️ Potential phishing email!")
        print("Suspicious phrases found:")
        for f in found:
            print("- " + f)
    else:
        print("✅ Email seems safe.")

# Input from user
email_text = input("Paste the email text here:\n")
is_phishing_email(email_text)

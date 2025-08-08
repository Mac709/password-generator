# 🔐 Password Generator (12-character secure password)

A simple Python script that generates secure 12-character passwords including:
- Uppercase letters
- Lowercase letters
- Digits
- Special symbols

Perfect for creating secure credentials for apps, databases, or personal accounts.

---

## 📦 Features

- Ensures at least one character from each category: upper, lower, digit, symbol
- Uses Python’s built-in `random` and `string` modules (no external dependencies)
- Easy to customize (password length, character sets)

---

## 🚀 How to Use

### 1. Clone or Download the Repository

```bash
git clone https://github.com/mac709/password-generator.git
cd password-generator
```

> Alternatively, just copy the script if you're using it in a standalone environment.

### 2. Run the Script

Make sure Python 3 is installed on your system.

```bash
python password_generator.py
```

You’ll see output like this:

```
Generated Password: fG8$Kp#v1T@x
```

---

## 🛠 Customize (Optional)

You can change the password length by modifying this line in the script:

```python
print(generate_password(length=16))
```

---

## 📄 Example Code

```python
import random
import string

def generate_password(length=12):
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = random.choices(all_chars, k=remaining_length)

    password_list = list(lowercase + uppercase + digit + symbol + ''.join(remaining_chars))
    random.shuffle(password_list)

    return ''.join(password_list)

if __name__ == '__main__':
    print("Generated Password:", generate_password())
```

---

## ✅ Requirements

- Python 3.x
- No additional libraries needed

---

## 🔒 License

MIT License

---

## 🙋‍♂️ Author

Mac709

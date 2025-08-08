import random
import string

def generate_password(length=12):
    # 各カテゴリから最低1文字ずつ確保
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    # 残りの文字をランダムに選択（合計が length になるように）
    remaining_length = length - 4
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = random.choices(all_chars, k=remaining_length)

    # すべての文字をシャッフル
    password_list = list(lowercase + uppercase + digit + symbol + ''.join(remaining_chars))
    random.shuffle(password_list)

    return ''.join(password_list)

# 使用例
print(generate_password())

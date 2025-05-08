import os

raw_text_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "raw_text.txt",
)


def encrypt_text(n, m):
    try:
        with open(
            raw_text_path,
            "r",
        ) as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: raw_text.txt not found.")
        return None

    encrypted = []
    for char in text:
        if char.islower():
            if char <= "m":
                # Shift forward by n*m
                shift = (n * m) % 26
                new_char = chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
            else:
                # Shift backward by n+m
                shift = (n + m) % 26
                new_char = chr(((ord(char) - ord("a") - shift) % 26) + ord("a"))
        elif char.isupper():
            if char <= "M":
                # Shift backward by n
                shift = n % 26
                new_char = chr(((ord(char) - ord("A") - shift) % 26) + ord("A"))
            else:
                # Shift forward by m^2
                shift = (m**2) % 26
                new_char = chr(((ord(char) - ord("A") + shift) % 26) + ord("A"))
        else:
            new_char = char
        encrypted.append(new_char)

    encrypted_text = "".join(encrypted)

    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    return encrypted_text


def decrypt_text(n, m, encrypted_text):
    decrypted = []
    for char in encrypted_text:
        if char.islower():
            if char <= "m":
                # Reverse shift forward by n*m (shift backward)
                shift = (n * m) % 26
                new_char = chr(((ord(char) - ord("a") - shift) % 26) + ord("a"))
            else:
                # Reverse shift backward by n+m (shift forward)
                shift = (n + m) % 26
                new_char = chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
        elif char.isupper():
            if char <= "M":
                # Reverse shift backward by n (shift forward)
                shift = n % 26
                new_char = chr(((ord(char) - ord("A") + shift) % 26) + ord("A"))
            else:
                # Reverse shift forward by m^2 (shift backward)
                shift = (m**2) % 26
                new_char = chr(((ord(char) - ord("A") - shift) % 26) + ord("A"))
        else:
            new_char = char
        decrypted.append(new_char)

    return "".join(decrypted)


def check_correctness(original_file, decrypted_text):
    try:
        with open(original_file, "r") as file:
            original_text = file.read()
    except FileNotFoundError:
        print(f"Error: {original_file} not found.")
        return False

    return original_text == decrypted_text


if __name__ == "__main__":
    try:
        n = int(input("Enter value for n: "))
        m = int(input("Enter value for m: "))
    except ValueError:
        print("Please enter valid integers for n and m.")
        exit()

    encrypted = encrypt_text(n, m)
    if encrypted:
        print("Text encrypted and saved to encrypted_text.txt")

        decrypted = decrypt_text(n, m, encrypted)
        print("\nDecrypted text:")
        print(decrypted)

        is_correct = check_correctness(
            raw_text_path,
            decrypted,
        )
        if is_correct:
            print("\nDecryption is correct!")
        else:
            print("\nDecryption is incorrect!")
    else:
        print("Encryption failed.")

import os

raw_text_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "raw_text.txt",
)


def shift_char(char, shift, direction):
    if not char.isalpha():
        return char

    base = ord("A") if char.isupper() else ord("a")
    offset = ord(char) - base

    if direction == "forward":
        new_offset = (offset + shift) % 26
    elif direction == "backward":
        new_offset = (offset - shift) % 26
    else:
        return char

    return chr(base + new_offset)


def encrypt_text(input_file, output_file, n, m, shift_log_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile, open(
        shift_log_file, "w"
    ) as log_file:
        for line in infile:
            encrypted_line = ""
            for char in line:
                if char.isalpha():
                    if char.islower():
                        if char <= "m":
                            shift = n * m
                            direction = "forward"
                        else:
                            shift = n + m
                            direction = "backward"
                    elif char.isupper():
                        if char <= "M":
                            shift = m * m
                            direction = "backward"
                        else:
                            shift = m * m
                            direction = "forward"

                    shifted = shift_char(char, shift, direction)
                    log_file.write(
                        f"{shift},{direction}\n"
                    )  # Write only shift and direction per letter
                    encrypted_line += shifted
                else:
                    log_file.write("0,none\n")  # Placeholder for non-alpha characters
                    encrypted_line += char
            outfile.write(encrypted_line)


def decrypt_text(input_file, output_file, shift_log_file):
    def decrypt_char(char, shift, direction):
        base = ord("A") if char.isupper() else ord("a")
        if direction == "forward":
            return chr((ord(char) - base - shift) % 26 + base)
        elif direction == "backward":
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    with open(input_file, "r") as infile, open(output_file, "w") as outfile, open(
        shift_log_file, "r"
    ) as log_file:
        for line in infile:
            decrypted_line = ""
            for char in line:
                shift_line = log_file.readline().strip()
                shift, direction = shift_line.split(",")
                shift = int(shift)

                if direction in ["forward", "backward"]:
                    decrypted_char = decrypt_char(char, shift, direction)
                else:
                    decrypted_char = char  # non-alphabetic characters

                decrypted_line += decrypted_char
            outfile.write(decrypted_line)


def main():
    n = int(input("Enter value for n: "))
    m = int(input("Enter value for m: "))

    input_file = raw_text_path
    encrypted_file = "encrypted_text.txt"
    decrypted_file = "decrypted_text.txt"
    shift_log_file = "shift_log.txt"

    encrypt_text(input_file, encrypted_file, n, m, shift_log_file)
    decrypt_text(encrypted_file, decrypted_file, shift_log_file)

    print("\nContents of raw_text.txt:")
    with open(input_file, "r") as f:
        print(f.read())

    print("\nContents of encrypted_text.txt:")
    with open(encrypted_file, "r") as f:
        print(f.read())

    print("\nContents of decrypted_text.txt:")
    with open(decrypted_file, "r") as f:
        print(f.read())

    with open(input_file, "r") as f1, open(decrypted_file, "r") as f2:
        if f1.read() == f2.read():
            print("\n✅ Decryption is correct!")
        else:
            print("\n❌ Decryption is incorrect!")


if __name__ == "__main__":
    main()

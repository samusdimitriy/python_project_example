message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ' ' <= ch <= '`':
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            encoded_message += ch
            continue
        pos = ord(ch) - ord(' ')
        pos = (pos + offset) % 94
        new_char = chr(pos + ord(" "))
        encoded_message += new_char
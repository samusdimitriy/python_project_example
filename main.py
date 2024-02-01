message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():
        if ch.islower():
            pos = ord(ch) - ord('a')
            pos = (pos + offset) % 26
            new_char = chr(pos + ord('a'))
            encoded_message += new_char
        else:
            pos = ord(ch) - ord('A')
            pos = (pos + offset) % 26
            new_char = chr(pos + ord('A'))
            encoded_message += new_char
    else:
        encoded_message += ch
        
print(encoded_message)
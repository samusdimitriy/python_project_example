import math

def decode(message_file):
    with open(message_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    message = ''
    line_number = 1
    total_lines = len(lines)

    for i in range(total_lines):
        if i == int(line_number * (line_number + 1) / 2) - 1:
            message += lines[i].split()[1] + ' '
            line_number += 1

    return message.strip()


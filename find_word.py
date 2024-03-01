import re

s = "I bought 77 nuts for 6$ and 110 bolts for 3$."




def find_all_words(text, word):
    found_list = re.findall(word, text, re.IGNORECASE)
    return found_list

print(find_all_words(s, r'\d+')) # ['77', '6', '110', '3']

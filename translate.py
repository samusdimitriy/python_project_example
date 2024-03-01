"""replace_dict = {ord("u"): "a"}
text = "sun"
print(text.translate(replace_dict))
"""
"""
txt = "sun"
my_table = txt.maketrans("u", "o")
print(txt.translate(my_table))  
"""
"""
txt = "sun"
my_table = txt.maketrans("sun", "tot")
print(txt.translate(my_table))  """

"""
CYRILLIC = ("а", "ч", "ш")
LATIN = ("a", "ch", "sh")

TRANSLIT_DICT = {}

for c, l in zip(CYRILLIC, LATIN):
    TRANSLIT_DICT[ord(c)] = l
    TRANSLIT_DICT[ord(c.upper())] = l.upper()
print(TRANSLIT_DICT)  # {1072: 'a', 1047: 'Ch', 1096: 'sh', 1040: 'A', 1063: 'Ch', 1097: 'Sh'}
print("чаша".translate(TRANSLIT_DICT))  # chasha
print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA"""



CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

def translate(name):
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return name.translate(TRANS)

print(translate("Дмитрий Коробов")) 
print(translate("Андрей Борисович"))  

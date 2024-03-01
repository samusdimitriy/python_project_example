def sanitize_phone_number(phone):
    return phone.strip().removeprefix("+").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

def get_phone_numbers_for_countries(list_phones):
    sorted_list = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": []
    }
    country_prefixes = {
        "JP": "81",
        "SG": "65",
        "TW": "886"
    }
    
    for phone in list_phones:
        new_phone = sanitize_phone_number(phone)
        for country, prefix in country_prefixes.items():
            if new_phone.startswith(prefix):
                sorted_list[country].append(new_phone)
                break
        else:
            sorted_list["UA"].append(new_phone)
    
    return sorted_list

phones = [
    "+380501234567",
    "+819012345678",
    "+819012345678",
    "+886987654321",
    "+819012345678",
    "+380501234567",
    "+380501234567",
    "+819012345678",
    "+819012345678",
]

print(get_phone_numbers_for_countries(phones))

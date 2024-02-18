# def is_valid_pin_codes(pin_codes):
#     if not pin_codes:  # Проверяем, что список не пустой
#         return False
    
#     # Проверяем, что все элементы списка являются строками длиной 4 и содержат только цифры
#     return all(isinstance(pin, str) and pin.isdigit() and len(pin) == 4 for pin in pin_codes) and len(set(pin_codes)) == len(pin_codes)  
# # Проверяем, что нет дубликатов

def is_valid_password(password):
    # Проверяем, что пароль не пустой
    if not password:
        return False
    
    # Проверяем, что длина пароля равна 8
    if len(password) != 8:
        return False
    
    # Проверяем, что в пароле есть хотя бы одна заглавная буква
    has_uppercase = any(char.isupper() for char in password)
    
    # Проверяем, что в пароле есть хотя бы одна строчная буква
    has_lowercase = any(char.islower() for char in password)
    
    # Проверяем, что в пароле есть хотя бы одна цифра
    has_digit = any(char.isdigit() for char in password)
    
    # Возвращаем результат проверки всех условий
    return has_uppercase and has_lowercase and has_digit

# Пример использования:
print(is_valid_password("Password1"))  # Выведет: True

'''
У нас есть три логические переменные.

Первая определяет статус пользователя is_active, которая равна True или False.
Вторая is_admin определяет, есть ли у пользователя права администратора, булевого типа.
Третья is_permission — разрешен ли доступ, тоже булевого типа.
Приведите переменные is_active, is_admin и is_permission к булевому виду.

Присвойте переменной access значение, которое покажет, есть ли доступ у пользователя. Используйте логические операторы.

Администратор всегда имеет доступ, независимо от значений переменных is_permission и is_active.

Пользователь имеет доступ, только если is_permission равен True и is_active также равен True.
'''

is_active = bool(input("Is the user active? "))
is_admin = bool(input("Is the user administrator? "))
is_permission = bool(input("Does the user have access? "))

access = is_admin or is_active and is_permission


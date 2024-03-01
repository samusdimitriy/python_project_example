def get_employees_by_profession(path, profession):
    # Инициализация списка для хранения имен сотрудников указанной профессии
    employee_names = []

    # Открытие файла для чтения
    with open(path, 'r') as file:
        # Чтение всех строк из файла
        lines = file.readlines()

        # Перебор всех строк файла
        for line in lines:
            # Разделение строки на имя и должность
            name, emp_profession = line.strip().split(' ', 1)
            print(name)
            # Проверка, соответствует ли должность указанной профессии
            if emp_profession == profession:
                # Добавление имени сотрудника в список
                employee_names.append(name)

    # Объединение имен в строку через пробел
    result = ' '.join(employee_names)

    # Возвращение итоговой строки
    return result

# Пример использования функции
path = "data.txt"  # Путь к файлу со списком сотрудников
profession = "cook"  # Профессия, по которой нужно найти сотрудников
result = get_employees_by_profession(path, profession)

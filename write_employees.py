def write_employees_to_file(employee_list, path):
    new_list = []
    for employee in employee_list:
        for e in employee:
            new_list.append(f"{e}\n")
    file = open(path, "w")
    file.writelines(new_list)
    file.close()

employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

write_employees_to_file(employee_list, "employees.txt")
        
            
                
    
        

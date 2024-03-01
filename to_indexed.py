def to_indexed(source_file, output_file):
    new_list = []
    with open(source_file, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            new_list.append(f"{i+1}: {line}")
        
    with open(output_file, 'w') as file:
        file.writelines(new_list)
        print("File created")

to_indexed("data.txt", "indexed_data.txt") # создаст файл indexed_data.txt с индексами строк
    
        
    
        
            
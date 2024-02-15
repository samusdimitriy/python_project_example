from pathlib import Path

current_path = Path("/Users/samsax/Documents/GitHub/python_project_example/__pycache__")
def parse_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            print(f"Folder: {el}")
        else:
            print(f"File: {el}")

parse_folder(current_path)

data = {
    2000: "Ford",
    2001: "Chevy",
    2002: "Toyota",
    2003: "Honda",
    2004: "Nissan",
    2005: "Dodge",
    2006: "GMC",
    2007: "Jeep",
    2008: "Buick",
    2009: "Cadillac", 
}

# for key, value in data.items():
    # print(f"{key}: {value}")

# data[2010] = "Tesla"
# print(data)

new_data = {
    2010: "Audi",
    2012: "BMW",
    2013: "Mercedes",
    2014: "Volkswagen",
    2015: "Mazda",
    2016: "Subaru",
    2017: "Kia",
    2018: "Hyundai",
    2019: "Volvo",
    2020: "Porsche",
}

# data.update(new_data)
# print(data)

# data[2004] += " (old)"
# print(data)
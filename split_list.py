# def split_list(grade):
#     if not grade:
#         return [], []
    
#     average = sum(grade) / len(grade)
    
#     lower = [x for x in grade if x <= average]
#     higher = [x for x in grade if x > average]
    
#     return lower, higher

def split_list(grade):
    if not grade:
        return [], []
    
    average = sum(grade) / len(grade)
    
    lower_grades = []
    higher_grades = []
    for x in grade:
        if x <= average:
            lower_grades.append(x)
        else:
            higher_grades.append(x)
    
    return lower_grades, higher_grades

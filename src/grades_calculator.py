import math

def calculate_weighted_average(grade, credits):
    if credits == 0:
        return "Not Started", 0.0
    return grade, credits

def calculate_overall_grades(thesis_grade, thesis_credits, basic_grade, basic_credits, 
                             compulsory_grade, compulsory_credits, elective_grade, elective_credits):
    
    individual_grades = []
    individual_credits = []

    # Calculate weighted averages for each category
    for grade, credits in [(thesis_grade, thesis_credits), (basic_grade, basic_credits), 
                           (compulsory_grade, compulsory_credits), (elective_grade, elective_credits)]:
        if grade > 0:
            individual_grades.append(grade)
            individual_credits.append(credits)

    if not individual_grades:
        return {"overall_grade": "Not Started"}

    overall_grade = sum(g * c for g, c in zip(individual_grades, individual_credits)) / sum(individual_credits)
    overall_grade = math.floor(overall_grade * 10) / 10  # Round down to the nearest decimal

    return {"overall_grade": overall_grade}

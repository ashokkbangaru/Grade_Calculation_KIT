import math

def calculate_weighted_average(df):
    if df.empty:
        return "Not Started", 0.0

    completed_courses = df[df['Grade'] > 0.0]
    if completed_courses.empty:
        return "Not Started", 0.0

    total_weighted_grades = (completed_courses['Grade'] * completed_courses['CP cur.']).sum()
    total_credit_points = completed_courses['CP cur.'].sum()
    weighted_average_grade = total_weighted_grades / total_credit_points
    rounded_grade = math.floor(weighted_average_grade * 10) / 10

    return rounded_grade, total_credit_points

def calculate_overall_grades(thesis_grade, thesis_credits, basic_grade, basic_credits, 
                             compulsory_grade, compulsory_credits, elective_grade, elective_credits):
    
    individual_grades = []
    individual_credits = []

    # Append valid grades and credits to lists
    for grade, credits in [(thesis_grade, thesis_credits), (basic_grade, basic_credits), 
                           (compulsory_grade, compulsory_credits), (elective_grade, elective_credits)]:
        if isinstance(grade, float) and credits > 0:  # Ensure the grade is a float and credits are valid
            individual_grades.append(grade)
            individual_credits.append(credits)

    if not individual_grades:
        return {"overall_grade": "Not Started"}

    overall_grade = sum(g * c for g, c in zip(individual_grades, individual_credits)) / sum(individual_credits)
    overall_grade = math.floor(overall_grade * 10) / 10  # Round down to the nearest decimal

    return {"overall_grade": overall_grade}

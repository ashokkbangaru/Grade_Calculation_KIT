from flask import Flask, render_template, request, jsonify
from grades_calculator import calculate_overall_grades

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/GRADE_CALCULATION_KIT', methods=['POST'])
def calculate_grades():
    data = request.json

    # Get grades and credit points from form submission
    thesis_data = data.get('thesis_grades', [])
    basic_data = data.get('basic_grades', [])
    compulsory_data = data.get('compulsory_grades', [])
    elective_data = data.get('elective_grades', [])

    # Calculate the overall grade using the backend logic
    thesis_grade, thesis_credits = calculate_weighted_average(thesis_data)
    basic_grade, basic_credits = calculate_weighted_average(basic_data)
    compulsory_grade, compulsory_credits = calculate_weighted_average(compulsory_data)
    elective_grade, elective_credits = calculate_weighted_average(elective_data)

    result = calculate_overall_grades(thesis_grade, thesis_credits, basic_grade, basic_credits,
                                      compulsory_grade, compulsory_credits, elective_grade, elective_credits)

    return jsonify(result)

def calculate_weighted_average(data):
    if not data:
        return 0, 0

    total_weighted_grades = sum(item['grade'] * item['credit'] for item in data)
    total_credit_points = sum(item['credit'] for item in data)

    if total_credit_points == 0:
        return 0, 0

    weighted_average = total_weighted_grades / total_credit_points
    return weighted_average, total_credit_points

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

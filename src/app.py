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
    thesis_grade = float(data.get('thesis_grade', 0))
    thesis_credits = float(data.get('thesis_credits', 0))
    basic_grade = float(data.get('basic_grade', 0))
    basic_credits = float(data.get('basic_credits', 0))
    compulsory_grade = float(data.get('compulsory_grade', 0))
    compulsory_credits = float(data.get('compulsory_credits', 0))
    elective_grade = float(data.get('elective_grade', 0))
    elective_credits = float(data.get('elective_credits', 0))

    # Calculate the overall grade using the backend logic
    result = calculate_overall_grades(thesis_grade, thesis_credits, basic_grade, basic_credits,
                                      compulsory_grade, compulsory_credits, elective_grade, elective_credits)

    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

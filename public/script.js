function submitGrades() {
    const thesis_grade = document.getElementById('thesis_grade').value;
    const thesis_credits = document.getElementById('thesis_credits').value;
    const basic_grade = document.getElementById('basic_grade').value;
    const basic_credits = document.getElementById('basic_credits').value;
    const compulsory_grade = document.getElementById('compulsory_grade').value;
    const compulsory_credits = document.getElementById('compulsory_credits').value;
    const elective_grade = document.getElementById('elective_grade').value;
    const elective_credits = document.getElementById('elective_credits').value;

    const data = {
        thesis_grade,
        thesis_credits,
        basic_grade,
        basic_credits,
        compulsory_grade,
        compulsory_credits,
        elective_grade,
        elective_credits
    };

    fetch('/calculate_grades', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Overall Grade: ' + data.overall_grade;
    })
    .catch(error => console.error('Error:', error));
}

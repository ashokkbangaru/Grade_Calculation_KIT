function submitGrades() {
    const data = {
        thesis_grades: [],
        basic_grades: [],
        compulsory_grades: [],
        elective_grades: []
    };

    // Gather all grades and credits
    const gradeInputs = document.querySelectorAll('.grade');
    const creditInputs = document.querySelectorAll('.credit');

    gradeInputs.forEach((gradeInput, index) => {
        const category = gradeInput.className.split(' ')[1].split('_')[0]; // Extract category
        const grade = parseFloat(gradeInput.value) || 0; // Default to 0 if not a number
        const credit = parseFloat(creditInputs[index].value) || 0; // Default to 0 if not a number

        if (grade > 0 || credit > 0) { // Only include valid entries
            data[`${category}`].push({ grade, credit });
        }
    });

    fetch('/GRADE_CALCULATION_KIT', {
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

function addGradeInput(section) {
    const newInputHTML = `
        <input type="number" class="grade ${section.toLowerCase()}_grade" placeholder="Grade">
        <input type="number" class="credit ${section.toLowerCase()}_credits" placeholder="Credits">
    `;
    const gradesDiv = document.querySelector(`.${section.toLowerCase()}-grades`);
    const newDiv = document.createElement('div');
    newDiv.className = 'grades';
    newDiv.innerHTML = newInputHTML;
    gradesDiv.appendChild(newDiv);
}

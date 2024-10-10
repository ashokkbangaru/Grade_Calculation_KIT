import pandas as pd
import math
from tkinter import Tk, filedialog
import sys
import msvcrt

def calculate_weighted_average(df):
    # Check if the DataFrame is empty (no grades and credits)
    if df.empty:
        return "Not Started", 0.0

    # Filter out courses with a grade of 0.0 (assuming 0.0 means the course is not completed)
    completed_courses = df[df['Grade'] > 0.0]

    # Check if there are no completed courses
    if completed_courses.empty:
        return "Not Started", 0.0

    # Calculate weighted average
    total_weighted_grades = (completed_courses['Grade'] * completed_courses['CP cur.']).sum()
    total_credit_points = completed_courses['CP cur.'].sum()

    weighted_average_grade = total_weighted_grades / total_credit_points

    # Round the grade down to the nearest decimal point
    rounded_grade = math.floor(weighted_average_grade * 10) / 10

    return rounded_grade, total_credit_points

def calculate_individual_grades(excel_file_path):
    # Load the Excel file into a pandas DataFrame
    xls = pd.ExcelFile(excel_file_path)

    # Create separate DataFrames for each category
    thesis_df = pd.read_excel(xls, 'Thesis')
    basic_df = pd.read_excel(xls, 'Basic')
    compulsory_df = pd.read_excel(xls, 'Compulsory')
    elective_df = pd.read_excel(xls, 'Elective')

    # Calculate individual grades and total credits for each category
    thesis_grade, thesis_credits = calculate_weighted_average(thesis_df)
    basic_grade, basic_credits = calculate_weighted_average(basic_df)
    compulsory_grade, compulsory_credits = calculate_weighted_average(compulsory_df)
    elective_grade, elective_credits = calculate_weighted_average(elective_df)

    # Exclude modules with "Not Started" status when calculating overall grade
    individual_grades = [grade for grade in [thesis_grade, basic_grade, compulsory_grade, elective_grade] if grade != "Not Started"]
    individual_credits = [credit for credit in [thesis_credits, basic_credits, compulsory_credits, elective_credits] if credit != 0]

    # Calculate overall grade based on individual grades and total credits
    if not individual_grades:
        overall_grade = "Not Started"
    else:
        overall_grade = sum(individual_grades[i] * individual_credits[i] for i in range(len(individual_grades))) / sum(individual_credits)

    # Round down the overall grade to the nearest decimal point if it's not "Not Started"
    if overall_grade != "Not Started":
        overall_grade = math.floor(overall_grade * 10) / 10

    return thesis_grade, basic_grade, compulsory_grade, elective_grade, overall_grade

def check_keypress(root):
    # Check if a key has been pressed
    if msvcrt.kbhit():
        root.destroy()

    # Schedule the function to run again after 100 milliseconds
    root.after(100, check_keypress, root)

def main():
    # Developer and version information
    developer_name = "\033[1;36mAshok Kumar Bangaru\033[0m"  # Cyan color
    version = "\033[1;36m1.0\033[0m"  # Cyan color
    powered_by = "\033[1;36mAITechSchool\033[0m"  # Cyan color

    print(f"Developer: {developer_name} | Version: {version} | Powered by: {powered_by}")

    print("Welcome! Please upload the Excel file with grades.")
    # Initialize the Tkinter root window (hidden)
    root = Tk()
    root.withdraw()

    # Ask the user to select the Excel file using a file dialog
    excel_file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel files", "*.xlsx;*.xls")],
    )

    # Check if the user selected a file
    if not excel_file_path:
        print("No file selected. Exiting.")
        return

    # Calculate individual grades for each category and overall grade
    thesis_grade, basic_grade, compulsory_grade, elective_grade, overall_grade = calculate_individual_grades(excel_file_path)

    # Adjust the print statements to handle "Not Started" strings
    print(f"Thesis Grade: {thesis_grade:.1f}" if isinstance(thesis_grade, float) else f"Thesis Grade: {thesis_grade}")
    print(f"Basic Grade: {basic_grade:.1f}" if isinstance(basic_grade, float) else f"Basic Grade: {basic_grade}")
    print(f"Compulsory Grade: {compulsory_grade:.1f}" if isinstance(compulsory_grade, float) else f"Compulsory Grade: {compulsory_grade}")
    print(f"Elective Grade: {elective_grade:.1f}" if isinstance(elective_grade, float) else f"Elective Grade: {elective_grade}")

    if isinstance(overall_grade, float):
        print(f"Overall Grade: {overall_grade:.1f}")
    else:
        print(f"Overall Grade: {overall_grade}")

    # Add a message to press any key before closing the window
    print("\nPress any key to close the window.")
    
    # Schedule the check_keypress function to run repeatedly
    root.after(100, check_keypress, root)

    # Keep the Tkinter main loop running
    try:
        root.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
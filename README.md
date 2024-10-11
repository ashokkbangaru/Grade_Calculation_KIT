# Grade_Calculation_KIT

Grade Calculator is a simple, user-friendly web application built using Python and Flask that helps students (Karlsruhe Institute of Technology) calculate their grades easily. Enter your course scores and corresponding credit points, and the app will calculate your weighted GPA or final grade.

This project is free and open for public use. Feel free to contribute or provide feedback to make it better!

## Features
1. Simple UI: Easy-to-use interface for calculating grades.
2. Weighted GPA Calculation: Calculates GPA based on input grades and credit points.
3. No Sign-Up Required: Immediate use without the need for user accounts.
4. Mobile-Responsive: Works smoothly on both desktop and mobile devices.

# Installation

## 1. Clone the Repository:
Clone this repository to your local machine:
```bash
git clone https://github.com/ashokkbangaru/Grade_Calculation_KIT.git
cd Grade_Calculation_KIT
```

## 2. Create a Virtual Environment:
Create a virtual environment to manage your dependencies:
```bash
# On macOS/Linux
python3 -m venv venv

# On Windows
python -m venv venv
```

## 3. Activate the Virtual Environment:
Activate the virtual environment:
```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

## 4. Install Dependencies:
Install the required Python packages:
```bash
pip install -r requirements.txt
```

## 5. Run the Application:
After the dependencies are installed, run the application:
```bash
cd .\src\
python .\app.py
```

## 6. Access the App:
Open your browser and go to:
```bash
http://127.0.0.1:5000/
```
## Live Demo
Want to try the app without setting it up locally? Check out our live demo hosted at:
https://grade-calculator-latest.onrender.com

# Publishing Docker Image to Docker Hub

Follow these steps to publish your Docker image from Docker Desktop to Docker Hub.

## Prerequisites:
1. **Install Docker Desktop**: Ensure Docker Desktop is installed and running.
2. **Docker Hub Account**: Create an account at [Docker Hub](https://hub.docker.com/) if you don't have one.
3. **Login to Docker Hub**: Log in via Docker Desktop or the command line.

## Steps to Publish Docker Image:

### 1. Log in to Docker Hub:

- **Via Docker Desktop**: Open Docker Desktop, click your account icon, and log in.
- **Via Command Line**: Run:
    ```bash
    docker login
    ```
  Enter your Docker Hub **username** and **password**.

### 2. Tag Your Docker Image:
Tag your local image using the format:
```bash
docker tag local-image-name dockerhub-username/repository-name:tag
```
Example: docker tag grade-calculator your-dockerhub-username/grade-calculator:latest

###  3. Push the Docker Image:
Push the image to Docker Hub:
```bash
docker push your-dockerhub-username/grade-calculator:latest
```


Enjoy using Grade Calculator! 😊

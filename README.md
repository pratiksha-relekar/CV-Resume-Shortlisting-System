# CV-Resume-Shortlisting-System

A Python web application that uses machine learning to analyze and score resumes based on job descriptions.

🌟 Features

Analyze and score resumes based on job descriptions.

Provide detailed feedback on skills, experience, education, and resume structure.

User-friendly interface with a modern look.

Responsive design for various devices.

Developed using Flask, HTML, CSS, and JavaScript.

Machine learning model to provide smart analysis and recommendations.

📱 Screens

Home Screen
Resume Upload Form: Users can upload their resumes and provide job details including title, description, responsibilities, required experience, skills, and education.

Submit Button: Submit the form to get resume analysis and score.

Analysis Screen

Displays the overall resume score and detailed feedback on different aspects such as skills match, experience match, education match, and resume structure.

🛠️ Technologies Used

Frontend: HTML, CSS, JavaScript

Backend: Python, Flask

Machine Learning: spaCy, transformers, scikit-learn

Other Libraries: Flask-WTF for form handling, docx for resume parsing

📝 Setup Instructions

Follow these steps to set up the project locally:

1. Clone the Repository
   
git clone https://github.com/yourusername/AI_Resume_Analyzer.git

cd AI_Resume_Analyzer

3. Create a Virtual Environment
   
python -m venv venv

source venv/bin/activate  # On Windows use: venv\Scripts\activate

5. Install Dependencies
   
pip install -r requirements.txt

7. Download and Install SpaCy Model
   
python -m spacy download en_core_web_sm

9. Run the Application
    
python run.py

Output 

![Screenshot 2024-09-14 181355](https://github.com/user-attachments/assets/97916218-e92b-4132-b105-9225c407c518)


![Screenshot 2024-09-14 181408](https://github.com/user-attachments/assets/7c3051b7-630c-41b0-bcec-bdf99e7a62f4)


![Screenshot 2024-09-14 181611](https://github.com/user-attachments/assets/8bf23548-750e-4d1c-ad7b-cef41f35ed86)


🎨 Customization

1. Update Styles
   
Modify the styles in static/css/styles.css to customize the look and feel of the app.

3. Update JavaScript
   
Adjust the JavaScript in static/js/scripts.js for additional interactivity.

4. Update Machine Learning Model
   
Update the machine learning model as needed for more accurate resume analysis.

from flask import render_template, flash, redirect, url_for, request  # Import necessary functions and modules from Flask
from . import main  # Import the main Blueprint from the current package
from .forms import ResumeForm  # Import the ResumeForm class from the forms module
from models.resume_parser import parse_resume, extract_text_from_docx  # Import functions from the resume_parser module
from models.job_description_parser import parse_job_description  # Import the parse_job_description function
from models.resume_scorer import score_resume, generate_feedback  # Import scoring and feedback functions from the resume_scorer module
from werkzeug.utils import secure_filename  # Import secure_filename function to safely handle filenames
import os  # Import the os module for operating system functionalities
import PyPDF2  # Import the PyPDF2 module for handling PDF files

# Define allowed file extensions for resume uploads
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

# Helper function to check if a file is allowed based on its extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to extract text from a PDF file using PyPDF2
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)  # Initialize PdfReader to read the PDF file
    text = ''
    for page_num in range(len(reader.pages)):  # Loop through each page in the PDF
        page = reader.pages[page_num]
        text += page.extract_text()  # Extract text from each page and add it to the text variable
    return text  # Return the extracted text

# Define the main route for the index page, allowing both GET and POST requests
@main.route('/', methods=['GET', 'POST'])
def index():
    form = ResumeForm()  # Instantiate the ResumeForm class

    # Check if the form is submitted and validated
    if form.validate_on_submit():
        resume_file = form.resume.data  # Get the uploaded resume file
        job_title = form.job_title.data  # Get the job title from the form
        job_description = form.job_description.data  # Get the job description from the form
        job_responsibilities = form.job_responsibilities.data  # Get the job responsibilities from the form
        job_experience = form.job_experience.data  # Get the required job experience from the form
        job_skills = form.job_skills.data  # Get the required job skills from the form
        job_education = form.job_education.data  # Get the required job education from the form

        # Check if the resume file is valid and allowed
        if resume_file and allowed_file(resume_file.filename):
            filename = secure_filename(resume_file.filename)  # Secure the filename
            file_extension = filename.rsplit('.', 1)[1].lower()  # Get the file extension

            # Extract text based on the file type
            if file_extension in {'doc', 'docx'}:
                resume_text = extract_text_from_docx(resume_file)  # Extract text from DOC/DOCX files
            elif file_extension == 'pdf':
                resume_text = extract_text_from_pdf(resume_file)  # Extract text from PDF files
            else:
                resume_text = resume_file.read().decode('utf-8', errors='ignore')  # Fallback for other file types

            # Parse the extracted resume text
            resume_data = parse_resume(resume_text)
            # Parse the job description and related details
            job_description_data = parse_job_description(
                job_description, job_responsibilities, job_experience, job_skills, job_education
            )
            # Score the resume against the job description
            scores = score_resume(resume_data, job_description_data)
            # Generate feedback based on the scoring
            feedback = generate_feedback(resume_data, job_description_data)

            # Flash messages to the user with the results
            flash(f'Overall Resume Score: {scores["total_score"]}%', 'success')
            flash(f'Details:', 'info')
            flash(f'Resume Structure: {scores["entity_score"]}%', 'info')
            flash(f'Skills Match: {scores["skills_score"]}%', 'info')
            flash(f'Experience Match: {scores["experience_score"]}%', 'info')
            flash(f'Education Match: {scores["education_score"]}%', 'info')
            flash(f'Issues: {feedback}', 'warning')

            # Redirect the user to the same page after processing
            return redirect(url_for('main.index'))

    # Render the index template with the form
    return render_template('index.html', form=form)

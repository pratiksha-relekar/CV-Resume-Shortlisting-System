from flask_wtf import FlaskForm  # Import the FlaskForm class from the flask_wtf module
from wtforms import FileField, StringField, TextAreaField, SubmitField  # Import specific field types from wtforms
from wtforms.validators import DataRequired  # Import the DataRequired validator

# Define a form class named ResumeForm that inherits from FlaskForm
class ResumeForm(FlaskForm):
    
    # Define a file upload field for the resume with a DataRequired validator
    resume = FileField('Resume', validators=[DataRequired()])
    
    # Define a string input field for the job title with a DataRequired validator
    job_title = StringField('Job Title', validators=[DataRequired()])
    
    # Define a text area input field for the job description with a DataRequired validator
    job_description = TextAreaField('Job Description', validators=[DataRequired()])
    
    # Define a text area input field for the job responsibilities with a DataRequired validator
    job_responsibilities = TextAreaField('Job Responsibilities', validators=[DataRequired()])
    
    # Define a text area input field for the required job experience with a DataRequired validator
    job_experience = TextAreaField('Required Experience', validators=[DataRequired()])
    
    # Define a text area input field for the required job skills with a DataRequired validator
    job_skills = TextAreaField('Required Skills', validators=[DataRequired()])
    
    # Define a text area input field for the required education with a DataRequired validator
    job_education = TextAreaField('Required Education', validators=[DataRequired()])
    
    # Define a submit button for the form
    submit = SubmitField('Submit')

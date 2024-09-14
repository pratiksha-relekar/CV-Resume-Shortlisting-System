import torch  # Import PyTorch, a deep learning library used here for tensor operations
from transformers import pipeline  # Import the pipeline function from the transformers library
from sklearn.metrics.pairwise import cosine_similarity  # Import cosine similarity function for measuring similarity between vectors

# Load a pre-trained transformer model for feature extraction using PyTorch (specified by 'pt')
nlp = pipeline('feature-extraction', model='distilbert-base-uncased', framework='pt')

# Function to calculate similarity between two pieces of text
def calculate_similarity(text1, text2):
    # Generate feature vectors for both texts using the pre-trained model
    vec1 = nlp(text1)
    vec2 = nlp(text2)

    # Perform average pooling on the vectors to get fixed-size vectors
    vec1_mean = torch.mean(torch.tensor(vec1), dim=1)
    vec2_mean = torch.mean(torch.tensor(vec2), dim=1)

    # Calculate cosine similarity between the two vectors
    similarity = cosine_similarity(vec1_mean, vec2_mean)[0][0]
    return similarity

# Function to check the structure of the resume
def check_resume_structure(resume_text):
    # Initialize a dictionary to track the presence of key sections in the resume
    sections = {
        'Contact Information': False,
        'Summary or Objective': False,
        'Skills': False,
        'Experience': False,
        'Education': False,
        'Certifications': False,
        'Projects': False
    }

    # Expanded keywords for section headers
    keywords = {
        'Contact Information': ['contact', 'email', 'phone', 'address'],
        'Summary or Objective': ['summary', 'objective', 'overview', 'profile'],
        'Skills': ['skill', 'competency', 'proficiency'],
        'Experience': ['experience', 'work history', 'professional experience', 'employment history'],
        'Education': ['education', 'academic background', 'qualifications'],
        'Certifications': ['certification', 'certificate', 'certifications'],
        'Projects': ['project', 'projects', 'portfolio']
    }

    # Check for the presence of section headers in the resume text
    lines = resume_text.split('\n')
    for line in lines:
        for section, section_keywords in keywords.items():
            if any(keyword in line.lower() for keyword in section_keywords):
                sections[section] = True

    # Calculate structure score as the percentage of detected sections
    structure_score = sum(sections.values()) / len(sections) * 100
    print(f"Debug: Detected sections: {sections}")
    return structure_score, sections

# Function to score the resume against the job description
def score_resume(resume_data, job_description_data):
    resume_entities = set(resume_data['entities'])  # Extract entities from the resume
    job_entities = set(job_description_data['keywords'])  # Extract keywords from the job description

    # Calculate entity match score as a percentage
    entity_score = len(resume_entities & job_entities) / len(job_entities) * 100 if job_entities else 0

    # Calculate similarity scores for skills, experience, and education
    skills_score = calculate_similarity(resume_data['skills'], job_description_data['skills']) * 100
    experience_score = calculate_similarity(resume_data['experience'], job_description_data['experience']) * 100
    education_score = calculate_similarity(resume_data['education'], job_description_data['education']) * 100

    # Check the resume structure and calculate the structure score
    structure_score, sections = check_resume_structure(resume_data['full_text'])

    # Calculate the total score as a weighted average of all the components
    total_score = 0.3 * entity_score + 0.3 * skills_score + 0.2 * experience_score + 0.2 * education_score + 0.1 * structure_score
    
    # Return a dictionary with the scores rounded to two decimal places and detected sections
    return {
        'total_score': round(total_score, 2),
        'entity_score': round(entity_score, 2),
        'skills_score': round(skills_score, 2),
        'experience_score': round(experience_score, 2),
        'education_score': round(education_score, 2),
        'structure_score': round(structure_score, 2),
        'sections': sections
    }

# Function to generate feedback for improving the resume
def generate_feedback(resume_data, job_description_data):
    feedback = []

    job_keywords = job_description_data['keywords']  # Get job-related keywords from the job description
    resume_skills = set(resume_data['skills'].split())  # Split and convert resume skills to a set
    resume_experience = set(resume_data['experience'].split())  # Split and convert resume experience to a set
    resume_education = set(resume_data['education'].split())  # Split and convert resume education to a set

    # Identify missing skills, experience, and education by comparing with job keywords
    missing_skills = job_keywords - resume_skills
    missing_experience = job_keywords - resume_experience
    missing_education = job_keywords - resume_education

    # Provide feedback for missing skills
    if missing_skills:
        feedback.append(
            f'Your skills section could be improved. Consider including skills such as: {", ".join(list(missing_skills)[:10])}.')

    # Provide feedback for missing experience
    if missing_experience:
        feedback.append(
            f'Your experience section could be improved. Consider including experiences such as: {", ".join(list(missing_experience)[:10])}.')

    # Provide feedback for missing education
    if missing_education:
        feedback.append(
            f'Your education section could be improved. Ensure it highlights education such as: {", ".join(list(missing_education)[:10])}.')

    # Check the resume structure and provide feedback on missing sections
    structure_score, sections = check_resume_structure(resume_data['full_text'])
    missing_sections = [section for section, present in sections.items() if not present]
    if missing_sections:
        feedback.append(f'Your resume is missing the following sections: {", ".join(missing_sections)}.')

    # Return the feedback as a single string
    return ' '.join(feedback)

import spacy  # Import the spaCy library for natural language processing (NLP)

# Load the small English NLP model provided by spaCy
nlp = spacy.load('en_core_web_sm')

# Function to extract keywords from a given text
def extract_keywords(text):
    doc = nlp(text)  # Process the text with the spaCy NLP model
    # Extract lemmatized keywords that are nouns, proper nouns, or adjectives and are not stopwords
    keywords = set([token.lemma_.lower() for token in doc if token.pos_ in {'NOUN', 'PROPN', 'ADJ'} and not token.is_stop])
    return keywords  # Return the set of extracted keywords

# Function to parse job description details and extract relevant information
def parse_job_description(job_description_text, job_responsibilities_text, job_experience_text, job_skills_text, job_education_text):
    # Combine all the job-related texts into one string
    combined_text = f"{job_description_text} {job_responsibilities_text} {job_experience_text} {job_skills_text} {job_education_text}"
    
    # Extract keywords from the combined text
    keywords = extract_keywords(combined_text)
    
    # Return a dictionary with the original texts and the extracted keywords
    return {
        'text': job_description_text,
        'responsibilities': job_responsibilities_text,
        'experience': job_experience_text,
        'skills': job_skills_text,
        'education': job_education_text,
        'keywords': keywords
    }

import spacy  # Import the spaCy library for natural language processing (NLP)
import docx  # Import the python-docx library to handle .docx files

# Load the small English NLP model provided by spaCy
nlp = spacy.load('en_core_web_sm')


# Function to extract text from a .docx file
def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)  # Open the .docx file
    full_text = []  # Initialize a list to hold the text from each paragraph
    for para in doc.paragraphs:  # Iterate over all paragraphs in the document
        full_text.append(para.text)  # Add the paragraph text to the list
    return '\n'.join(full_text)  # Join all paragraphs with a newline and return the full text


# Function to extract a specific section from the resume text
def extract_section(text, section_title):
    section = []  # Initialize a list to hold the lines in the section
    in_section = False  # A flag to indicate whether we are in the desired section
    for line in text.split("\n"):  # Iterate over each line in the text
        if section_title.lower() in line.lower():  # Check if the line contains the section title
            in_section = True  # Start capturing lines for this section
        elif in_section and line.strip() == "":  # Stop capturing when an empty line is found after the section starts
            break
        elif in_section:  # Continue capturing lines within the section
            section.append(line)
    return "\n".join(section)  # Join the captured lines with a newline and return the section text


# Function to parse the resume text and extract relevant information
def parse_resume(resume_text):
    doc = nlp(resume_text)  # Process the resume text with the spaCy NLP model

    # Extract specific sections from the resume
    skills = extract_section(resume_text, 'skills')
    experience = extract_section(resume_text, 'experience')
    education = extract_section(resume_text, 'education')

    # Return a dictionary containing the extracted information
    return {
        'skills': skills.lower(),  # Convert the skills section to lowercase
        'experience': experience.lower(),  # Convert the experience section to lowercase
        'education': education.lower(),  # Convert the education section to lowercase
        'entities': [ent.text for ent in doc.ents],  # Extract named entities from the resume text using spaCy
        'full_text': resume_text  # Include the full text of the resume
    }

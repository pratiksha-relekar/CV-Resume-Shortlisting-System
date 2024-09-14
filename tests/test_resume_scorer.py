import unittest  # Import the unittest module for creating and running tests
from models.resume_parser import parse_resume  # Import the parse_resume function to be tested
from models.job_description_parser import parse_job_description  # Import the parse_job_description function to be tested
from models.resume_scorer import score_resume  # Import the score_resume function to be tested

class TestResumeScorer(unittest.TestCase):  # Define a test case class that inherits from unittest.TestCase
    
    def test_score_resume(self):  # Define a test method to test the score_resume function
        resume_text = "John Doe\nSoftware Engineer\nSkills: Python, Java"  # Sample resume text for testing
        job_description_text = "Looking for a Software Engineer with experience in Python and Java."  # Sample job description text for testing

        resume_doc = parse_resume(resume_text)  # Call the parse_resume function with the sample resume text
        job_description_doc = parse_job_description(job_description_text)  # Call the parse_job_description function with the sample job description text

        score = score_resume(resume_doc, job_description_doc)  # Call the score_resume function to score the resume against the job description
        self.assertGreater(score, 0)  # Assert that the score is greater than 0, indicating some match

    def test_score_resume_with_no_skills_match(self):  # Test case where the resume does not match the job skills
        resume_text = "Pratiksha Relekar\nMarketing Manager\nSkills: SEO, Content Creation"  # Resume for a different job role
        job_description_text = "Looking for a Software Engineer with experience in Python and Java."  # Original job description text

        resume_doc = parse_resume(resume_text)  # Parse the resume text
        job_description_doc = parse_job_description(job_description_text)  # Parse the job description text

        score = score_resume(resume_doc, job_description_doc)  # Score the resume against the job description
        self.assertEqual(score['total_score'], 0)  # Assert that the total score is 0 due to no matching skills

    def test_score_resume_with_partial_match(self):  # Test case where the resume partially matches the job description
        resume_text = "Jane Doe\nSoftware Developer\nSkills: Python, SQL"  # Resume with partial skill match
        job_description_text = "Looking for a Software Engineer with experience in Python, Java, and C++."  # Job description with more skills

        resume_doc = parse_resume(resume_text)  # Parse the resume text
        job_description_doc = parse_job_description(job_description_text)  # Parse the job description text

        score = score_resume(resume_doc, job_description_doc)  # Score the resume against the job description
        self.assertGreater(score['skills_score'], 0)  # Assert that the skills score is greater than 0
        self.assertLess(score['skills_score'], 100)  # Assert that the skills score is less than 100, indicating a partial match

    def test_score_resume_with_exact_match(self):  # Test case where the resume exactly matches the job description
        resume_text = "John Doe\nSoftware Engineer\nSkills: Python, Java, C++\nExperience: 5 years\nEducation: BSc in Computer Science"
        job_description_text = "Looking for a Software Engineer with experience in Python, Java, and C++."

        resume_doc = parse_resume(resume_text)  # Parse the resume text
        job_description_doc = parse_job_description(job_description_text)  # Parse the job description text

        score = score_resume(resume_doc, job_description_doc)  # Score the resume against the job description
        self.assertEqual(score['total_score'], 100)  # Assert that the total score is 100 due to an exact match

if __name__ == '__main__':  # Run the tests if the script is executed directly
    unittest.main()  # Call unittest's main method to run the tests

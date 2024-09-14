import unittest  # Import the unittest module for creating and running tests
from models.resume_parser import parse_resume  # Import the parse_resume function to be tested

class TestResumeParser(unittest.TestCase):  # Define a test case class that inherits from unittest.TestCase

    def test_parse_resume(self):  # Define a test method to test the parse_resume function
        resume_text = "John Doe\nSoftware Engineer\nSkills: Python, Java"  # Sample resume text for testing
        doc = parse_resume(resume_text)  # Call the parse_resume function with the sample text
        self.assertIsNotNone(doc)  # Assert that the result is not None, indicating the function returned a valid result

    def test_parse_resume_with_empty_string(self):  # Another test case with an empty resume text
        resume_text = ""  # Empty resume text
        doc = parse_resume(resume_text)  # Call the parse_resume function with the empty text
        self.assertEqual(doc['skills'], "")  # Assert that skills section is empty
        self.assertEqual(doc['experience'], "")  # Assert that experience section is empty
        self.assertEqual(doc['education'], "")  # Assert that education section is empty

    def test_parse_resume_with_different_format(self):  # Another test case with a different format
        resume_text = "Jane Doe\nData Scientist\nExperience: 5 years\nSkills: Python, R, SQL\nEducation: MSc in Data Science"  # Different format
        doc = parse_resume(resume_text)  # Call the parse_resume function with the different format
        self.assertIn('python', doc['skills'])  # Assert that 'python' is in the skills section
        self.assertIn('data scientist', doc['entities'])  # Assert that 'Data Scientist' is recognized as an entity

    def test_parse_resume_with_unstructured_text(self):  # Another test case with unstructured text
        resume_text = "Skills: Java, C++\nExperienced in various programming languages.\nEducation: BSc Computer Science\nWork includes software development, testing."
        doc = parse_resume(resume_text)  # Call the parse_resume function with unstructured text
        self.assertIn('java', doc['skills'])  # Assert that 'Java' is in the skills section
        self.assertIn('computer science', doc['education'])  # Assert that 'Computer Science' is in the education section

if __name__ == '__main__':  # Run the tests if the script is executed directly
    unittest.main()  # Call unittest's main method to run the tests

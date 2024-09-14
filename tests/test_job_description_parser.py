import unittest  # Import the unittest module for creating and running tests
from models.job_description_parser import parse_job_description  # Import the parse_job_description function to be tested

# Define a test case class that inherits from unittest.TestCase
class TestJobDescriptionParser(unittest.TestCase):

    # Define a test method to test the parse_job_description function with a standard job description
    def test_parse_job_description(self):
        # Sample job description text for testing
        job_description_text = "Looking for a Software Engineer with experience in Python and Java."
        # Call the parse_job_description function with the sample text
        doc = parse_job_description(job_description_text)
        # Assert that the result is not None, indicating the function returned a valid result
        self.assertIsNotNone(doc)

    # Test case for an empty job description
    def test_parse_empty_job_description(self):
        job_description_text = ""  # Empty job description text
        doc = parse_job_description(job_description_text)  # Call the parse_job_description function with the empty text
        self.assertEqual(doc['keywords'], set())  # Assert that no keywords are extracted

    # Test case with a job description including multiple technologies and soft skills
    def test_parse_job_description_with_multiple_skills(self):
        job_description_text = "We need a Full Stack Developer skilled in React, Node.js, MongoDB, and with strong problem-solving abilities."
        doc = parse_job_description(job_description_text)  # Call the parse_job_description function
        self.assertIn('react', doc['keywords'])  # Assert that 'react' is in the extracted keywords
        self.assertIn('node.js', doc['keywords'])  # Assert that 'node.js' is in the extracted keywords
        self.assertIn('problem-solving', doc['keywords'])  # Assert that 'problem-solving' is in the extracted keywords

    # Test case for a job description with no clear skills or technologies
    def test_parse_job_description_without_technical_skills(self):
        job_description_text = "Looking for a team player who can adapt to a fast-paced environment and is eager to learn."
        doc = parse_job_description(job_description_text)  # Call the parse_job_description function
        self.assertIn('team player', doc['keywords'])  # Assert that 'team player' is in the extracted keywords
        self.assertIn('eager to learn', doc['keywords'])  # Assert that 'eager to learn' is in the extracted keywords

# Run the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()

import pyrebase
import random
import unittest

# Configuration for firebase
config = {
    "apiKey": "your_api_key",
    "authDomain": "your_auth_domain",
    "databaseURL": "your_database_url",
    "storageBucket": "your_storage_bucket",
    "serviceAccount": "path_to_your_service_account_key.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Function to get questions from Firebase
def get_questions(level, grade):
    path = f'questions/{level}/{grade}'
    return db.child(path).get().val()

# Function to create a test
def create_test(level, grade, num_questions):
    questions = get_questions(level, grade)
    if questions is None:
        return None
    return random.sample(questions, num_questions)

class TestFirebase(unittest.TestCase):
    def test_get_questions(self):
        questions = get_questions('level1', 'gradeA')
        self.assertIsNotNone(questions)

    def test_create_test(self):
        test = create_test('level1', 'gradeA', 10)
        self.assertIsNotNone(test)
        self.assertEqual(len(test), 10)

if __name__ == '__main__':
    unittest.main()

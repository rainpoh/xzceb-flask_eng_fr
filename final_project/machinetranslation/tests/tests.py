import unittest
from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(english_to_french(0))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(french_to_english(0))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
          
unittest.main()
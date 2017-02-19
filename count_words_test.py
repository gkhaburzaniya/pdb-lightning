import unittest

from count_words import count_words

class TestCountWords(unittest.TestCase):

    def test_sentence(self):
        word_count = count_words(
            "We went to the store and we bought some cookies.", "we")
        self.assertEqual(word_count, 2)

if __name__ == '__main__':
    unittest.main()

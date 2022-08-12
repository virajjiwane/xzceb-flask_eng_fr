import unittest

from translator import englishToFrench, frenchToEnglish

class TranslatorModuleTest(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')


if __name__=='__main__':
    unittest.main()

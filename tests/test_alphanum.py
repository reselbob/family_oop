from unittest import TestCase
from alphanum import AlphaNum

class TestAlphanum(TestCase):

    def test_char_get(self):
        an = AlphaNum()
        c = an.get_char(2)
        self.assertEqual(c, 'c')

    def test_bad_pos(self):
        an = AlphaNum()
        try:
            c = an.get_char(27)
        except Exception as ex:
            self.assertEqual(type(ex).__name__, 'AlphanumValidationError')


    def test_get_pos(self):
        an = AlphaNum()
        pos = an.get_position('c')
        self.assertEqual(pos, 2)

    def test_get_pos_upper(self):
        an = AlphaNum()
        pos = an.get_position('E')
        self.assertEqual(pos, 4)

    def test_get_default_language(self):
        an = AlphaNum()
        self.assertEqual(an.get_locale(), 'en-us')

    def test_get_french_language(self):
        an = AlphaNum('fr-fr')
        fr = an.get_french_alphabet()
        self.assertIsNotNone(fr)
        self.assertEqual(an.get_locale(), 'fr-fr')
        
    def test_get_french_language(self):
        an = AlphaNum('fr-fr')
        fr = an.get_french_alphabet()
        fra = ['a', 'à', 'á', 'ä', 'b', 'c', 'ç', 'd', 'e', 'è', 'é', 'ê', 'f', 'g', 'h', 'î', 'ï', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ô', 'œ', 'p', 'q', 'r', 's', 't', 'u', 'ù', 'ü', 'v', 'w', 'x', 'y', 'ÿ', 'z']
        self.assertEqual(fr,fra)

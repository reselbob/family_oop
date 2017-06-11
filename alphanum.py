import string
import locale

from alphanum_exception import AlphanumValidationError
class AlphaNum():
    def __init__(self, locale_code = ''):
        self.locale_code = locale_code
        self.fr_alphabet = None
        if self.locale_code == '':
            self.locale_code = 'en-us'
        print('I am some constructor behavior and the language I am supporting is: ' + self.locale_code)

    def get_french_chars(self):
        ## read up on unicode, https://en.wikipedia.org/wiki/List_of_Unicode_characters#Basic_Latin
        chrs = [['\u00E0','\u00E1','\u00E4'], ['\u00E7'], ['\u00E8','\u00E9','\u00EA'], ['\u00EE', '\u00EF'], ['\u00F4', '\u0153'], ['\u00F9', '\u00FC'], ['\u00FF']]
        return chrs

    def get_char(self, position):
        char = None
        try:
            char = list(self.get_alphabet(self.locale_code))[position]
            return char
        except Exception as ex:
            if(type(ex).__name__ == 'IndexError'):
                raise AlphanumValidationError({"message": "You passed a number which is outside of the range of the alphabet positions",
                                               "acceptable_range": "0-25",
                                               "value_passed": position})
            raise ex
    def get_position(self, character):
        return self.get_alphabet(self.locale_code).index(character.lower())

    def get_locale(self):
        return self.locale_code

    def get_french_alphabet(self):
        if self.fr_alphabet == None:
            fr_alphabet = list(string.ascii_lowercase)
            poss = [1,6,9,15,24,32,38]
            chrs = self.get_french_chars()
            for x in poss:
                pos = x
                car = chrs.pop(0)
                while len(car) != 0:
                    carr = car.pop(len(car)-1)
                    fr_alphabet.insert(pos, carr)
        self.fr_alphabet = fr_alphabet
        return fr_alphabet

    def get_german_alphabet(self):
        raise Exception('German alphabet not implemented')

    def get_alphabet(self, locale):
        if locale == 'en-us' : return string.ascii_lowercase
        if locale == 'fr-fr': return self.get_french_alphabet()
        raise Exception('Unknown locale, unsupported')



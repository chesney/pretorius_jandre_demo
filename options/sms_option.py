
'''
Created on 29 Jan 2015

@author: JANDRE-PRETORIUS
'''
from custom_exceptions import TranslationException
import re

class SMSOption(object):
    '''
    SMS styled translation. Snippet found on the web years ago, not all my own but customised a bit.
    Don't re-invent the wheel!
    '''
    #--------------------------------------------------------------
    def __init__(self):
        """
        """
        self._replace_ob = re.compile(r'\B[aeiou]\B')
        self._double_char_ob = re.compile(r'([a-z])\1+')
        self._punctuation_ob = re.compile(r'[^a-zA-Z0-9\s]')
    #--------------------------------------------------------------
    def translate(self, line):
        """
        Do the actual translation
        """
        try:

            lower_str = ""
            line = line.split()

            for word in line:
                lower_str += word.lower() + ' '

            # "find a letter, followed by one or more occurrences of that same letter"
            # Only replaces vowels that have a not-word-boundary, or vowels completely inside a word.
            replace = self._replace_ob.sub('', lower_str)
            double_char = self._double_char_ob.sub(r'\1', replace)

            return self._punctuation_ob.sub('', double_char)

        except Exception, e:
            raise TranslationException(e)

#--------------------------------------------------------------------------
def getHandler():
    """
    """
    return SMSOption()

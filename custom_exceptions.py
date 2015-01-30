"""
Custom exceptions for translations
"""

import utilities
#===================================================================
class TranslationExceptionBase(Exception):
    """
    Base exception class handler
    """
    #--------------------------------------------------------------
    def __init__(self):
        """ 
        """
        self.error_message = ''

    #--------------------------------------------------------------
    def _explainExcepotion(self):
        """
        """
        raise NotImplementedError

#===================================================================
class InvalidFileException(TranslationExceptionBase):
    """
    Passed in file is not of type file
    """

    #--------------------------------------------------------------
    def __init__(self, err=None):
        """
        """
        super(InvalidFileException, self).__init__()
        self._err = err
        self.error_message = self._explainException()

    #--------------------------------------------------------------
    def __str__(self):
        """
        """
        return str(self.error_message)

    #--------------------------------------------------------------
    def _explainException(self):
        """
        Returns a brief explanation why the exception has been called
        """
        text = """Invalid File Type Exception -- Please supply an object of type file. 
                 File objects are implemented using C's stdio package and can be created with the built-in open() function. 
                 File objects are also returned by some other built-in functions and methods, such as os.popen() and os.fdopen() 
                 and the makefile() method of socket objects. Temporary files can be created using the tempfile module, and high-level 
                 file operations such as copying, moving, and deleting files and directories can be achieved with the shutil module. %s""" % (self._err if self._err else '')

        return utilities.formatText(text, 300)

#===================================================================
class ImportException(TranslationExceptionBase):
    """
    Imported resource not found
    """

    #--------------------------------------------------------------
    def __init__(self, err=None):
        """
        """
        super(ImportException, self).__init__()
        self._err = err
        self.error_message = self._explainException()

    #--------------------------------------------------------------
    def __str__(self):
        """
        """
        return str(self.error_message)

    #--------------------------------------------------------------
    def _explainException(self):
        """
        Returns a brief explanation why the exception has been called
        """
        text = """Import Not Found Exception -- The requested resource could not be imported %s""" % (self._err if self._err else '')

        return utilities.formatText(text)


#===================================================================
class TranslationException(TranslationExceptionBase):
    """
    Exception while translating
    """

    #--------------------------------------------------------------
    def __init__(self, err=None):
        """
        """
        super(TranslationException, self).__init__()
        self._err = err
        self.error_message = self._explainException()

    #--------------------------------------------------------------
    def __str__(self):
        """
        """
        return str(self.error_message)

    #--------------------------------------------------------------
    def _explainException(self):
        """
        Returns a brief explanation why the exception has been called
        """
        text = """Translation Exception -- The requested file could not be translated %s""" % (self._err if self._err else '')

        return utilities.formatText(text)

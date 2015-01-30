'''
Created on 29 Jan 2015

@author: JANDRE-PRETORIUS

This controller consists of helper functions to  *TRY* translate English words to a specified option... best effort
'''

import settings
from custom_exceptions import InvalidFileException, ImportException

#===================================================================
class TransaltaionController(object):
    '''
    '''

    #--------------------------------------------------------------
    def __init__(self, file_to_transalte, exit_file_name="exit_file.txt"):
        '''
        '''
        self.file_to_translate = file_to_transalte
        self._parsed_file_data = []
        self._handler = None
        self._exit_file = open(exit_file_name, "w")

        self.result_message = "Unsuccessful Translation"
    #--------------------------------------------------------------
    def serviceTranslation(self):
        '''
        Entry point for all translation related activities
        '''

        self._validateFileType()

        # If we get here we can assume this is a  type(file)
        map(self._parsed_file_data.append, [line for line in self.file_to_translate])

        self._getHandler()

        if not self._handler:
            raise ImportException('No handler')

        with self._exit_file as exit_file:
            for line in self._parsed_file_data:
                exit_file.write(str(self._handler.translate(line) + '\n'))

        self._exit_file.close()
        self.file_to_translate.close()

        self.result_message = "Successful Translation"
    #--------------------------------------------------------------
    def _validateFileType(self):
        """
        Ensure we are dealing with a dinkum file
        """
        if type(self.file_to_translate) != file:
            raise InvalidFileException()

    #--------------------------------------------------------------------------
    def _importOption(self, option):
        """
        Import the option handler
        """
        return __import__(
            'options.%s' % option,
            globals(),
            locals(),
            [option]
        )

    #--------------------------------------------------------------
    def _getHandler(self, option=settings.TRANSLATION_OPTION):
        """
        Get the needed handler
        """
        try:

            importer = self._importOption(option)
            self._handler = importer.getHandler()

        except Exception, err:
            raise ImportException(err)

    #--------------------------------------------------------------
    def getResultMessage(self):
        """
        """
        return self.result_message

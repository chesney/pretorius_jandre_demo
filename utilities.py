'''
Created on 29 Jan 2015

@author: JANDRE-PRETORIUS

'''

#--------------------------------------------------------------
def formatText(text, line_width=20):
    """
    Returns a block of text formatted to a specified number of chars per line
    """
    wrap_length = int(line_width)
    index_split = text.split(' ')
    text_return = ''
    for index in range(0, len(index_split)):
        """
        Iterate over element in text until max length reached then split and 
        concat onto return var
        """
        current_line = text_return.split('\n')[-1]
        if (len(current_line) + len(index_split[index]) + 1) > wrap_length:
            text_return += '\n' + index_split[index]
        else:
            if len(current_line) == 0 :
                text_return += index_split[index]
            else:
                text_return += ' ' + index_split[index]

    return text_return

#------------------------------------------------------------------------------


if __name__ == '__main__':

    print formatText('lorem ipsume foo bar one two three')
    print '%s' % (100 * '-')
    print formatText('lorem ipsume foo bar one two three', 30)
    print '%s' % (100 * '-')
    print formatText('lorem ipsume foo bar one two three', 300)
    print '%s' % (100 * '-')
    print formatText('lorem ipsume foo bar one two three', 1)

'''
Created on 29 Jan 2015

@author: JANDRE-PRETORIUS

Small snippit to demonstrate basic Python litracy. Application reads in The Adventures of Huckleberry Finn
and tries to translate it into SMS speak. Application dumps translated output to screen. 

Custom exceptions have been introduced and is also demonstrated in this main.

'''

import transalation_cntrl
import decimal

if __name__ == '__main__':

    # Happy Flow
    print "Happy Flow"
    try:
        correct_file = open("pg76.txt", "r")
        controller = transalation_cntrl.TransaltaionController(correct_file, exit_file_name="happy_flow.txt")
        controller.serviceTranslation()

        print controller.getResultMessage()
        print "\n Translated Text\n============================"
        exit_file = open("happy_flow.txt")

        count = 0
        for line in exit_file:
            print line,
            count += 1
            if count == 100:
                print "\n\n\ntruncating ...\n\n\n"
                break

        exit_file.close()

    except Exception, e:
        print e

    print 100 * '=' + '\n'

    # Invalid file type raising a custom exception
    print "Invalid File type"
    try:
        non_file_type_obj = decimal.Decimal("1.1")
        controller = transalation_cntrl.TransaltaionController(non_file_type_obj, exit_file_name="non_happy_flow.txt")

        controller.serviceTranslation()
        print controller.getResultMessage()

    except Exception, e:
        print e

    raw_input("\n\n\n\nPress Enter to exit...")

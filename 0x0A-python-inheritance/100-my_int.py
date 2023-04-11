#!/usr/bin/python3
""" Switches  == operator with  != operator """


Class MyInt(int):
    """ Subclass of int implementing switch """
    def __eq__(self, value):
        """ Inverted == operator """
        return super().__ne__(value)

    def __ne__(self, value):
        """ Inverted != operator """
        return super().__eq__(value)

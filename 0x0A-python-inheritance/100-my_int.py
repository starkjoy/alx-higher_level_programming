#!/usr/bin/python3
""" Switches  == operator with  != operator """


Class MyInt(int):
    """ Subclass of int implementing switch """
    def __eq__(self, other):
        """ Inverted == operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Inverted != operator """
        return super().__eq__(other)

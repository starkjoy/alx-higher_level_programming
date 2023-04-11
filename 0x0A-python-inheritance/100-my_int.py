#!/usr/bin/python3
""" Switches  == operator with  != operator """


class MyInt(int):
    """ Subclass of int implementing switch """
    def __eq__(self, value):
        """ Inverted == operator """
        return self.real != value

    def __ne__(self, value):
        """ Inverted != operator """
        return self.real == value

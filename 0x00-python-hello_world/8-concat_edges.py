#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
        language that combines remarkable power with very clear syntax"
str = str[35:60] + str[96:100] + str[:6] + str[:5] + str[:61]
print(str)

#!/usr/bin/python3
"""function that inserts a line of text to a file, 
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each line
    containing a specific string 

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    lines = ""
    with open(filename) as r:
        for line in r:
            lines += line
            if search_string in line:
                lines += new_string
    with open(filename, "w") as w:
        w.write(lines)

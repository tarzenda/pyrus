__author__ = 'Peter'
def one_line():
    print()

def three_lines():
    one_line()
    one_line()
    one_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()

clear_screen()

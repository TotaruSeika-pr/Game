from sys import platform

def GameInitialization():
    global separator
    if platform == 'linux' or platform == 'linux2':
        separator = '/'
    elif platform == 'win32':
        separator = '\\'
    else:
        print('OS unknown to the program!')
        return False
    
    return True

def YesOrNoChecking(arg):
    if arg == 'y' or arg == 'yes':
        return True
    elif arg == 'n' or arg == 'no':
        return False
    else:
        SyntaxError()

def SyntaxError():
    print('Incorrect syntax!')